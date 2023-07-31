# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'show_problem.ui'
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
    QHBoxLayout, QLabel, QSizePolicy, QTextBrowser,
    QToolButton, QVBoxLayout, QWidget)
import resources_rc

class Ui_show_problem(object):
    def setupUi(self, show_problem):
        if not show_problem.objectName():
            show_problem.setObjectName(u"show_problem")
        show_problem.resize(505, 440)
        self.verticalLayout = QVBoxLayout(show_problem)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(show_problem)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy1)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.widget_6)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)

        self.horizontalLayout_4.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.widget_6)

        self.pid = QLabel(self.widget_2)
        self.pid.setObjectName(u"pid")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pid.sizePolicy().hasHeightForWidth())
        self.pid.setSizePolicy(sizePolicy2)
        self.pid.setFont(font)

        self.horizontalLayout_2.addWidget(self.pid)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_7 = QWidget(self.widget_4)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy1.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy1)
        self.horizontalLayout_5 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.widget_7)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_3)


        self.horizontalLayout_3.addWidget(self.widget_7)

        self.site = QLabel(self.widget_4)
        self.site.setObjectName(u"site")
        sizePolicy2.setHeightForWidth(self.site.sizePolicy().hasHeightForWidth())
        self.site.setSizePolicy(sizePolicy2)
        self.site.setFont(font)

        self.horizontalLayout_3.addWidget(self.site)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy3)
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy4)
        self.verticalLayout_3 = QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(self.widget_5)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setFont(font)

        self.verticalLayout_3.addWidget(self.label_5)

        self.copy = QToolButton(self.widget_5)
        self.copy.setObjectName(u"copy")
        self.copy.setStyleSheet(u"QToolButton#copy {\n"
"	border-image: url(:/icon/\u590d\u5236.png)\n"
"}")

        self.verticalLayout_3.addWidget(self.copy)


        self.horizontalLayout.addWidget(self.widget_5)

        self.code = QTextBrowser(self.widget_3)
        self.code.setObjectName(u"code")
        font1 = QFont()
        font1.setPointSize(10)
        self.code.setFont(font1)

        self.horizontalLayout.addWidget(self.code)


        self.verticalLayout_2.addWidget(self.widget_3)


        self.verticalLayout.addWidget(self.widget)

        self.buttonBox = QDialogButtonBox(show_problem)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(show_problem)
        self.buttonBox.accepted.connect(show_problem.accept)
        self.buttonBox.rejected.connect(show_problem.reject)

        QMetaObject.connectSlotsByName(show_problem)
    # setupUi

    def retranslateUi(self, show_problem):
        show_problem.setWindowTitle(QCoreApplication.translate("show_problem", u"\u9898\u76ee\u8be6\u60c5", None))
        self.label.setText(QCoreApplication.translate("show_problem", u"\u9898\u76ee\uff1a", None))
        self.pid.setText(QCoreApplication.translate("show_problem", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("show_problem", u"\u5e73\u53f0\uff1a", None))
        self.site.setText(QCoreApplication.translate("show_problem", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("show_problem", u"\u4ee3\u7801\uff1a", None))
        self.copy.setText("")
    # retranslateUi

