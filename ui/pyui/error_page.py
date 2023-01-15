# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'error_page.ui'
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

class Ui_error_page(object):
    def setupUi(self, error_page):
        if not error_page.objectName():
            error_page.setObjectName(u"error_page")
        error_page.resize(427, 214)
        self.verticalLayout = QVBoxLayout(error_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.error_browser = QTextBrowser(error_page)
        self.error_browser.setObjectName(u"error_browser")

        self.verticalLayout.addWidget(self.error_browser)

        self.buttonBox = QDialogButtonBox(error_page)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(error_page)
        self.buttonBox.accepted.connect(error_page.accept)
        self.buttonBox.rejected.connect(error_page.reject)

        QMetaObject.connectSlotsByName(error_page)
    # setupUi

    def retranslateUi(self, error_page):
        error_page.setWindowTitle(QCoreApplication.translate("error_page", u"Error - \u9519\u8bef", None))
    # retranslateUi

