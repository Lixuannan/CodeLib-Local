# -*- coding: utf-8 -*-

import base64
import json
import sys
import os
import sqlite3
import shutil
import socket
import platform
from threading import Thread

import requests
import pyperclip
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QWidget, QDialog
from PySide6.QtGui import QShortcut, QKeySequence

import syncer
import ui.show_problem
from logger import Logger
from ui import main_window, setting, chooseOJ, massage, log, update

RESET_SQL = ("DROP TABLE problems; DROP TABLE settings; DROP TABLE default_sync; CREATE TABLE problems( pid text, "
             "site text, code text); CREATE TABLE settings( option TEXT, value TEXT, number_i INT, number_f FLOAT); "
             "INSERT INTO settings VALUES('loginWhenStartup',NULL,1,NULL); INSERT INTO settings VALUES("
             "'oiclassUsername','',NULL,NULL); INSERT INTO settings VALUES('oiclassPassword','',NULL,NULL); INSERT "
             "INTO settings VALUES('hydroojUsername','',NULL,NULL); INSERT INTO settings VALUES('hydroojPassword','',"
             "NULL,NULL); INSERT INTO settings VALUES('uojUsername','',NULL,NULL); INSERT INTO settings VALUES("
             "'uojPassword','',NULL,NULL); INSERT INTO settings VALUES('codeforcesUsername','',NULL,NULL); INSERT "
             "INTO settings VALUES('codeforcesPassword','',NULL,NULL); INSERT INTO settings VALUES('language',"
             "'Simplified Chinese',NULL,NULL); CREATE TABLE default_sync( site TEXT, onOroff BOOLEAN); INSERT INTO "
             "default_sync VALUES('Oiclass',0); INSERT INTO default_sync VALUES('HydroOJ',0); INSERT INTO "
             "default_sync VALUES('UOJ',0); INSERT INTO default_sync VALUES('Codeforces',0);")
LOGGER = Logger()
VERSION = "v1.1.4"
DATA_ROOT = os.path.join(os.getenv['APPDATA'], "CodeLib-Local") if platform.system() == "Windows" else os.path.join(os.getenv("HOME"), ".local/share/")


def load_list():
    main_widget.problems.clear()
    for i in db.execute("SELECT * FROM problems ORDER BY site, pid;"):
        main_widget.problems.addItem(f"{i[1]} - {i[0]}")


def save_settings():
    for i in settings:
        if type(settings[i]) == int or type(settings[i]) == bool:
            db.execute(f"UPDATE settings SET number_i = {settings[i]} WHERE option = \'{i}\';")
        elif type(settings[i]) == float:
            db.execute(f"UPDATE settings SET number_f = {settings[i]} WHERE option = \'{i}\';")
        elif type(settings[i]) == str:
            db.execute(f"UPDATE settings SET value = \'{settings[i]}\' WHERE option = \'{i}\';")

    for i in default_site:
        db.execute(f"UPDATE default_sync SET onOroff = {default_site[i]} WHERE site=\'{i}\'")

    db.commit()


def lcs(a: str, b: str) -> int:
    m, n = len(a), len(b)
    f = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                f[i][j] = f[i - 1][j - 1] + 1
            else:
                f[i][j] = max(f[i - 1][j], f[i][j - 1])

    return f[m][n]


def search():
    search_text = main_widget.keyword.text()
    if search_text == "":
        load_list()
        return
    main_widget.problems.clear()
    problems = []
    for i in db.execute("SELECT * FROM problems;"):
        x = lcs(search_text, i[0] + i[1] + base64.b32decode(i[2].encode("utf-8")).decode("utf-8"))
        if x > 0:
            problems.append((x, i[0], i[1]))

    problems.sort(reverse=True)
    for i in problems:
        main_widget.problems.addItem(f"{i[2]} - {i[1]}")


def show_settings():
    for i in settings:
        if 'Password' not in i:
            LOGGER.log(10, f"{i}: {settings[i]}")


