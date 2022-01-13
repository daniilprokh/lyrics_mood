# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.l_api_list = QLabel(Dialog)
        self.l_api_list.setObjectName(u"l_api_list")
        font = QFont()
        font.setPointSize(10)
        self.l_api_list.setFont(font)

        self.verticalLayout.addWidget(self.l_api_list)

        self.cb_ibm_watson = QCheckBox(Dialog)
        self.cb_ibm_watson.setObjectName(u"cb_ibm_watson")
        self.cb_ibm_watson.setFont(font)
        self.cb_ibm_watson.setChecked(True)
        self.cb_ibm_watson.setTristate(False)

        self.verticalLayout.addWidget(self.cb_ibm_watson)

        self.cb_parallel_dots = QCheckBox(Dialog)
        self.cb_parallel_dots.setObjectName(u"cb_parallel_dots")
        self.cb_parallel_dots.setFont(font)
        self.cb_parallel_dots.setChecked(True)

        self.verticalLayout.addWidget(self.cb_parallel_dots)

        self.cb_twinword = QCheckBox(Dialog)
        self.cb_twinword.setObjectName(u"cb_twinword")
        self.cb_twinword.setFont(font)

        self.verticalLayout.addWidget(self.cb_twinword)

        self.cb_prompt = QCheckBox(Dialog)
        self.cb_prompt.setObjectName(u"cb_prompt")
        self.cb_prompt.setFont(font)

        self.verticalLayout.addWidget(self.cb_prompt)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pb_ok = QPushButton(Dialog)
        self.pb_ok.setObjectName(u"pb_ok")
        self.pb_ok.setFont(font)

        self.horizontalLayout.addWidget(self.pb_ok)

        self.pb_cancel = QPushButton(Dialog)
        self.pb_cancel.setObjectName(u"pb_cancel")
        self.pb_cancel.setFont(font)

        self.horizontalLayout.addWidget(self.pb_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u043e\u0440 API \u0434\u043b\u044f \u0430\u043d\u0430\u043b\u0438\u0437\u0430 \u0442\u0435\u043a\u0441\u0442\u0430", None))
        self.l_api_list.setText(QCoreApplication.translate("Dialog", u"\u0421\u043f\u0438\u0441\u043e\u043a API \u0434\u043b\u044f \u0430\u043d\u0430\u043b\u0438\u0437\u0430 \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u044f \u0442\u0435\u043a\u0441\u0442\u0430:", None))
        self.cb_ibm_watson.setText(QCoreApplication.translate("Dialog", u"IBM Watson Tone Analyzer API", None))
        self.cb_parallel_dots.setText(QCoreApplication.translate("Dialog", u"ParallelDots Text Analysis API", None))
        self.cb_twinword.setText(QCoreApplication.translate("Dialog", u"Twinword Emotion Analysis API", None))
        self.cb_prompt.setText(QCoreApplication.translate("Dialog", u"Prompt Text to Emotion API", None))
        self.pb_ok.setText(QCoreApplication.translate("Dialog", u"\u041e\u041a", None))
        self.pb_cancel.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

