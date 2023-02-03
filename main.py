import logging
import os.path
import queue
import sys
import time
from concurrent.futures import ThreadPoolExecutor

import pyperclip
import requests
from PySide6.QtCore import Signal, QObject, Qt
from PySide6.QtWidgets import QWidget, QDialog, QApplication
from bs4 import BeautifulSoup

import ui

data_stream = queue.Queue()

DATA_TEMPLATE = r"{'oiclass': {'info': {'username': '', 'password': '', 'uid': ''}, 'problems': []}, 'hydro':{'info': "\
                r"{'username': '', 'password': '', 'uid': ''}, 'problems': []}}"


# show info
# 显示信息
class Info(QDialog, ui.Ui_Info_Page):
    def __init__(self, title: str, info: str):
        super(Info, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(title)
        self.textBrowser.setText(info)
        self.exec()


# get some info
# 获取必须的信息
class GetInfo(QDialog, ui.Ui_Get_Info):
    def __init__(self, info_name: str):
        super(GetInfo, self).__init__()
        self.setupUi(self)
        self.label.setText(info_name)
        self.buttonBox.clicked.connect(self.get_value)
        self.exec()

    # get value of the info which you want to know, then send it to "data_stream"
    # 获得信息的值，并发送到全局变量 "data_stream" 中
    def get_value(self):
        data_stream.put(self.info_line.text())
        self.close()


# show a problem
# 显示题目
class ShowProblem(QDialog, ui.Ui_problem_view):
    def __init__(self, site: str, problem: str, code: str):
        super(ShowProblem, self).__init__()
        self.setupAll(site, problem, code)
        self.exec()
        self.code = ""

    # setup everything in this class
    # 设置类中的所有乱七八糟的东西
    def setupAll(self, site: str, problem: str, code: str):
        self.setupUi(self)
        self.code = code
        self.site.setText(site)
        self.problem.setText(problem)
        self.code_browser.setText(code)
        self.pushButton.clicked.connect(self.copy_code)

    # copy all code of this problem
    # 复制题目的代码
    def copy_code(self):
        pyperclip.copy(self.code)


# let user choose what OJ they want to sync
# 让用户选择需要更新的 OJ
class ChooseOJ(QDialog, ui.Ui_Dialog):
    def __init__(self):
        self.data = []
        super(ChooseOJ, self).__init__()
        self.setupAll()
        self.exec()

    # setup everything in this class
    # 设置类中的所有乱七八糟的东西
    def setupAll(self):
        self.setupUi(self)
        self.accepted.connect(self.send_data)

    # send data to the "data_stream"
    # 将数据发送到全局变量 "data_stream"
    def send_data(self):
        if self.checkBox_1.checkState() == Qt.CheckState.Checked:
            self.data.append("oiclass")
        if self.checkBox_0.checkState() == Qt.CheckState.Checked:
            self.data.append("hydro")

        data_stream.put(self.data)


# main program
# 主程序
class Main(ui.Ui_MainWidget, QObject):
    ShowInfoSignal = Signal()

    def __init__(self):
        super().__init__()
        self.hydro_session = requests.Session()
        self.pool = ThreadPoolExecutor(1)
        self.oiclass_session = requests.Session()
        self.db = {}
        self.log = logging.getLogger("CodeLib-Log")
        self.load_data()

    # setup everything in this class
    # 设置类中的所有乱七八糟的东西
    def setupAll(self, mainWindow):
        self.setupUi(mainWindow)
        self.sync.clicked.connect(self.sync_func)
        self.load_list()
        self.ShowInfoSignal.connect(lambda: Info(title=data_stream.get(), info=data_stream.get()))
        self.problems.itemDoubleClicked.connect(lambda: self.show_problems(self.problems.selectedItems()[0]))
        self.keyword.textChanged.connect(self.search_func)

    # search problems
    # 搜索题目
    def search_func(self):
        keyword = self.keyword.text()
        if keyword == "":
            self.load_list()
            return 0

        self.problems.clear()
        for i in self.db["oiclass"]["problems"]:
            if keyword in f"oiclass-{i['pname']}":
                self.problems.addItem(f"oiclass-{i['pname']}")

        for i in self.db["hydro"]["problems"]:
            if keyword in f"hydro-{i['pname']}":
                self.problems.addItem(f"hydro-{i['pname']}")

    # Show problems in a problem view
    # 将题目详情展示出来
    def show_problems(self, problem):
        text = problem.text()
        info = text.split("-")
        for i in self.db[info[0]]["problems"]:
            if i["pname"] == info[1]:
                ShowProblem(site=info[0], problem=info[1], code=i["code"])

    # Call all sync function
    # 调用所有同于同步的函数
    def sync_func(self):
        ChooseOJ()
        sync_list = data_stream.get()
        for i in sync_list:
            eval(f"self.pool.submit(self.sync_{i}_problems)")

    # sync problems from hydro.ac
    # 同步来自 hydro.ac 的题目
    def sync_hydro_problems(self):
        if not self.db["hydro"]["info"]["username"]:
            GetInfo("hydro: Username 用户名: ")
            self.db["hydro"]["info"]["username"] = data_stream.get()
            self.load_data()
            self.load_list()

        if not self.db["hydro"]["info"]["password"]:
            GetInfo("hydro: Password 密码: ")
            self.db["hydro"]["info"]["password"] = data_stream.get()
            self.load_data()
            self.load_list()

        if not self.db["hydro"]["info"]["uid"]:
            GetInfo("hydro: UID :")
            self.db["hydro"]["info"]["uid"] = data_stream.get()
            self.load_data()
            self.load_list()

        page = self.hydro_session.post(url="https://hydro.ac/login", data={
            "uname": self.db["hydro"]["info"]["username"],
            "password": self.db["hydro"]["info"]["password"],
        }).text

        if "Oops!" in page:
            soup = BeautifulSoup(markup=page, features="lxml")
            error = soup.find_all(name="div", class_="error__text-container")
            if error:
                error = error[0].text
                Info(title="Error - 错误", info=error)
            else:
                Error("Unknown Error")

        ac_problems_server = set()
        ac_problems_local = set()

        for i in self.db["hydro"]["problems"]:
            ac_problems_local.add(i["pname"])

        page = self.hydro_session.get(url=f"https://hydro.ac/user/{self.db['hydro']['info']['uid']}").text
        soup = BeautifulSoup(markup=page, features="lxml")

        for i in soup.find_all(name="a"):
            if "p/" in i["href"]:
                ac_problems_server.add(i.text)

        problems = list(ac_problems_server - ac_problems_local)

        records = []
        for i in problems:
            page = self.hydro_session.get(
                url=f"https://hydro.ac/record?uidOrName=10952&pid=H1000&tid=&lang=&status=1").text
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
                page = self.hydro_session.get(url=f"https://hydro.ac/p/{i}").text
                soup = BeautifulSoup(markup=page, features="lxml")
                record = soup.find_all(name="a", class_="record-status--text pass")
                if record:
                    records.append(record[0])

        for i in records:
            code = str(self.hydro_session.get(f"https://hydro.ac{i[0]}?download=true").content.decode())
            if "<!DOCTYPE html>" in code:
                time.sleep(5)
                code = str(self.hydro_session.get(f"https://hydro.ac{i[0]}?download=true").content.decode())

            self.db["hydro"]["problems"].append({"pname": i[1], "code": code})

        with open("data.data", "wt") as f:
            f.write(str(self.db))

        self.load_data()
        self.load_list()

        data_stream.put("Finish - 完成")
        data_stream.put(
            f"""Finish Sync of Hydro
            完成对 hydro 的同步
            Total Add {len(problems)} Problems
            共新增 {len(problems)} 道题目
            They are （他们是）：
                {str(problems)}"""
        )

        self.ShowInfoSignal.emit()

    # Sync problems from oiclass.com
    # 同步来自 oiclass.com 的题目
    def sync_oiclass_problems(self):
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

        problems = list(ac_problems_server - ac_problems_local)

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

    # load problems from "self.db" to the GUI
    # 将 "self.db" 中的题目信息加载到页面中
    def load_list(self):
        self.problems.clear()
        for i in self.db["oiclass"]["problems"]:
            self.problems.addItem(f"oiclass-{i['pname']}")

        for i in self.db["hydro"]["problems"]:
            self.problems.addItem(f"hydro-{i['pname']}")

    # load data from "data.data" to "self.db"
    # 将 "data.data" 之中的数据读取到变量 "self.db" 中
    def load_data(self):
        with open("data.data", "rt") as f:
            self.db = eval(f.read())


if __name__ == '__main__':
    if not os.path.isfile("data.data"):
        with open("data.data", "wt") as file:
            file.write(DATA_TEMPLATE)
    main = Main()
    app = QApplication()
    main_widget = QWidget()
    main.setupAll(main_widget)
    main_widget.show()
    sys.exit(app.exec())
