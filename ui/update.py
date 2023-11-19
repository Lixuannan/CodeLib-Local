# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'update.ui'
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
    QHBoxLayout, QLabel, QProgressBar, QSizePolicy,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_UpdateDialog(object):
    def setupUi(self, UpdateDialog):
        if not UpdateDialog.objectName():
            UpdateDialog.setObjectName(u"UpdateDialog")
        UpdateDialog.resize(406, 117)
        icon = QIcon()
        icon.addFile(u":/icon/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        UpdateDialog.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(UpdateDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.question = QLabel(UpdateDialog)
        self.question.setObjectName(u"question")
        font = QFont()
        font.setPointSize(11)
        self.question.setFont(font)

        self.verticalLayout.addWidget(self.question)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.progressLabel = QLabel(UpdateDialog)
        self.progressLabel.setObjectName(u"progressLabel")
        self.progressLabel.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressLabel.sizePolicy().hasHeightForWidth())
        self.progressLabel.setSizePolicy(sizePolicy)
        self.progressLabel.setFont(font)

        self.horizontalLayout.addWidget(self.progressLabel)

        self.downloadProgress = QProgressBar(UpdateDialog)
        self.downloadProgress.setObjectName(u"downloadProgress")
        self.downloadProgress.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.downloadProgress.sizePolicy().hasHeightForWidth())
        self.downloadProgress.setSizePolicy(sizePolicy1)
        self.downloadProgress.setMinimum(0)
        self.downloadProgress.setValue(0)
        self.downloadProgress.setTextVisible(True)
        self.downloadProgress.setInvertedAppearance(False)

        self.horizontalLayout.addWidget(self.downloadProgress)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.ifUpdate = QDialogButtonBox(UpdateDialog)
        self.ifUpdate.setObjectName(u"ifUpdate")
        self.ifUpdate.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.ifUpdate)


        self.retranslateUi(UpdateDialog)

        QMetaObject.connectSlotsByName(UpdateDialog)
    # setupUi

    def retranslateUi(self, UpdateDialog):
        UpdateDialog.setWindowTitle(QCoreApplication.translate("UpdateDialog", u"\u7248\u672c\u66f4\u65b0", None))
        self.question.setText(QCoreApplication.translate("UpdateDialog", u"\u68c0\u6d4b\u5230\u65b0\u7248\u672c\uff0c\u662f\u5426\u66f4\u65b0\uff1f", None))
        self.progressLabel.setText(QCoreApplication.translate("UpdateDialog", u"\u4e0b\u8f7d\u8fdb\u5ea6\uff1a", None))
    # retranslateUi

