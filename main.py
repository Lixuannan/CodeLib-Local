import logging
import queue
import sys
import time
from threading import Thread

import requests
from PySide6.QtCore import Signal, QObject
from PySide6.QtWidgets import QWidget, QDialog, QApplication
from bs4 import BeautifulSoup

import ui

data_stream = queue.Queue()
progress = 0


class Info(QDialog, ui.Ui_Info_Page):
    def __init__(self, title: str, info: str):
        super(Info, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(title)
        self.textBrowser.setText(info)
        self.exec()


class GetInfo(QDialog, ui.Ui_Get_Info):
    def __init__(self, info_name: str):
        super(GetInfo, self).__init__()
        self.setupUi(self)
        self.label.setText(info_name)
        self.buttonBox.clicked.connect(self.get_value)
        self.exec()

    def get_value(self):
        data_stream.put(self.info_line.text())
        self.close()


class ShowProblem(QDialog, ui.Ui_problem_view):
    def __init__(self, site: str, problem: str, code: str):
        super(ShowProblem, self).__init__()
        self.setupAll(site, problem, code)
        self.exec()

    def setupAll(self, site: str, problem: str, code: str):
        self.setupUi(self)
        self.site.setText(site)
        self.problem.setText(problem)
        self.code_browser.setText(code)


class Main(ui.Ui_MainWidget, QObject):
    ShowInfoSignal = Signal()

    def __init__(self):
        super().__init__()
        self.db = {}
        self.log = logging.getLogger("CodeLib-Log")
        self.load_data()

    def setupAll(self, mainWindow):
        self.setupUi(mainWindow)
        self.sync.clicked.connect(self.sync_func)
        self.load_list()
        self.ShowInfoSignal.connect(lambda: Info(title=data_stream.get(), info=data_stream.get()))
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
        self.luogu_session = requests.Session()

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

        if not self.db["luogu"]["info"]["username"]:
            GetInfo("luogu: Username 用户名: ")
            self.db["luogu"]["info"]["username"] = data_stream.get()
            with open("data.data", "wt") as f:
                f.write(str(self.db))

            self.load_data()
            self.load_list()

        if not self.db["luogu"]["info"]["password"]:
            GetInfo("luogu: Password 密码: ")
            self.db["luogu"]["info"]["password"] = data_stream.get()
            with open("data.data", "wt") as f:
                f.write(str(self.db))

            self.load_data()
            self.load_list()

        if not self.db["luogu"]["info"]["uid"]:
            GetInfo("luogu: UID :")
            self.db["luogu"]["info"]["uid"] = data_stream.get()
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
                Info(title="Error - 错误", info=error)
            else:
                Error("Unknown Error")

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

        need_update_problems = list(ac_problems_server - ac_problems_local)

        sync_thread = Thread(target=lambda: self.sync_oiclass_problems(need_update_problems))
        sync_thread.start()



    def sync_oiclass_problems(self, problems: list):
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
                    Error("Unknown Error")

            record = soup.find_all(name="a", class_="record-status--text pass")

            if record:
                records.append((record[0]["href"], i))
            else:
                page = self.oiclass_session.get(url=f"http://oiclass.com/p/{i}").text
                soup = BeautifulSoup(markup=page, features="lxml")
                record = soup.find_all(name="a", class_="record-status--text pass")
                if record:
                    records.append(record[0])

        for i in records:
            code = str(self.oiclass_session.get(f"http://oiclass.com{i[0]}?download=true").content.decode())
            if "<!DOCTYPE html>" in code:
                time.sleep(5)
                code = str(self.oiclass_session.get(f"http://oiclass.com{i[0]}?download=true").content.decode())

            self.db["oiclass"]["problems"].append({"pname": i[1], "code": code})

        with open("data.data", "wt") as f:
            f.write(str(self.db))

        self.load_data()
        self.load_list()

        data_stream.put("Finish - 完成")
        data_stream.put(
            f"""Finish Sync of Oiclass
            完成对 oiclass 的同步
            Total Add {len(problems)} Problems
            共新增 {len(problems)} 道题目
            They are （他们是）：
                {str(problems)}"""
        )

        self.ShowInfoSignal.emit()

    def load_list(self):
        self.problems.clear()
        for i in self.db["oiclass"]["problems"]:
            self.problems.addItem(f"oiclass-{i['pname']}")

    def load_data(self):
        with open("data.data", "rt") as f:
            self.db = eval(f.read())


if __name__ == '__main__':
    main = Main()
    app = QApplication()
    main_widget = QWidget()
    main.setupAll(main_widget)
    main_widget.show()
    sys.exit(app.exec())