class ShowProblem(ui.show_problem.Ui_show_problem, QDialog):
    def __init__(self, problem):
        super(ShowProblem, self).__init__()
        self.setupUi(self)
        p = problem.split(" - ")
        self.pidT = p[-1]
        self.siteT = " - ".join(p[:-1])
        self.pid.setText(self.pidT)
        self.site.setText(self.siteT)

        LOGGER.log(10, self.siteT)
        LOGGER.log(10, self.pidT)

        for i in db.execute(f"SELECT * FROM problems WHERE pid = '{self.pidT}' AND site = '{self.siteT}';"):
            self.codeT = base64.b32decode(i[2].encode("utf-8")).decode("utf-8")

        self.code.setText(self.codeT)
        self.copy.clicked.connect(self.cp)

        self.exec()

    def cp(self):
        pyperclip.copy(self.codeT)


class Setting(setting.Ui_settingPage, QDialog):
    def __init__(self):
        LOGGER.log(10, str(settings))
        super(Setting, self).__init__()
        self.setupUi(self)
        self.resetDbButton.clicked.connect(
            lambda: Massage("确认重置数据库？", accept=lambda: (db.executescript(RESET_SQL), db.commit())))
        self.dialogButtonBox.accepted.connect(self.save_and_exit)
        self.load_settings()

        self.exec()

    def save_and_exit(self):
        settings["loginWhenStartup"] = self.checkBox.isChecked()
        settings["language"] = self.LanguageComboBox.currentText()

        settings["oiclassUsername"] = self.oicAccInput.text()
        settings["oiclassPassword"] = self.oicPwdInput.text()
        settings["hydroojUsername"] = self.hydroAccInput.text()
        settings["hydroojPassword"] = self.hydroPwdInput.text()
        settings["uojUsername"] = self.uojAccInput.text()
        settings["uojPassword"] = self.uojPwdInput.text()
        settings["codeforcesUsername"] = self.cfAccInput.text()
        settings["codeforcesPassword"] = self.cfPwdInput.text()

        default_site["Oiclass"] = self.oicCheckBox.isChecked()
        default_site["HydroOJ"] = self.hydroCheckBox.isChecked()
        default_site["UOJ"] = self.uojCheckBox.isChecked()
        default_site["Codeforces"] = self.cfCheckBox.isChecked()

        save_settings()
        self.close()
        LOGGER.log(20, str(settings))
        p = sys.executable
        os.execl(p, p, *sys.argv)
        sys.exit(0)

    def load_settings(self):
        self.checkBox.setChecked(settings["loginWhenStartup"])
        self.LanguageComboBox.setCurrentText(settings["language"])

        self.oicAccInput.setText(settings["oiclassUsername"])
        self.oicPwdInput.setText(settings["oiclassPassword"])
        self.hydroAccInput.setText(settings["hydroojUsername"])
        self.hydroPwdInput.setText(settings["hydroojPassword"])
        self.uojAccInput.setText(settings["uojUsername"])
        self.uojPwdInput.setText(settings["uojPassword"])
        self.cfAccInput.setText(settings["codeforcesUsername"])
        self.cfPwdInput.setText(settings["codeforcesPassword"])

        self.oicCheckBox.setChecked(default_site["Oiclass"])
        self.uojCheckBox.setChecked(default_site["UOJ"])
        self.cfCheckBox.setChecked(default_site["Codeforces"])
        self.hydroCheckBox.setChecked(default_site["HydroOJ"])


class Massage(massage.Ui_massagePage, QDialog):
    def __init__(self, massage_text: str, accept=None, reject=None):
        super(Massage, self).__init__()
        self.setupUi(self)

        if accept is not None:
            self.massageButtonBox.accepted.connect(lambda: (self.close(), accept()))
            LOGGER.log(10, "self.accepted Connected to customize function")
        else:
            self.massageButtonBox.accepted.connect(self.accept)
            LOGGER.log(10, "self.accepted Connected to default self.accept")
        if reject is not None:
            self.massageButtonBox.rejected.connect(lambda: (self.close(), reject()))
            LOGGER.log(10, "self.rejected Connected to customize function")
        else:
            self.massageButtonBox.rejected.connect(self.reject)
            LOGGER.log(10, "self.rejected Connected to default self.reject")

        self.massageBrowser.setText(massage_text)
        self.exec()


class Log:
    def __init__(self):
        LOGGER.show()


