import sys
import os
import sqlite3

from PySide6.QtWidgets import QApplication, QWidget, QDialog

import syncer
from ui import main_window, setting, chooseOJ, massage


def load_list():
    main_widget.problems.clear()
    for i in db.execute("SELECT * FROM problems;"):
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


def show_settings():
    for i in settings:
        print(f"{i}: {settings[i]}")


class Setting(setting.Ui_settingPage, QDialog):
    def __init__(self):
        print(settings)
        super(Setting, self).__init__()
        self.setupUi(self)
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
        print(settings)
        p = sys.executable
        os.execl(p, p, *sys.argv)
        sys.exit()

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
            print("self.accepted Connected to customize function")
        else:
            self.massageButtonBox.accepted.connect(self.accept)
            print("self.accepted Connected to default self.accept")
        if reject is not None:
            self.massageButtonBox.rejected.connect(lambda: (self.close(), reject()))
            print("self.rejected Connected to customize function")
        else:
            self.massageButtonBox.rejected.connect(self.reject)
            print("self.rejected Connected to default self.reject")

        self.massageBrowser.setText(massage_text)
        self.exec()


class ChooseOJ(chooseOJ.Ui_chooseOJ, QDialog):
    def __init__(self):
        print(default_site)
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
    settings = {}
    default_site = {}
    db = sqlite3.connect("data.db")
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
    print(f"Default site: {default_site}")

    s = syncer.Syncer(settings)

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

    load_list()

    widget.show()
    sys.exit(app.exec())
