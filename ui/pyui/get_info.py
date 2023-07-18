# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'get_info.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Get_Info(object):
    def setupUi(self, Get_Info):
        if not Get_Info.objectName():
            Get_Info.setObjectName(u"Get_Info")
        Get_Info.resize(429, 127)
        self.verticalLayout = QVBoxLayout(Get_Info)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Get_Info)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.info_line = QLineEdit(Get_Info)
        self.info_line.setObjectName(u"info_line")

        self.horizontalLayout.addWidget(self.info_line)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(Get_Info)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Get_Info)

        QMetaObject.connectSlotsByName(Get_Info)
    # setupUi

    def retranslateUi(self, Get_Info):
        Get_Info.setWindowTitle(QCoreApplication.translate("Get_Info", u"Lost Info - \u7f3a\u5c11\u4fe1\u606f", None))
        self.label.setText(QCoreApplication.translate("Get_Info", u"Info", None))
    # retranslateUi