class Update(update.Ui_UpdateDialog, QDialog):
    update_progress = Signal(int)
    finish = Signal()

    def __init__(self, update_url):
        super(Update, self).__init__()
        self.setupUi(self)
        self.update_url = update_url
        self.update_progress.connect(self.downloadProgress.setValue)
        self.ifUpdate.accepted.connect(self.update)
        self.ifUpdate.rejected.connect(self.close)
        self.finish.connect(self.close)
        self.exec()

    def download(self, url):
        LOGGER.log(20, f"Start Downloading from {self.update_url}")
        with open(os.path.join(DATA_ROOT, "CodeLib-Local", self.update_url.split("/")[-1]), "wb") as f:
            r = requests.get(self.update_url, stream=True)
            size = r.headers.get("content-length")
            for data in r.iter_content(chunk_size=1048576):
                f.write(data)
                self.update_progress.emit(int(f.tell() / int(size) * 100))
        LOGGER.log(20, "Finish Downloading")
        self.finish.emit()

    def update(self):
        self.downloadProgress.setEnabled(True)
        self.progressLabel.setEnabled(True)

        download_thread = Thread(target=self.download, args=(self.update_url,))
        download_thread.start()


class ChooseOJ(chooseOJ.Ui_chooseOJ, QDialog):
    def __init__(self):
        LOGGER.log(10, str(default_site))
        super(ChooseOJ, self).__init__()
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.sync)
        self.load_default_sites()
        self.exec()

    def load_default_sites(self):
        self.oiclassCheckBox.setChecked(default_site["Oiclass"])
        self.hydroOJCheckBox.setChecked(default_site["HydroOJ"])
        self.uojCheckBox.setChecked(default_site["UOJ"])
        self.cfCheckBox.setChecked(default_site["Codeforces"])

    def sync(self):
        self.close()

        if self.oiclassCheckBox.isChecked():
            if s.check_login("Oiclass"):
                s.sync("Oiclass")
            else:
                if settings["oiclassUsername"] == '':
                    Massage(massage_text="检测到 Oiclass 账号未登录且未配置，请前往配置后重新操作")
                else:
                    Massage(massage_text="检测到 Oiclass 账号未登录，是否登录并继续同步？",
                            accept=lambda: (s.login(site="Oiclass"),
                                            s.sync("Oiclass")))
        if self.hydroOJCheckBox.isChecked():
            if s.check_login("HydroOJ"):
                s.sync("HydroOJ")
            else:
                if settings["hydroojUsername"] == '':
                    Massage(massage_text="检测到 HydroOJ 账号未登录且未配置，请前往配置后重新操作")
                else:
                    Massage(massage_text="检测到 HydroOJ 账号未登录，是否登录并继续同步？",
                            accept=lambda: (s.login(site="HydroOJ"),
                                            s.sync("HydroOJ")))
        if self.uojCheckBox.isChecked():
            if s.check_login("UOJ"):
                s.sync("UOJ")
            else:
                if settings["uojUsername"] == '':
                    Massage(massage_text="检测到 UOJ 账号未登录且未配置，请前往配置后重新操作")
                else:
                    Massage(massage_text="检测到 UOJ 账号未登录，是否登录并继续同步？",
                            accept=lambda: (s.login(site="UOJ"),
                                            s.sync("UOJ")))
        if self.cfCheckBox.isChecked():
            if s.check_login("Codeforces"):
                s.sync("Codeforces")
            else:
                if settings["codeforcesUsername"] == '':
                    Massage(massage_text="检测到 Codeforces 账号未登录且未配置，请前往配置后重新操作")
                else:
                    Massage(massage_text="检测到 Codeforces 账号未登录，是否登录并继续同步？",
                            accept=lambda: (s.login(site="Codeforces"),
                                            s.sync("Codeforces")))

        load_list()


