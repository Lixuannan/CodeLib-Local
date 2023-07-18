# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QSizePolicy, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        if not MainWidget.objectName():
            MainWidget.setObjectName(u"MainWidget")
        MainWidget.resize(643, 564)
        self.verticalLayout = QVBoxLayout(MainWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.search = QLabel(MainWidget)
        self.search.setObjectName(u"search")
        font = QFont()
        font.setPointSize(16)
        self.search.setFont(font)

        self.horizontalLayout.addWidget(self.search)

        self.keyword = QLineEdit(MainWidget)
        self.keyword.setObjectName(u"keyword")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.keyword.sizePolicy().hasHeightForWidth())
        self.keyword.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(14)
        self.keyword.setFont(font1)

        self.horizontalLayout.addWidget(self.keyword)

        self.sync = QToolButton(MainWidget)
        self.sync.setObjectName(u"sync")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sync.sizePolicy().hasHeightForWidth())
        self.sync.setSizePolicy(sizePolicy1)
        self.sync.setFont(font1)

        self.horizontalLayout.addWidget(self.sync)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.problems = QListWidget(MainWidget)
        self.problems.setObjectName(u"problems")

        self.verticalLayout.addWidget(self.problems)


        self.retranslateUi(MainWidget)

        QMetaObject.connectSlotsByName(MainWidget)
    # setupUi

    def retranslateUi(self, MainWidget):
        MainWidget.setWindowTitle(QCoreApplication.translate("MainWidget", u"CodeLib-Local", None))
        self.search.setText(QCoreApplication.translate("MainWidget", u"\u641c\u7d22:", None))
        self.sync.setText(QCoreApplication.translate("MainWidget", u"\u540c\u6b65", None))
    # retranslateUi

