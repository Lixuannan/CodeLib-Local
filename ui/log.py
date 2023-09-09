# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'log.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QHBoxLayout,
    QSizePolicy, QTextBrowser, QToolButton, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_log(object):
    def setupUi(self, log):
        if not log.objectName():
            log.setObjectName(u"log")
        log.resize(611, 371)
        icon = QIcon()
        icon.addFile(u":/icon/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        log.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(log)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.logBrowser = QTextBrowser(log)
        self.logBrowser.setObjectName(u"logBrowser")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logBrowser.sizePolicy().hasHeightForWidth())
        self.logBrowser.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.logBrowser)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.refresh = QToolButton(log)
        self.refresh.setObjectName(u"refresh")
        icon1 = QIcon()
        icon1.addFile(u":/icon/\u5237\u65b0.png", QSize(), QIcon.Normal, QIcon.Off)
        self.refresh.setIcon(icon1)

        self.horizontalLayout.addWidget(self.refresh)

        self.buttonBox = QDialogButtonBox(log)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(log)
        self.buttonBox.clicked.connect(log.hide)

        QMetaObject.connectSlotsByName(log)
    # setupUi

    def retranslateUi(self, log):
        log.setWindowTitle(QCoreApplication.translate("log", u"\u65e5\u5fd7", None))
        self.refresh.setText(QCoreApplication.translate("log", u"...", None))
    # retranslateUi

