# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\My_Codes\easylearn-fmri\eslearn\gui_test\easylearn_data_loading_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1037, 484)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.listView_modalities = QtWidgets.QListView(self.centralwidget)
        self.listView_modalities.setMinimumSize(QtCore.QSize(10, 10))
        self.listView_modalities.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.listView_modalities.setObjectName("listView_modalities")
        self.gridLayout.addWidget(self.listView_modalities, 1, 2, 1, 1)
        self.listView_files = QtWidgets.QListView(self.centralwidget)
        self.listView_files.setMinimumSize(QtCore.QSize(10, 10))
        self.listView_files.setBaseSize(QtCore.QSize(10, 10))
        self.listView_files.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.listView_files.setObjectName("listView_files")
        self.gridLayout.addWidget(self.listView_files, 1, 4, 1, 1)
        self.group_btn = QtWidgets.QHBoxLayout()
        self.group_btn.setObjectName("group_btn")
        self.pushButton_addgroups = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_addgroups.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_addgroups.setToolTipDuration(-5)
        self.pushButton_addgroups.setObjectName("pushButton_addgroups")
        self.group_btn.addWidget(self.pushButton_addgroups)
        self.pushButton_removegroups = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_removegroups.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_removegroups.setObjectName("pushButton_removegroups")
        self.group_btn.addWidget(self.pushButton_removegroups)
        self.pushButton_cleargroups = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cleargroups.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_cleargroups.setObjectName("pushButton_cleargroups")
        self.group_btn.addWidget(self.pushButton_cleargroups)
        self.gridLayout.addLayout(self.group_btn, 2, 0, 1, 1)
        self.modality_btn = QtWidgets.QHBoxLayout()
        self.modality_btn.setObjectName("modality_btn")
        self.pushButton_addmodalities = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_addmodalities.setToolTipDuration(-5)
        self.pushButton_addmodalities.setObjectName("pushButton_addmodalities")
        self.modality_btn.addWidget(self.pushButton_addmodalities)
        self.pushButton_removemodalites = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_removemodalites.setObjectName("pushButton_removemodalites")
        self.modality_btn.addWidget(self.pushButton_removemodalites)
        self.pushButton_clearmodalities = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clearmodalities.setObjectName("pushButton_clearmodalities")
        self.modality_btn.addWidget(self.pushButton_clearmodalities)
        self.gridLayout.addLayout(self.modality_btn, 2, 2, 1, 1)
        self.listView_groups = QtWidgets.QListView(self.centralwidget)
        self.listView_groups.setMinimumSize(QtCore.QSize(10, 10))
        self.listView_groups.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.listView_groups.setObjectName("listView_groups")
        self.gridLayout.addWidget(self.listView_groups, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.file_btn = QtWidgets.QHBoxLayout()
        self.file_btn.setObjectName("file_btn")
        self.pushButton_addfiles = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_addfiles.setBaseSize(QtCore.QSize(10, 10))
        self.pushButton_addfiles.setToolTipDuration(-5)
        self.pushButton_addfiles.setObjectName("pushButton_addfiles")
        self.file_btn.addWidget(self.pushButton_addfiles)
        self.pushButton_removefiles = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_removefiles.setBaseSize(QtCore.QSize(10, 10))
        self.pushButton_removefiles.setObjectName("pushButton_removefiles")
        self.file_btn.addWidget(self.pushButton_removefiles)
        self.pushButton_clearfiles = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clearfiles.setBaseSize(QtCore.QSize(10, 10))
        self.pushButton_clearfiles.setObjectName("pushButton_clearfiles")
        self.file_btn.addWidget(self.pushButton_clearfiles)
        self.gridLayout.addLayout(self.file_btn, 2, 4, 1, 1)
        self.label_modalities = QtWidgets.QLabel(self.centralwidget)
        self.label_modalities.setObjectName("label_modalities")
        self.gridLayout.addWidget(self.label_modalities, 0, 2, 1, 1)
        self.label_file = QtWidgets.QLabel(self.centralwidget)
        self.label_file.setObjectName("label_file")
        self.gridLayout.addWidget(self.label_file, 0, 4, 1, 1)
        self.label_group = QtWidgets.QLabel(self.centralwidget)
        self.label_group.setObjectName("label_group")
        self.gridLayout.addWidget(self.label_group, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1037, 26))
        self.menubar.setObjectName("menubar")
        self.menuConfiguration_file = QtWidgets.QMenu(self.menubar)
        self.menuConfiguration_file.setObjectName("menuConfiguration_file")
        self.menuHelp_H = QtWidgets.QMenu(self.menubar)
        self.menuHelp_H.setObjectName("menuHelp_H")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionChoose_configuration_file = QtWidgets.QAction(MainWindow)
        self.actionChoose_configuration_file.setObjectName("actionChoose_configuration_file")
        self.actionSave_configuration = QtWidgets.QAction(MainWindow)
        self.actionSave_configuration.setObjectName("actionSave_configuration")
        self.menuConfiguration_file.addAction(self.actionChoose_configuration_file)
        self.menuConfiguration_file.addAction(self.actionSave_configuration)
        self.menubar.addAction(self.menuConfiguration_file.menuAction())
        self.menubar.addAction(self.menuHelp_H.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_addgroups.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>push the button then close program</p></body></html>"))
        self.pushButton_addgroups.setText(_translate("MainWindow", "Add"))
        self.pushButton_removegroups.setText(_translate("MainWindow", "Remove"))
        self.pushButton_cleargroups.setText(_translate("MainWindow", "Clear"))
        self.pushButton_addmodalities.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>push the button then close program</p></body></html>"))
        self.pushButton_addmodalities.setText(_translate("MainWindow", "Add"))
        self.pushButton_removemodalites.setText(_translate("MainWindow", "Remove"))
        self.pushButton_clearmodalities.setText(_translate("MainWindow", "Clear"))
        self.pushButton_addfiles.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>push the button then close program</p></body></html>"))
        self.pushButton_addfiles.setText(_translate("MainWindow", "Add"))
        self.pushButton_removefiles.setText(_translate("MainWindow", "Remove"))
        self.pushButton_clearfiles.setText(_translate("MainWindow", "Clear"))
        self.label_modalities.setText(_translate("MainWindow", "Modalities"))
        self.label_file.setText(_translate("MainWindow", "Files"))
        self.label_group.setText(_translate("MainWindow", "Groups"))
        self.menuConfiguration_file.setTitle(_translate("MainWindow", "Configuration file(&F)"))
        self.menuHelp_H.setTitle(_translate("MainWindow", "Help(&H)"))
        self.actionChoose_configuration_file.setText(_translate("MainWindow", "Choose configuration"))
        self.actionSave_configuration.setText(_translate("MainWindow", "Save configuration"))

