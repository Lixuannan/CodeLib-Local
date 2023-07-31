# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QSizePolicy, QToolButton,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(575, 601)
        self.verticalLayout = QVBoxLayout(mainWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(mainWindow)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.keyword = QLineEdit(mainWindow)
        self.keyword.setObjectName(u"keyword")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.keyword.sizePolicy().hasHeightForWidth())
        self.keyword.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(11)
        self.keyword.setFont(font1)

        self.horizontalLayout.addWidget(self.keyword)

        self.refresh = QToolButton(mainWindow)
        self.refresh.setObjectName(u"refresh")
        sizePolicy.setHeightForWidth(self.refresh.sizePolicy().hasHeightForWidth())
        self.refresh.setSizePolicy(sizePolicy)
        self.refresh.setStyleSheet(u"QToolButton#refresh {\n"
"    border-image: url(:/icon/\u5237\u65b0.png)\n"
"}")

        self.horizontalLayout.addWidget(self.refresh)

        self.sync = QToolButton(mainWindow)
        self.sync.setObjectName(u"sync")
        sizePolicy.setHeightForWidth(self.sync.sizePolicy().hasHeightForWidth())
        self.sync.setSizePolicy(sizePolicy)
        self.sync.setFont(font)
        self.sync.setStyleSheet(u"QToolButton#sync {\n"
"    border-image: url(:/icon/\u4e91\u540c\u6b65.png)\n"
"}")

        self.horizontalLayout.addWidget(self.sync)

        self.setting = QToolButton(mainWindow)
        self.setting.setObjectName(u"setting")
        sizePolicy.setHeightForWidth(self.setting.sizePolicy().hasHeightForWidth())
        self.setting.setSizePolicy(sizePolicy)
        self.setting.setFont(font)
        self.setting.setStyleSheet(u"QToolButton#setting {\n"
"    border-image: url(:/icon/\u8bbe\u7f6e.png)\n"
"}")

        self.horizontalLayout.addWidget(self.setting)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.problems = QListWidget(mainWindow)
        self.problems.setObjectName(u"problems")
        font2 = QFont()
        font2.setPointSize(10)
        self.problems.setFont(font2)

        self.verticalLayout.addWidget(self.problems)


        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"CodeLib-Local", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"\u641c\u7d22\uff1a", None))
        self.refresh.setText("")
        self.sync.setText("")
        self.setting.setText("")
    # retranslateUi