if __name__ == '__main__':
    slash = '/'

    if platform.system() == 'Windows':
        slash = '\\'

    region = requests.get(f"https://ipapi.co/{requests.get('https://ipapi.co/ip/').text}/country_code").text
    LOGGER.log(10, f"Region: {region}")
    if region == 'CN':
        result = json.loads(requests.get("https://gitee.com/api/v5/repos/lixuannan/CodeLib-Local/releases/latest").text)
        tag = result["tag_name"]
        url = result["assets"]
    else:
        result = json.loads(requests.get("https://api.github.com/repos/lixuannan/CodeLib-Local/releases/latest").text)
        tag = result["tag_name"]
        url = result["assets"]

    update_url = ""
    if tag != VERSION:
        if platform.system() == 'Windows':
            for i in url:
                if "name" in i and i["name"] == f"CodeLib-Local-Setup-{tag}.exe":
                    update_url = i["browser_download_url"]
                    break

    db_location = os.path.join(DATA_ROOT, 'CodeLib-Local', 'data.db')
    db_template_location = ""
    db_template_location_l = os.path.join(os.path.abspath(sys.argv[0]))

    if '/' in db_template_location_l:
        db_template_location_l = db_template_location_l.split('/')
    if '\\' in db_template_location_l:
        db_template_location_l = db_template_location_l.split('\\')

    for i in range(len(db_template_location_l) - 1):
        db_template_location += db_template_location_l[i] + slash

    if not os.path.isdir(os.path.join(DATA_ROOT, "CodeLib-Local")):
        os.mkdir(os.path.join(DATA_ROOT, "CodeLib-Local"))

    if not os.path.isfile(db_location):
        shutil.copy(os.path.join(db_template_location, "data.db.template"), db_location)

    settings = {}
    default_site = {}

    LOGGER.log(10, f"DB location: {db_location}")

    db = sqlite3.connect(db_location)
    cursor = db.execute("SELECT * FROM settings")
    for i in cursor:
        value = None
        for j in i:
            if j is not None:
                value = j
        settings[i[0]] = value
    show_settings()

    cursor = db.execute("SELECT * FROM default_sync")
    for i in cursor:
        default_site[i[0]] = i[1]
    LOGGER.log(10, f"Default site: {default_site}")

    s = syncer.Syncer(settings, LOGGER)

    if settings["loginWhenStartup"]:
        if settings["oiclassUsername"] != '':
            s.login("Oiclass")
        if settings["hydroojUsername"] != '':
            s.login("HydroOJ")
        if settings["uojUsername"] != '':
            s.login("UOJ")
        if settings["codeforcesUsername"] != '':
            s.login("Codeforces")

    app = QApplication()
    widget = QWidget()
    main_widget = main_window.Ui_mainWindow()
    main_widget.setupUi(widget)
    main_widget.setting.clicked.connect(lambda: Setting())
    main_widget.sync.clicked.connect(lambda: ChooseOJ())
    main_widget.refresh.clicked.connect(load_list)
    main_widget.keyword.returnPressed.connect(search)
    main_widget.problems.doubleClicked.connect(lambda: ShowProblem(main_widget.problems.selectedItems()[0].text()))

    log_widget = QWidget()
    log_window = log.Ui_log()
    log_window.setupUi(log_widget)
    log_window.refresh.clicked.connect(lambda: log_window.logBrowser.setText(LOGGER.allLogs))

    show_log_shortcut = QShortcut(QKeySequence("Ctrl+l"), widget)
    show_log_shortcut.activated.connect(lambda: log_widget.show())

    refresh_shortcut_main_1 = QShortcut(QKeySequence("f5"), widget)
    refresh_shortcut_main_1.activated.connect(load_list)

    refresh_shortcut_log_1 = QShortcut(QKeySequence("f5"), log_widget)
    refresh_shortcut_log_1.activated.connect(lambda: log_window.logBrowser.setText(LOGGER.allLogs))

    refresh_shortcut_main_2 = QShortcut(QKeySequence("Ctrl+r"), widget)
    refresh_shortcut_main_2.activated.connect(load_list)

    refresh_shortcut_log_2 = QShortcut(QKeySequence("Ctrl+r"), log_widget)
    refresh_shortcut_log_2.activated.connect(lambda: log_window.logBrowser.setText(LOGGER.allLogs))

    setting_shortcut = QShortcut(QKeySequence("Ctrl+,"), widget)
    setting_shortcut.activated.connect(lambda: Setting())

    sync_shortcut = QShortcut(QKeySequence("Ctrl+s"), widget)
    sync_shortcut.activated.connect(lambda: ChooseOJ())

    load_list()

    if update_url != "":
        Update(update_url)
        os.system(f"\"{os.path.join(DATA_ROOT, 'CodeLib-Local', update_url.split('/')[-1])}\"")
        sys.exit(0)

    widget.show()
    sys.exit(app.exec())
