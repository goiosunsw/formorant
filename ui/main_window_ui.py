# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(633, 520)
        self.actionOpen_recording = QAction(MainWindow)
        self.actionOpen_recording.setObjectName(u"actionOpen_recording")
        self.actionSave_recording = QAction(MainWindow)
        self.actionSave_recording.setObjectName(u"actionSave_recording")
        self.actionDevice_Setup = QAction(MainWindow)
        self.actionDevice_Setup.setObjectName(u"actionDevice_Setup")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.action_New = QAction(MainWindow)
        self.action_New.setObjectName(u"action_New")
        self.action_Guide = QAction(MainWindow)
        self.action_Guide.setObjectName(u"action_Guide")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.vlayout1 = QVBoxLayout()
        self.vlayout1.setObjectName(u"vlayout1")
        self.vlayout1.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.vlayout1.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setMinimumSize(QSize(400, 300))

        self.horizontalLayout.addWidget(self.widget)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.interval_label = QLabel(self.centralwidget)
        self.interval_label.setObjectName(u"interval_label")

        self.verticalLayout_2.addWidget(self.interval_label)

        self.interval_selector = QComboBox(self.centralwidget)
        self.interval_selector.setObjectName(u"interval_selector")

        self.verticalLayout_2.addWidget(self.interval_selector)

        self.fft_size_label = QLabel(self.centralwidget)
        self.fft_size_label.setObjectName(u"fft_size_label")

        self.verticalLayout_2.addWidget(self.fft_size_label)

        self.fft_size_selector = QComboBox(self.centralwidget)
        self.fft_size_selector.setObjectName(u"fft_size_selector")

        self.verticalLayout_2.addWidget(self.fft_size_selector)

        self.noise_selector = QRadioButton(self.centralwidget)
        self.noise_selector.setObjectName(u"noise_selector")

        self.verticalLayout_2.addWidget(self.noise_selector)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(0, 1)

        self.vlayout1.addLayout(self.horizontalLayout)

        self.info_label_top = QLabel(self.centralwidget)
        self.info_label_top.setObjectName(u"info_label_top")

        self.vlayout1.addWidget(self.info_label_top)

        self.info_label_bottom = QLabel(self.centralwidget)
        self.info_label_bottom.setObjectName(u"info_label_bottom")

        self.vlayout1.addWidget(self.info_label_bottom)

        self.vlayout1.setStretch(0, 1)

        self.gridLayout.addLayout(self.vlayout1, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 633, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.action_New)
        self.menuFile.addAction(self.actionOpen_recording)
        self.menuFile.addAction(self.actionSave_recording)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionDevice_Setup)
        self.menuHelp.addAction(self.action_Guide)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen_recording.setText(QCoreApplication.translate("MainWindow", u"&Open recording...", None))
        self.actionSave_recording.setText(QCoreApplication.translate("MainWindow", u"&Save recording...", None))
        self.actionDevice_Setup.setText(QCoreApplication.translate("MainWindow", u"&Device Setup...", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About...", None))
        self.action_New.setText(QCoreApplication.translate("MainWindow", u"&New", None))
        self.action_Guide.setText(QCoreApplication.translate("MainWindow", u"&Guide", None))
        self.interval_label.setText(QCoreApplication.translate("MainWindow", u"Interval", None))
        self.fft_size_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.noise_selector.setText(QCoreApplication.translate("MainWindow", u"Noise", None))
        self.info_label_top.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.info_label_bottom.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

