# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        icon = QIcon()
        icon.addFile(u"lmood.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.a_audio_file = QAction(MainWindow)
        self.a_audio_file.setObjectName(u"a_audio_file")
        font = QFont()
        font.setPointSize(10)
        self.a_audio_file.setFont(font)
        self.a_api = QAction(MainWindow)
        self.a_api.setObjectName(u"a_api")
        self.a_api.setFont(font)
        self.a_tag = QAction(MainWindow)
        self.a_tag.setObjectName(u"a_tag")
        self.a_tag.setFont(font)
        self.a_txt = QAction(MainWindow)
        self.a_txt.setObjectName(u"a_txt")
        self.a_txt.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.l_artist = QLabel(self.centralwidget)
        self.l_artist.setObjectName(u"l_artist")
        self.l_artist.setFont(font)

        self.horizontalLayout.addWidget(self.l_artist)

        self.le_artist = QLineEdit(self.centralwidget)
        self.le_artist.setObjectName(u"le_artist")
        self.le_artist.setFont(font)

        self.horizontalLayout.addWidget(self.le_artist)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.l_title = QLabel(self.centralwidget)
        self.l_title.setObjectName(u"l_title")
        self.l_title.setFont(font)

        self.horizontalLayout.addWidget(self.l_title)

        self.le_title = QLineEdit(self.centralwidget)
        self.le_title.setObjectName(u"le_title")
        self.le_title.setFont(font)

        self.horizontalLayout.addWidget(self.le_title)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pb_load_lyrics = QPushButton(self.centralwidget)
        self.pb_load_lyrics.setObjectName(u"pb_load_lyrics")
        self.pb_load_lyrics.setFont(font)

        self.verticalLayout.addWidget(self.pb_load_lyrics)

        self.l_lyrics = QLabel(self.centralwidget)
        self.l_lyrics.setObjectName(u"l_lyrics")
        font1 = QFont()
        font1.setPointSize(12)
        self.l_lyrics.setFont(font1)

        self.verticalLayout.addWidget(self.l_lyrics)

        self.sa_lyrics = QScrollArea(self.centralwidget)
        self.sa_lyrics.setObjectName(u"sa_lyrics")
        self.sa_lyrics.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 776, 173))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.t_lyrics = QLabel(self.scrollAreaWidgetContents)
        self.t_lyrics.setObjectName(u"t_lyrics")
        self.t_lyrics.setFont(font1)

        self.verticalLayout_2.addWidget(self.t_lyrics)

        self.sa_lyrics.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.sa_lyrics)

        self.pb_analyze_tone = QPushButton(self.centralwidget)
        self.pb_analyze_tone.setObjectName(u"pb_analyze_tone")
        self.pb_analyze_tone.setFont(font)

        self.verticalLayout.addWidget(self.pb_analyze_tone)

        self.l_tone_analysis = QLabel(self.centralwidget)
        self.l_tone_analysis.setObjectName(u"l_tone_analysis")
        font2 = QFont()
        font2.setPointSize(11)
        self.l_tone_analysis.setFont(font2)

        self.verticalLayout.addWidget(self.l_tone_analysis)

        self.sa_tone_analysis = QScrollArea(self.centralwidget)
        self.sa_tone_analysis.setObjectName(u"sa_tone_analysis")
        self.sa_tone_analysis.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 776, 173))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.t_tone_analysis = QLabel(self.scrollAreaWidgetContents_2)
        self.t_tone_analysis.setObjectName(u"t_tone_analysis")
        self.t_tone_analysis.setFont(font1)

        self.verticalLayout_3.addWidget(self.t_tone_analysis)

        self.sa_tone_analysis.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout.addWidget(self.sa_tone_analysis)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.m_save_lyrics = QMenu(self.menu)
        self.m_save_lyrics.setObjectName(u"m_save_lyrics")
        self.m_save_lyrics.setFont(font)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.a_audio_file)
        self.menu.addAction(self.m_save_lyrics.menuAction())
        self.menu.addSeparator()
        self.menu.addAction(self.a_api)
        self.m_save_lyrics.addAction(self.a_txt)
        self.m_save_lyrics.addAction(self.a_tag)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"LyricsMood", None))
        self.a_audio_file.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0443\u0434\u0438\u043e\u0444\u0430\u0439\u043b..", None))
        self.a_api.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 API \u0434\u043b\u044f \u0430\u043d\u0430\u043b\u0438\u0437\u0430..", None))
        self.a_tag.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0433 \u0430\u0443\u0434\u0438\u043e\u0444\u0430\u0439\u043b\u0430", None))
        self.a_txt.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0441\u0442\u043e\u0432\u044b\u0439 \u0444\u0430\u0439\u043b (.txt)", None))
        self.l_artist.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c:", None))
        self.l_title.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0435\u0441\u043d\u0438:", None))
        self.pb_load_lyrics.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0442\u0435\u043a\u0441\u0442 \u043f\u0435\u0441\u043d\u0438 c Genius", None))
        self.l_lyrics.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0441\u0442 \u043f\u0435\u0441\u043d\u0438:", None))
        self.t_lyrics.setText("")
        self.pb_analyze_tone.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0430\u043d\u0430\u043b\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435 \u043f\u0435\u0441\u043d\u0438", None))
        self.l_tone_analysis.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0430\u043b\u0438\u0437 \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u044f \u0442\u0435\u043a\u0441\u0442\u0430:", None))
        self.t_tone_analysis.setText("")
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e", None))
        self.m_save_lyrics.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0442\u0435\u043a\u0441\u0442 \u043f\u0435\u0441\u043d\u0438 \u043a\u0430\u043a", None))
    # retranslateUi

