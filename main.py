import logging
import sys
import queue
import traceback
from threading import Thread

import requests
from bs4 import BeautifulSoup
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QDialog, QApplication

import mainui
import error_page
import warming_page
import get_info
import sync_page
import problem_view


data_stream = queue.Queue()
progress = 0


class SyncPage(QDialog, sync_page.Ui_sync_page):
    progress_update_signal = Signal()

    def __init__(self):
        super(SyncPage, self).__init__()
        self.setupUi(self)
        self.exec()

    def update_progress(self):
        self.progressBar.setValue(progress)
        if progress >= 100:
            self.buttonBox.setUpdatesEnabled(True)

        self.update()


class Warming(QDialog, warming_page.Ui_warming_page):
    def __init__(self, warming: str):
        super(Warming, self).__init__()
        self.setupUi(self)
        self.warming.setText(warming)
        self.exec()


class Error(QDialog, error_page.Ui_error_page):
    def __init__(self, error: str):
        super(Error, self).__init__()
        self.setupUi(self)
        self.error_browser.setText(error)
        sys.exit(self.exec())


class GetInfo(QDialog, get_info.Ui_window):
    def __init__(self, info_name: str):
        super(GetInfo, self).__init__()
        self.setupUi(self)
        self.label.setText(info_name)
        self.buttonBox.clicked.connect(self.get_value)
        self.exec()

    def get_value(self):
        data_stream.put(self.info_line.text())
        self.close()


class ShowProblem(QDialog, problem_view.Ui_problem_view):
    def __init__(self, site: str, problem: str, code: str):
        super(ShowProblem, self).__init__()
        self.setupAll(site, problem, code)
        self.exec()

    def setupAll(self, site: str, problem: str, code: str):
        self.setupUi(self)
        self.site.setText(site)
        self.problem.setText(problem)
        self.code_browser.setText(code)


class Main(mainui.Ui_MainWidget):
    def __init__(self):
        self.db = {}
        self.log = logging.getLogger("CodeLib-Log")
        self.load_data()

    def setupAll(self, mainWindow):
        self.setupUi(mainWindow)
        self.sync.clicked.connect(self.sync_func)
        self.load_list()
        self.problems.itemDoubleClicked.connect(lambda: self.show_problems(self.problems.selectedItems()[0]))

    def show_problems(self, problem):
        text = problem.text()
        info = text.split("-")
        for i in self.db[info[0]]["problems"]:
            if i["pname"] == info[1]:
                ShowProblem(site=info[0], problem=info[1], code=i["code"])

    def sync_func(self):
        # Sync oiclass.com 同步 oiclass 的数据
        self.oiclass_session = requests.Session()

        # Check if info is completed 检查信息完整性
        if not self.db["oiclass"]["info"]["username"]:
            GetInfo("oiclass: Username 用户名: ")
            self.db["oiclass"]["info"]["username"] = data_stream.get()
            with open("data.data", "wt") as f:
                f.write(str(self.db))

            self.load_data()
            self.load_list()

        if not self.db["oiclass"]["info"]["password"]:
            GetInfo("oiclass: Password 密码: ")
            self.db["oiclass"]["info"]["password"] = data_stream.get()
            with open("data.data", "wt") as f:
                f.write(str(self.db))

            self.load_data()
            self.load_list()

        if not self.db["oiclass"]["info"]["uid"]:
            GetInfo("oiclass: UID :")
            self.db["oiclass"]["info"]["uid"] = data_stream.get()
            with open("data.data", "wt") as f:
                f.write(str(self.db))

            self.load_data()
            self.load_list()

        # login oiclass 登录 oiclass
        page = self.oiclass_session.post(url="http://oiclass.com/login/", data={
            "uname": self.db["oiclass"]["info"]["username"],
            "password": self.db["oiclass"]["info"]["password"]
        }).text

        if "Oops!" in page:
            soup = BeautifulSoup(markup=page, features="lxml")
            error = soup.find_all(name="div", class_="error__text-container")
            if error:
                error = error[0].text
                Error(error)
            else:
                Error("Unknow Error")

        page = self.oiclass_session.get(f"http://oiclass.com/user/{self.db['oiclass']['info']['uid']}").text
        soup = BeautifulSoup(markup=page, features="lxml")
        problems = soup.find_all(name="a")
        ac_problems_server = set()
        ac_problems_local = set()

        for i in problems:
            if "/p/" in i["href"]:
                ac_problems_server.add(i.text)

        for i in self.db["oiclass"]["problems"]:
            ac_problems_local.add(i["pname"])

        need_update_problems = ac_problems_server - ac_problems_local

        SyncPage()
        sync_thread = Thread(target=lambda: self.sync_oiclass_problems(need_update_problems))
        sync_thread.start()
        ###################
        # NEED A NEW PAGE #
        ###################

    def sync_oiclass_problems(self, problems: set):
        records = []
        for i in problems:
            page = self.oiclass_session.get(url=f"http://oiclass.com/record?"
                                                f"uidOrName={self.db['oiclass']['info']['uid']}&pid={i}&status=1").text
            soup = BeautifulSoup(markup=page, features="lxml")

            if "Oops!" in page:
                error = soup.find_all(name="div", class_="error__text-container")
                if error:
                    error = error[0].text
                    Error(error)
                else:
                    Error("Unknow Error")

            record = soup.find_all(name="a", class_="record-status--text pass")

            if record:
                records.append((record[0], i))
            else:
                page = self.oiclass_session.get(url=f"http://oiclass.com/p/{i}").text
                soup = BeautifulSoup(markup=page, features="lxml")
                record = soup.find_all(name="a", class_="record-status--text pass")
                if record:
                    records.append(record[0])
                else:
                    Warming(f"No record found from problem: {i}\n在题目 {i} 中未找到记录")

        records = list(set(records))

        for i in records:
            code = self.oiclass_session.get(f"{i[0]}?download=true").content
            self.db["oiclass"]["problems"].append({"pname": i[1], "code": code})

            with open("data.data", "wt") as f:
                f.write(str(self.db))

            self.load_data()
            self.load_list()

    def load_list(self):
        self.problems.clear()
        for i in self.db["oiclass"]["problems"]:
            self.problems.addItem(f"oiclass-{i['pname']}")

    def load_data(self):
        try:
            with open("data.data", "rt") as f:
                self.db = eval(f.read())
        except:
            exception = traceback.format_exc()
            self.log.error(exception)


if __name__ == '__main__':
    main = Main()
    app = QApplication()
    main_widget = QWidget()
    main.setupAll(main_widget)
    main_widget.show()
    sys.exit(app.exec())
