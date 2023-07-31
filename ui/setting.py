# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QScrollArea, QSizePolicy,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_settingPage(object):
    def setupUi(self, settingPage):
        if not settingPage.objectName():
            settingPage.setObjectName(u"settingPage")
        settingPage.resize(416, 355)
        self.verticalLayout = QVBoxLayout(settingPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(settingPage)
        self.tabWidget.setObjectName(u"tabWidget")
        self.generic = QWidget()
        self.generic.setObjectName(u"generic")
        self.verticalLayout_2 = QVBoxLayout(self.generic)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.generic_tab = QScrollArea(self.generic)
        self.generic_tab.setObjectName(u"generic_tab")
        self.generic_tab.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 372, 259))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.loginWhenStartup = QWidget(self.scrollAreaWidgetContents_2)
        self.loginWhenStartup.setObjectName(u"loginWhenStartup")
        self.horizontalLayout = QHBoxLayout(self.loginWhenStartup)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.loginWhenStartL = QLabel(self.loginWhenStartup)
        self.loginWhenStartL.setObjectName(u"loginWhenStartL")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginWhenStartL.sizePolicy().hasHeightForWidth())
        self.loginWhenStartL.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(11)
        self.loginWhenStartL.setFont(font)

        self.horizontalLayout.addWidget(self.loginWhenStartL)

        self.checkBox = QCheckBox(self.loginWhenStartup)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.checkBox)


        self.verticalLayout_4.addWidget(self.loginWhenStartup)

        self.Language = QWidget(self.scrollAreaWidgetContents_2)
        self.Language.setObjectName(u"Language")
        self.horizontalLayout_5 = QHBoxLayout(self.Language)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.LanguageL = QLabel(self.Language)
        self.LanguageL.setObjectName(u"LanguageL")
        sizePolicy.setHeightForWidth(self.LanguageL.sizePolicy().hasHeightForWidth())
        self.LanguageL.setSizePolicy(sizePolicy)
        self.LanguageL.setFont(font)

        self.horizontalLayout_5.addWidget(self.LanguageL)

        self.LanguageComboBox = QComboBox(self.Language)
        self.LanguageComboBox.addItem("")
        self.LanguageComboBox.setObjectName(u"LanguageComboBox")
        sizePolicy.setHeightForWidth(self.LanguageComboBox.sizePolicy().hasHeightForWidth())
        self.LanguageComboBox.setSizePolicy(sizePolicy)
        self.LanguageComboBox.setFont(font)

        self.horizontalLayout_5.addWidget(self.LanguageComboBox)


        self.verticalLayout_4.addWidget(self.Language)

        self.generic_tab.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_2.addWidget(self.generic_tab)

        self.tabWidget.addTab(self.generic, "")
        self.account = QWidget()
        self.account.setObjectName(u"account")
        self.verticalLayout_3 = QVBoxLayout(self.account)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.account_tab = QScrollArea(self.account)
        self.account_tab.setObjectName(u"account_tab")
        self.account_tab.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 355, 372))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.oiclassAccount = QWidget(self.scrollAreaWidgetContents)
        self.oiclassAccount.setObjectName(u"oiclassAccount")
        self.horizontalLayout_3 = QHBoxLayout(self.oiclassAccount)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.oicAccL = QLabel(self.oiclassAccount)
        self.oicAccL.setObjectName(u"oicAccL")
        self.oicAccL.setFont(font)

        self.horizontalLayout_3.addWidget(self.oicAccL)

        self.oicAccInput = QLineEdit(self.oiclassAccount)
        self.oicAccInput.setObjectName(u"oicAccInput")
        font1 = QFont()
        font1.setPointSize(10)
        self.oicAccInput.setFont(font1)

        self.horizontalLayout_3.addWidget(self.oicAccInput)


        self.verticalLayout_5.addWidget(self.oiclassAccount)

        self.oiclassPassword = QWidget(self.scrollAreaWidgetContents)
        self.oiclassPassword.setObjectName(u"oiclassPassword")
        self.horizontalLayout_2 = QHBoxLayout(self.oiclassPassword)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.oicPwdL = QLabel(self.oiclassPassword)
        self.oicPwdL.setObjectName(u"oicPwdL")
        self.oicPwdL.setFont(font)

        self.horizontalLayout_2.addWidget(self.oicPwdL)

        self.oicPwdInput = QLineEdit(self.oiclassPassword)
        self.oicPwdInput.setObjectName(u"oicPwdInput")
        self.oicPwdInput.setFont(font1)

        self.horizontalLayout_2.addWidget(self.oicPwdInput)


        self.verticalLayout_5.addWidget(self.oiclassPassword)

        self.hydroojAccount = QWidget(self.scrollAreaWidgetContents)
        self.hydroojAccount.setObjectName(u"hydroojAccount")
        self.horizontalLayout_4 = QHBoxLayout(self.hydroojAccount)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.hydroAccL = QLabel(self.hydroojAccount)
        self.hydroAccL.setObjectName(u"hydroAccL")
        self.hydroAccL.setFont(font)

        self.horizontalLayout_4.addWidget(self.hydroAccL)

        self.hydroAccInput = QLineEdit(self.hydroojAccount)
        self.hydroAccInput.setObjectName(u"hydroAccInput")
        self.hydroAccInput.setFont(font1)

        self.horizontalLayout_4.addWidget(self.hydroAccInput)


        self.verticalLayout_5.addWidget(self.hydroojAccount)

        self.hydroojPassword = QWidget(self.scrollAreaWidgetContents)
        self.hydroojPassword.setObjectName(u"hydroojPassword")
        self.horizontalLayout_6 = QHBoxLayout(self.hydroojPassword)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.hydroPwdL = QLabel(self.hydroojPassword)
        self.hydroPwdL.setObjectName(u"hydroPwdL")
        self.hydroPwdL.setFont(font)

        self.horizontalLayout_6.addWidget(self.hydroPwdL)

        self.hydroPwdInput = QLineEdit(self.hydroojPassword)
        self.hydroPwdInput.setObjectName(u"hydroPwdInput")
        self.hydroPwdInput.setFont(font1)

        self.horizontalLayout_6.addWidget(self.hydroPwdInput)


        self.verticalLayout_5.addWidget(self.hydroojPassword)

        self.uojAccount = QWidget(self.scrollAreaWidgetContents)
        self.uojAccount.setObjectName(u"uojAccount")
        self.horizontalLayout_7 = QHBoxLayout(self.uojAccount)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.oujAccL = QLabel(self.uojAccount)
        self.oujAccL.setObjectName(u"oujAccL")
        self.oujAccL.setFont(font)

        self.horizontalLayout_7.addWidget(self.oujAccL)

        self.uojAccInput = QLineEdit(self.uojAccount)
        self.uojAccInput.setObjectName(u"uojAccInput")
        self.uojAccInput.setFont(font1)

        self.horizontalLayout_7.addWidget(self.uojAccInput)


        self.verticalLayout_5.addWidget(self.uojAccount)

        self.uojPassword = QWidget(self.scrollAreaWidgetContents)
        self.uojPassword.setObjectName(u"uojPassword")
        self.horizontalLayout_8 = QHBoxLayout(self.uojPassword)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.uojPwdL = QLabel(self.uojPassword)
        self.uojPwdL.setObjectName(u"uojPwdL")
        self.uojPwdL.setFont(font)

        self.horizontalLayout_8.addWidget(self.uojPwdL)

        self.uojPwdInput = QLineEdit(self.uojPassword)
        self.uojPwdInput.setObjectName(u"uojPwdInput")
        self.uojPwdInput.setFont(font1)

        self.horizontalLayout_8.addWidget(self.uojPwdInput)


        self.verticalLayout_5.addWidget(self.uojPassword)

        self.codeforcesAccount = QWidget(self.scrollAreaWidgetContents)
        self.codeforcesAccount.setObjectName(u"codeforcesAccount")
        self.horizontalLayout_9 = QHBoxLayout(self.codeforcesAccount)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.cfAccL = QLabel(self.codeforcesAccount)
        self.cfAccL.setObjectName(u"cfAccL")
        self.cfAccL.setFont(font)

        self.horizontalLayout_9.addWidget(self.cfAccL)

        self.cfAccInput = QLineEdit(self.codeforcesAccount)
        self.cfAccInput.setObjectName(u"cfAccInput")
        self.cfAccInput.setFont(font1)

        self.horizontalLayout_9.addWidget(self.cfAccInput)


        self.verticalLayout_5.addWidget(self.codeforcesAccount)

        self.codeforcesPassword = QWidget(self.scrollAreaWidgetContents)
        self.codeforcesPassword.setObjectName(u"codeforcesPassword")
        self.horizontalLayout_10 = QHBoxLayout(self.codeforcesPassword)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.cfPwdL = QLabel(self.codeforcesPassword)
        self.cfPwdL.setObjectName(u"cfPwdL")
        self.cfPwdL.setFont(font)

        self.horizontalLayout_10.addWidget(self.cfPwdL)

        self.cfPwdInput = QLineEdit(self.codeforcesPassword)
        self.cfPwdInput.setObjectName(u"cfPwdInput")
        self.cfPwdInput.setFont(font1)

        self.horizontalLayout_10.addWidget(self.cfPwdInput)


        self.verticalLayout_5.addWidget(self.codeforcesPassword)

        self.account_tab.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.account_tab)

        self.tabWidget.addTab(self.account, "")
        self.sync = QWidget()
        self.sync.setObjectName(u"sync")
        self.verticalLayout_6 = QVBoxLayout(self.sync)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.sync_tab = QScrollArea(self.sync)
        self.sync_tab.setObjectName(u"sync_tab")
        self.sync_tab.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 372, 259))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label = QLabel(self.scrollAreaWidgetContents_3)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(12)
        self.label.setFont(font2)

        self.verticalLayout_7.addWidget(self.label)

        self.widget = QWidget(self.scrollAreaWidgetContents_3)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.cfCheckBox = QCheckBox(self.widget)
        self.cfCheckBox.setObjectName(u"cfCheckBox")
        sizePolicy.setHeightForWidth(self.cfCheckBox.sizePolicy().hasHeightForWidth())
        self.cfCheckBox.setSizePolicy(sizePolicy)
        self.cfCheckBox.setFont(font1)

        self.gridLayout.addWidget(self.cfCheckBox, 2, 0, 1, 1)

        self.hydroCheckBox = QCheckBox(self.widget)
        self.hydroCheckBox.setObjectName(u"hydroCheckBox")
        sizePolicy.setHeightForWidth(self.hydroCheckBox.sizePolicy().hasHeightForWidth())
        self.hydroCheckBox.setSizePolicy(sizePolicy)
        self.hydroCheckBox.setFont(font1)

        self.gridLayout.addWidget(self.hydroCheckBox, 1, 0, 1, 1)

        self.oicCheckBox = QCheckBox(self.widget)
        self.oicCheckBox.setObjectName(u"oicCheckBox")
        sizePolicy.setHeightForWidth(self.oicCheckBox.sizePolicy().hasHeightForWidth())
        self.oicCheckBox.setSizePolicy(sizePolicy)
        self.oicCheckBox.setFont(font1)

        self.gridLayout.addWidget(self.oicCheckBox, 1, 1, 1, 1)

        self.uojCheckBox = QCheckBox(self.widget)
        self.uojCheckBox.setObjectName(u"uojCheckBox")
        sizePolicy.setHeightForWidth(self.uojCheckBox.sizePolicy().hasHeightForWidth())
        self.uojCheckBox.setSizePolicy(sizePolicy)
        self.uojCheckBox.setFont(font1)

        self.gridLayout.addWidget(self.uojCheckBox, 1, 2, 1, 1)


        self.verticalLayout_7.addWidget(self.widget)

        self.sync_tab.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_6.addWidget(self.sync_tab)

        self.tabWidget.addTab(self.sync, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.dialogButtonBox = QDialogButtonBox(settingPage)
        self.dialogButtonBox.setObjectName(u"dialogButtonBox")
        self.dialogButtonBox.setOrientation(Qt.Horizontal)
        self.dialogButtonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.dialogButtonBox)


        self.retranslateUi(settingPage)
        self.dialogButtonBox.rejected.connect(settingPage.reject)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(settingPage)
    # setupUi

    def retranslateUi(self, settingPage):
        settingPage.setWindowTitle(QCoreApplication.translate("settingPage", u"\u8bbe\u7f6e", None))
        self.loginWhenStartL.setText(QCoreApplication.translate("settingPage", u"\u5f00\u542f\u5e94\u7528\u65f6\u767b\u5f55\uff1a", None))
        self.checkBox.setText("")
        self.LanguageL.setText(QCoreApplication.translate("settingPage", u"\u8bed\u8a00\uff1a", None))
        self.LanguageComboBox.setItemText(0, QCoreApplication.translate("settingPage", u"Simplified Chinese", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.generic), QCoreApplication.translate("settingPage", u"\u901a\u7528", None))
        self.oicAccL.setText(QCoreApplication.translate("settingPage", u"Oiclass \u8d26\u53f7\uff1a", None))
        self.oicPwdL.setText(QCoreApplication.translate("settingPage", u"Oiclass \u5bc6\u7801\uff1a", None))
        self.hydroAccL.setText(QCoreApplication.translate("settingPage", u"HydroOJ \u8d26\u53f7\uff1a", None))
        self.hydroPwdL.setText(QCoreApplication.translate("settingPage", u"HydroOJ \u5bc6\u7801\uff1a", None))
        self.oujAccL.setText(QCoreApplication.translate("settingPage", u"UOJ \u8d26\u53f7\uff1a", None))
        self.uojPwdL.setText(QCoreApplication.translate("settingPage", u"UOJ \u5bc6\u7801\uff1a", None))
        self.cfAccL.setText(QCoreApplication.translate("settingPage", u"Codeforces \u8d26\u53f7\uff1a", None))
        self.cfPwdL.setText(QCoreApplication.translate("settingPage", u"Codeforces \u5bc6\u7801\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.account), QCoreApplication.translate("settingPage", u"\u8d26\u53f7", None))
        self.label.setText(QCoreApplication.translate("settingPage", u"\u9ed8\u8ba4\u540c\u6b65\u7684 OJ\uff1a", None))
        self.cfCheckBox.setText(QCoreApplication.translate("settingPage", u"Codeforces", None))
        self.hydroCheckBox.setText(QCoreApplication.translate("settingPage", u"HydroOJ", None))
        self.oicCheckBox.setText(QCoreApplication.translate("settingPage", u"Oiclass", None))
        self.uojCheckBox.setText(QCoreApplication.translate("settingPage", u"UOJ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sync), QCoreApplication.translate("settingPage", u"\u540c\u6b65", None))
    # retranslateUi

