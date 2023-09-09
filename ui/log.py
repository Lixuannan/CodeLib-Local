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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QSizePolicy, QTextBrowser, QVBoxLayout, QWidget)

class Ui_Log(object):
    def setupUi(self, Log):
        if not Log.objectName():
            Log.setObjectName(u"Log")
        Log.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Log)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.logBrowser = QTextBrowser(Log)
        self.logBrowser.setObjectName(u"logBrowser")

        self.verticalLayout.addWidget(self.logBrowser)

        self.buttonBox = QDialogButtonBox(Log)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Log)
        self.buttonBox.accepted.connect(Log.accept)
        self.buttonBox.rejected.connect(Log.reject)

        QMetaObject.connectSlotsByName(Log)
    # setupUi

    def retranslateUi(self, Log):
        Log.setWindowTitle(QCoreApplication.translate("Log", u"\u65e5\u5fd7", None))
    # retranslateUi

