# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sync_page.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QProgressBar, QSizePolicy,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_sync_page(object):
    def setupUi(self, sync_page):
        if not sync_page.objectName():
            sync_page.setObjectName(u"sync_page")
        sync_page.resize(531, 355)
        self.verticalLayout = QVBoxLayout(sync_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(sync_page)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.progressBar = QProgressBar(sync_page)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(1)

        self.horizontalLayout.addWidget(self.progressBar)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.textBrowser = QTextBrowser(sync_page)
        self.textBrowser.setObjectName(u"textBrowser")
        font1 = QFont()
        font1.setPointSize(14)
        self.textBrowser.setFont(font1)

        self.verticalLayout_2.addWidget(self.textBrowser)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.buttonBox = QDialogButtonBox(sync_page)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setEnabled(False)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(sync_page)

        QMetaObject.connectSlotsByName(sync_page)
    # setupUi

    def retranslateUi(self, sync_page):
        sync_page.setWindowTitle(QCoreApplication.translate("sync_page", u"Syncing - \u540c\u6b65\u4e2d", None))
        self.label.setText(QCoreApplication.translate("sync_page", u"Progress \u8fdb\u5ea6 : ", None))
    # retranslateUi

