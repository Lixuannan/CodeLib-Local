# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'massage.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
    QSizePolicy, QTextBrowser, QVBoxLayout, QWidget)
import resources_rc

class Ui_massagePage(object):
    def setupUi(self, massagePage):
        if not massagePage.objectName():
            massagePage.setObjectName(u"massagePage")
        massagePage.resize(435, 210)
        icon = QIcon()
        icon.addFile(u":/icon/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        massagePage.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(massagePage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.massageBrowser = QTextBrowser(massagePage)
        self.massageBrowser.setObjectName(u"massageBrowser")
        font = QFont()
        font.setPointSize(10)
        self.massageBrowser.setFont(font)

        self.verticalLayout.addWidget(self.massageBrowser)

        self.massageButtonBox = QDialogButtonBox(massagePage)
        self.massageButtonBox.setObjectName(u"massageButtonBox")
        self.massageButtonBox.setOrientation(Qt.Horizontal)
        self.massageButtonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.massageButtonBox)


        self.retranslateUi(massagePage)

        QMetaObject.connectSlotsByName(massagePage)
    # setupUi

    def retranslateUi(self, massagePage):
        massagePage.setWindowTitle(QCoreApplication.translate("massagePage", u"\u6d88\u606f", None))
        self.massageBrowser.setHtml(QCoreApplication.translate("massagePage", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>", None))
    # retranslateUi

