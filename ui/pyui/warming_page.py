# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'warming_page.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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

class Ui_warming_page(object):
    def setupUi(self, warming_page):
        if not warming_page.objectName():
            warming_page.setObjectName(u"warming_page")
        warming_page.resize(427, 214)
        self.verticalLayout = QVBoxLayout(warming_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.warming = QTextBrowser(warming_page)
        self.warming.setObjectName(u"warming")

        self.verticalLayout.addWidget(self.warming)

        self.buttonBox = QDialogButtonBox(warming_page)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(warming_page)
        self.buttonBox.accepted.connect(warming_page.accept)
        self.buttonBox.rejected.connect(warming_page.reject)

        QMetaObject.connectSlotsByName(warming_page)
    # setupUi

    def retranslateUi(self, warming_page):
        warming_page.setWindowTitle(QCoreApplication.translate("warming_page", u"Warming - \u8b66\u544a", None))
    # retranslateUi

