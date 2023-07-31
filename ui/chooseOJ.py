# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chooseOJ.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_chooseOJ(object):
    def setupUi(self, chooseOJ):
        if not chooseOJ.objectName():
            chooseOJ.setObjectName(u"chooseOJ")
        chooseOJ.resize(385, 195)
        icon = QIcon()
        icon.addFile(u":/icon/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        chooseOJ.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(chooseOJ)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(chooseOJ)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.checkBoxWidget = QWidget()
        self.checkBoxWidget.setObjectName(u"checkBoxWidget")
        self.checkBoxWidget.setGeometry(QRect(0, 0, 365, 144))
        self.verticalLayout_2 = QVBoxLayout(self.checkBoxWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.oiclassCheckBox = QCheckBox(self.checkBoxWidget)
        self.oiclassCheckBox.setObjectName(u"oiclassCheckBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oiclassCheckBox.sizePolicy().hasHeightForWidth())
        self.oiclassCheckBox.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        self.oiclassCheckBox.setFont(font)

        self.verticalLayout_2.addWidget(self.oiclassCheckBox)

        self.hydroOJCheckBox = QCheckBox(self.checkBoxWidget)
        self.hydroOJCheckBox.setObjectName(u"hydroOJCheckBox")
        sizePolicy.setHeightForWidth(self.hydroOJCheckBox.sizePolicy().hasHeightForWidth())
        self.hydroOJCheckBox.setSizePolicy(sizePolicy)
        self.hydroOJCheckBox.setFont(font)

        self.verticalLayout_2.addWidget(self.hydroOJCheckBox)

        self.uojCheckBox = QCheckBox(self.checkBoxWidget)
        self.uojCheckBox.setObjectName(u"uojCheckBox")
        sizePolicy.setHeightForWidth(self.uojCheckBox.sizePolicy().hasHeightForWidth())
        self.uojCheckBox.setSizePolicy(sizePolicy)
        self.uojCheckBox.setFont(font)

        self.verticalLayout_2.addWidget(self.uojCheckBox)

        self.cfCheckBox = QCheckBox(self.checkBoxWidget)
        self.cfCheckBox.setObjectName(u"cfCheckBox")
        sizePolicy.setHeightForWidth(self.cfCheckBox.sizePolicy().hasHeightForWidth())
        self.cfCheckBox.setSizePolicy(sizePolicy)
        self.cfCheckBox.setFont(font)

        self.verticalLayout_2.addWidget(self.cfCheckBox)

        self.scrollArea.setWidget(self.checkBoxWidget)

        self.verticalLayout.addWidget(self.scrollArea)

        self.buttonBox = QDialogButtonBox(chooseOJ)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(chooseOJ)
        self.buttonBox.rejected.connect(chooseOJ.reject)

        QMetaObject.connectSlotsByName(chooseOJ)
    # setupUi

    def retranslateUi(self, chooseOJ):
        chooseOJ.setWindowTitle(QCoreApplication.translate("chooseOJ", u"\u9009\u62e9OJ", None))
        self.oiclassCheckBox.setText(QCoreApplication.translate("chooseOJ", u"Oiclass", None))
        self.hydroOJCheckBox.setText(QCoreApplication.translate("chooseOJ", u"HydroOJ", None))
        self.uojCheckBox.setText(QCoreApplication.translate("chooseOJ", u"UOJ", None))
        self.cfCheckBox.setText(QCoreApplication.translate("chooseOJ", u"Codeforces", None))
    # retranslateUi

