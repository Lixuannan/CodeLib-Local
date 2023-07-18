from .pyui.mainui import *
from .pyui.problem_view import *
from .pyui.get_info import *
from .pyui.info_page import *
from .pyui.choose_oj_page import *

import pyperclip

import queue

data_stream = queue.Queue()


class Info(QDialog, Ui_Info_Page):
    def __init__(self, title: str, info: str):
        super(Info, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(title)
        self.textBrowser.setText(info)
        self.exec()


# show a problem
class ShowProblem(QDialog, Ui_problem_view):
    def __init__(self, site: str, problem: str, code: str):
        super(ShowProblem, self).__init__()
        self.code = ""
        self.setup_all(site, problem, code)
        self.exec()

    # Setup everything in this class
    def setup_all(self, site: str, problem: str, code: str):
        self.setupUi(self)
        self.code = code
        self.site.setText(site)
        self.problem.setText(problem)
        self.code_browser.setText(code)
        self.pushButton.clicked.connect(self.copy_code)

    # Copy all code of this problem
    def copy_code(self):
        pyperclip.copy(self.code)


# Get some info
class GetInfo(QDialog, Ui_Get_Info):
    def __init__(self, info_name: str):
        super(GetInfo, self).__init__()
        self.setupUi(self)
        self.label.setText(info_name)
        self.buttonBox.clicked.connect(self.get_value)
        self.exec()

    # Get value of the info which you want to know, then send it to "data_stream"
    def get_value(self):
        data_stream.put(self.info_line.text())
        self.close()


class UI:
    # Initialize the ui of the application
    def __init__(self):
        self.app = QApplication()
        self.main_widget = QWidget()
        self.main = Ui_MainWidget()

        self.main.setupUi(self.main_widget)

    # Show information with tile
    @staticmethod
    def show_info(title: str, info: str):
        Info(title=title, info=info)

    # Show problem
    @staticmethod
    def show_problem(site: str, problem: str, code: str):
        ShowProblem(site=site, problem=problem, code=code)

    # Get information
    @staticmethod
    def get_info(info_name: str):
        GetInfo(info_name=info_name)
        return data_stream.get()


