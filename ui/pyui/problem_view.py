# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'problem_view.ui'
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
    QFrame, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QTextBrowser, QVBoxLayout, QWidget)

class Ui_problem_view(object):
    def setupUi(self, problem_view):
        if not problem_view.objectName():
            problem_view.setObjectName(u"problem_view")
        problem_view.resize(475, 509)
        self.verticalLayout = QVBoxLayout(problem_view)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(problem_view)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.site = QLabel(problem_view)
        self.site.setObjectName(u"site")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.site.sizePolicy().hasHeightForWidth())
        self.site.setSizePolicy(sizePolicy)
        self.site.setFont(font)
        self.site.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.site)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(problem_view)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.problem = QLabel(problem_view)
        self.problem.setObjectName(u"problem")
        sizePolicy.setHeightForWidth(self.problem.sizePolicy().hasHeightForWidth())
        self.problem.setSizePolicy(sizePolicy)
        self.problem.setFont(font)
        self.problem.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.problem)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.line = QFrame(problem_view)
        self.line.setObjectName(u"line")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy1)
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setFrameShape(QFrame.HLine)

        self.horizontalLayout_3.addWidget(self.line)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(problem_view)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.pushButton = QPushButton(problem_view)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy3)

        self.verticalLayout_2.addWidget(self.pushButton)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.code_browser = QTextBrowser(problem_view)
        self.code_browser.setObjectName(u"code_browser")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.code_browser.sizePolicy().hasHeightForWidth())
        self.code_browser.setSizePolicy(sizePolicy4)
        font1 = QFont()
        font1.setPointSize(15)
        self.code_browser.setFont(font1)

        self.horizontalLayout_3.addWidget(self.code_browser)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.buttonBox = QDialogButtonBox(problem_view)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(problem_view)
        self.buttonBox.clicked.connect(problem_view.close)

        QMetaObject.connectSlotsByName(problem_view)
    # setupUi

    def retranslateUi(self, problem_view):
        problem_view.setWindowTitle(QCoreApplication.translate("problem_view", u"Problem-View", None))
        self.label_2.setText(QCoreApplication.translate("problem_view", u"\u5e73\u53f0", None))
        self.site.setText(QCoreApplication.translate("problem_view", u"None", None))
        self.label_4.setText(QCoreApplication.translate("problem_view", u"\u9898\u76ee  ", None))
        self.problem.setText(QCoreApplication.translate("problem_view", u"None", None))
        self.label.setText(QCoreApplication.translate("problem_view", u"\u4ee3\u7801", None))
        self.pushButton.setText(QCoreApplication.translate("problem_view", u"Copy", None))
        self.code_browser.setHtml(QCoreApplication.translate("problem_view", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt;\">#include&lt;iostream&gt;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt;\">int main(){</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" fon"
                        "t-size:13pt;\">    std::cout &lt;&lt; &quot;None&quot;;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt;\">}</span></p></body></html>", None))
    # retranslateUi

