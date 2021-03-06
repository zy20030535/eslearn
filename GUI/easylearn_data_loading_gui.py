# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\easylearn_data_loading_gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(974, 833)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(21)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_addgroups = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_addgroups.setMinimumSize(QtCore.QSize(20, 40))
        self.pushButton_addgroups.setToolTipDuration(-5)
        self.pushButton_addgroups.setObjectName("pushButton_addgroups")
        self.gridLayout_2.addWidget(self.pushButton_addgroups, 2, 0, 1, 1)
        self.listView_groups = QtWidgets.QListView(self.centralwidget)
        self.listView_groups.setEnabled(True)
        self.listView_groups.setMinimumSize(QtCore.QSize(20, 10))
        self.listView_groups.setMaximumSize(QtCore.QSize(5000, 5000))
        self.listView_groups.setAcceptDrops(False)
        self.listView_groups.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.listView_groups.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listView_groups.setDragEnabled(False)
        self.listView_groups.setBatchSize(94)
        self.listView_groups.setObjectName("listView_groups")
        self.gridLayout_2.addWidget(self.listView_groups, 1, 0, 1, 3)
        self.pushButton_removegroups = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_removegroups.setMinimumSize(QtCore.QSize(20, 40))
        self.pushButton_removegroups.setObjectName("pushButton_removegroups")
        self.gridLayout_2.addWidget(self.pushButton_removegroups, 2, 1, 1, 1)
        self.pushButton_cleargroups = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cleargroups.setMinimumSize(QtCore.QSize(20, 40))
        self.pushButton_cleargroups.setObjectName("pushButton_cleargroups")
        self.gridLayout_2.addWidget(self.pushButton_cleargroups, 2, 2, 1, 1)
        self.label_group = QtWidgets.QLabel(self.centralwidget)
        self.label_group.setObjectName("label_group")
        self.gridLayout_2.addWidget(self.label_group, 0, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_mask = QtWidgets.QLabel(self.centralwidget)
        self.label_mask.setObjectName("label_mask")
        self.gridLayout_3.addWidget(self.label_mask, 2, 0, 1, 1)
        self.pushButton_selectMask = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_selectMask.setMinimumSize(QtCore.QSize(20, 40))
        self.pushButton_selectMask.setBaseSize(QtCore.QSize(10, 10))
        self.pushButton_selectMask.setToolTipDuration(-5)
        self.pushButton_selectMask.setObjectName("pushButton_selectMask")
        self.gridLayout_3.addWidget(self.pushButton_selectMask, 4, 0, 1, 1)
        self.lineEdit_mask = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_mask.setMinimumSize(QtCore.QSize(30, 40))
        self.lineEdit_mask.setObjectName("lineEdit_mask")
        self.gridLayout_3.addWidget(self.lineEdit_mask, 3, 0, 1, 3)
        self.pushButton_clearMask = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clearMask.setMinimumSize(QtCore.QSize(20, 40))
        self.pushButton_clearMask.setBaseSize(QtCore.QSize(10, 10))
        self.pushButton_clearMask.setObjectName("pushButton_clearMask")
        self.gridLayout_3.addWidget(self.pushButton_clearMask, 4, 1, 1, 1)
        self.pushButton_mask = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mask.setMinimumSize(QtCore.QSize(20, 40))
        self.pushButton_mask.setBaseSize(QtCore.QSize(10, 10))
        self.pushButton_mask.setObjectName("pushButton_mask")
        self.gridLayout_3.addWidget(self.pushButton_mask, 4, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_3, 10, 2, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_target = QtWidgets.QLabel(self.centralwidget)
        self.label_target.setObjectName("label_target")
        self.gridLayout_4.addWidget(self.label_target, 0, 0, 1, 1)
        self.lineEdit_target = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_target.setMinimumSize(QtCore.QSize(30, 40))
        self.lineEdit_target.setObjectName("lineEdit_target")
        self.gridLayout_4.addWidget(self.lineEdit_target, 1, 0, 1, 3)
        self.pushButton_selectTarget = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_selectTarget.setMinimumSize(QtCore.QSize(20, 40))
        self.pushButton_selectTarget.setBaseSize(QtCore.QSize(10, 10))
        self.pushButton_selectTarget.setToolTipDuration(-5)
        self.pushButton_selectTarget.setObjectName("pushButton_selectTarget")
        self.gridLayout_4.addWidget(self.pushButton_selectTarget, 2, 0, 1, 1)
        self.pushButton_target = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_target.setMinimumSize(QtCore.QSize(20, 40))
        self.pushButton_target.setBaseSize(QtCore.QSize(10, 10))
        self.pushButton_target.setObjectName("pushButton_target")
        self.gridLayout_4.addWidget(self.pushButton_target, 2, 2, 1, 1)
        self.pushButton_clearTarget = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clearTarget.setMinimumSize(QtCore.QSize(20, 40))
        self.pushButton_clearTarget.setBaseSize(QtCore.QSize(10, 10))
        self.pushButton_clearTarget.setObjectName("pushButton_clearTarget")
        self.gridLayout_4.addWidget(self.pushButton_clearTarget, 2, 1, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_4, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_7.addItem(spacerItem, 9, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem1, 3, 1, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_addmodalities = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_addmodalities.setMinimumSize(QtCore.QSize(20, 40))
        self.pushButton_addmodalities.setToolTipDuration(-5)
        self.pushButton_addmodalities.setObjectName("pushButton_addmodalities")
        self.gridLayout_5.addWidget(self.pushButton_addmodalities, 2, 0, 1, 1)
        self.pushButton_removemodalites = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_removemodalites.setMinimumSize(QtCore.QSize(20, 40))
        self.pushButton_removemodalites.setObjectName("pushButton_removemodalites")
        self.gridLayout_5.addWidget(self.pushButton_removemodalites, 2, 1, 1, 1)
        self.label_modalities = QtWidgets.QLabel(self.centralwidget)
        self.label_modalities.setObjectName("label_modalities")
        self.gridLayout_5.addWidget(self.label_modalities, 0, 0, 1, 1)
        self.listView_modalities = QtWidgets.QListView(self.centralwidget)
        self.listView_modalities.setEnabled(True)
        self.listView_modalities.setMinimumSize(QtCore.QSize(20, 10))
        self.listView_modalities.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.listView_modalities.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listView_modalities.setObjectName("listView_modalities")
        self.gridLayout_5.addWidget(self.listView_modalities, 1, 0, 1, 3)
        self.pushButton_clearmodalities = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clearmodalities.setMinimumSize(QtCore.QSize(20, 40))
        self.pushButton_clearmodalities.setObjectName("pushButton_clearmodalities")
        self.gridLayout_5.addWidget(self.pushButton_clearmodalities, 2, 2, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_5, 10, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_covariance = QtWidgets.QLabel(self.centralwidget)
        self.label_covariance.setObjectName("label_covariance")
        self.gridLayout.addWidget(self.label_covariance, 0, 0, 1, 1)
        self.pushButton_selectCovariance = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_selectCovariance.setMinimumSize(QtCore.QSize(20, 40))
        self.pushButton_selectCovariance.setBaseSize(QtCore.QSize(10, 10))
        self.pushButton_selectCovariance.setToolTipDuration(-5)
        self.pushButton_selectCovariance.setObjectName("pushButton_selectCovariance")
        self.gridLayout.addWidget(self.pushButton_selectCovariance, 2, 0, 1, 1)
        self.pushButton_clearCovriance = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clearCovriance.setMinimumSize(QtCore.QSize(20, 40))
        self.pushButton_clearCovriance.setBaseSize(QtCore.QSize(10, 10))
        self.pushButton_clearCovriance.setObjectName("pushButton_clearCovriance")
        self.gridLayout.addWidget(self.pushButton_clearCovriance, 2, 1, 1, 1)
        self.lineEdit_covariates = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_covariates.setMinimumSize(QtCore.QSize(30, 40))
        self.lineEdit_covariates.setObjectName("lineEdit_covariates")
        self.gridLayout.addWidget(self.lineEdit_covariates, 1, 0, 1, 3)
        self.pushButton_covariate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_covariate.setMinimumSize(QtCore.QSize(20, 40))
        self.pushButton_covariate.setBaseSize(QtCore.QSize(10, 10))
        self.pushButton_covariate.setObjectName("pushButton_covariate")
        self.gridLayout.addWidget(self.pushButton_covariate, 2, 2, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout, 8, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pushButton_removefiles = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_removefiles.setMinimumSize(QtCore.QSize(20, 40))
        self.pushButton_removefiles.setBaseSize(QtCore.QSize(10, 10))
        self.pushButton_removefiles.setObjectName("pushButton_removefiles")
        self.gridLayout_6.addWidget(self.pushButton_removefiles, 3, 2, 1, 1)
        self.pushButton_addfiles = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_addfiles.setMinimumSize(QtCore.QSize(20, 40))
        self.pushButton_addfiles.setBaseSize(QtCore.QSize(10, 10))
        self.pushButton_addfiles.setToolTipDuration(-5)
        self.pushButton_addfiles.setObjectName("pushButton_addfiles")
        self.gridLayout_6.addWidget(self.pushButton_addfiles, 3, 1, 1, 1)
        self.label_file = QtWidgets.QLabel(self.centralwidget)
        self.label_file.setObjectName("label_file")
        self.gridLayout_6.addWidget(self.label_file, 0, 1, 1, 1)
        self.listView_files = QtWidgets.QListView(self.centralwidget)
        self.listView_files.setEnabled(True)
        self.listView_files.setMinimumSize(QtCore.QSize(10, 400))
        self.listView_files.setBaseSize(QtCore.QSize(10, 10))
        self.listView_files.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.listView_files.setAcceptDrops(False)
        self.listView_files.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.listView_files.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listView_files.setDragEnabled(False)
        self.listView_files.setObjectName("listView_files")
        self.gridLayout_6.addWidget(self.listView_files, 1, 1, 1, 3)
        self.pushButton_clearfiles = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clearfiles.setMinimumSize(QtCore.QSize(20, 40))
        self.pushButton_clearfiles.setBaseSize(QtCore.QSize(10, 10))
        self.pushButton_clearfiles.setObjectName("pushButton_clearfiles")
        self.gridLayout_6.addWidget(self.pushButton_clearfiles, 3, 3, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_6, 1, 2, 8, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_7.addItem(spacerItem2, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_7.addItem(spacerItem3, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 974, 26))
        self.menubar.setObjectName("menubar")
        self.menuConfiguration_file = QtWidgets.QMenu(self.menubar)
        self.menuConfiguration_file.setObjectName("menuConfiguration_file")
        self.menuHelp_H = QtWidgets.QMenu(self.menubar)
        self.menuHelp_H.setObjectName("menuHelp_H")
        self.menuSkin = QtWidgets.QMenu(self.menubar)
        self.menuSkin.setObjectName("menuSkin")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionChoose_configuration_file = QtWidgets.QAction(MainWindow)
        self.actionChoose_configuration_file.setObjectName("actionChoose_configuration_file")
        self.actionSave_configuration = QtWidgets.QAction(MainWindow)
        self.actionSave_configuration.setObjectName("actionSave_configuration")
        self.actionWeb = QtWidgets.QAction(MainWindow)
        self.actionWeb.setObjectName("actionWeb")
        self.actionPDF = QtWidgets.QAction(MainWindow)
        self.actionPDF.setObjectName("actionPDF")
        self.actionDark = QtWidgets.QAction(MainWindow)
        self.actionDark.setObjectName("actionDark")
        self.actionBlack = QtWidgets.QAction(MainWindow)
        self.actionBlack.setObjectName("actionBlack")
        self.actionDarkOrange = QtWidgets.QAction(MainWindow)
        self.actionDarkOrange.setObjectName("actionDarkOrange")
        self.actionGray = QtWidgets.QAction(MainWindow)
        self.actionGray.setObjectName("actionGray")
        self.actionBlue = QtWidgets.QAction(MainWindow)
        self.actionBlue.setObjectName("actionBlue")
        self.actionNavy = QtWidgets.QAction(MainWindow)
        self.actionNavy.setObjectName("actionNavy")
        self.actionClassic = QtWidgets.QAction(MainWindow)
        self.actionClassic.setObjectName("actionClassic")
        self.actionLight = QtWidgets.QAction(MainWindow)
        self.actionLight.setObjectName("actionLight")
        self.menuConfiguration_file.addAction(self.actionChoose_configuration_file)
        self.menuConfiguration_file.addAction(self.actionSave_configuration)
        self.menuHelp_H.addAction(self.actionWeb)
        self.menuHelp_H.addAction(self.actionPDF)
        self.menuSkin.addAction(self.actionDark)
        self.menuSkin.addAction(self.actionBlack)
        self.menuSkin.addAction(self.actionDarkOrange)
        self.menuSkin.addAction(self.actionGray)
        self.menuSkin.addAction(self.actionBlue)
        self.menuSkin.addAction(self.actionNavy)
        self.menuSkin.addAction(self.actionClassic)
        self.menuSkin.addAction(self.actionLight)
        self.menubar.addAction(self.menuConfiguration_file.menuAction())
        self.menubar.addAction(self.menuHelp_H.menuAction())
        self.menubar.addAction(self.menuSkin.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_addgroups.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>push the button then close program</p></body></html>"))
        self.pushButton_addgroups.setText(_translate("MainWindow", "Add"))
        self.pushButton_removegroups.setText(_translate("MainWindow", "Remove"))
        self.pushButton_cleargroups.setText(_translate("MainWindow", "Clear"))
        self.label_group.setText(_translate("MainWindow", "Groups"))
        self.label_mask.setText(_translate("MainWindow", "Mask"))
        self.pushButton_selectMask.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>push the button then close program</p></body></html>"))
        self.pushButton_selectMask.setText(_translate("MainWindow", "Select mask"))
        self.pushButton_clearMask.setText(_translate("MainWindow", "Clear mask"))
        self.pushButton_mask.setText(_translate("MainWindow", "OK"))
        self.label_target.setText(_translate("MainWindow", "Targets"))
        self.pushButton_selectTarget.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>push the button then close program</p></body></html>"))
        self.pushButton_selectTarget.setText(_translate("MainWindow", "Select targets"))
        self.pushButton_target.setText(_translate("MainWindow", "OK"))
        self.pushButton_clearTarget.setText(_translate("MainWindow", "Clear targets"))
        self.pushButton_addmodalities.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>push the button then close program</p></body></html>"))
        self.pushButton_addmodalities.setText(_translate("MainWindow", "Add"))
        self.pushButton_removemodalites.setText(_translate("MainWindow", "Remove"))
        self.label_modalities.setText(_translate("MainWindow", "Modalities"))
        self.pushButton_clearmodalities.setText(_translate("MainWindow", "Clear"))
        self.label_covariance.setText(_translate("MainWindow", "Covariates"))
        self.pushButton_selectCovariance.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>push the button then close program</p></body></html>"))
        self.pushButton_selectCovariance.setText(_translate("MainWindow", "Select covariates"))
        self.pushButton_clearCovriance.setText(_translate("MainWindow", "Clear covariates"))
        self.pushButton_covariate.setText(_translate("MainWindow", "OK"))
        self.pushButton_removefiles.setText(_translate("MainWindow", "Remove"))
        self.pushButton_addfiles.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>push the button then close program</p></body></html>"))
        self.pushButton_addfiles.setText(_translate("MainWindow", "Add"))
        self.label_file.setText(_translate("MainWindow", "Files"))
        self.pushButton_clearfiles.setText(_translate("MainWindow", "Clear"))
        self.menuConfiguration_file.setTitle(_translate("MainWindow", "Configuration file(&F)"))
        self.menuHelp_H.setTitle(_translate("MainWindow", "Help(&H)"))
        self.menuSkin.setTitle(_translate("MainWindow", "Skin"))
        self.actionChoose_configuration_file.setText(_translate("MainWindow", "Load configuration"))
        self.actionSave_configuration.setText(_translate("MainWindow", "Save configuration"))
        self.actionWeb.setText(_translate("MainWindow", "Web"))
        self.actionPDF.setText(_translate("MainWindow", "PDF"))
        self.actionDark.setText(_translate("MainWindow", "Dark"))
        self.actionBlack.setText(_translate("MainWindow", "Black"))
        self.actionDarkOrange.setText(_translate("MainWindow", "DarkOrange"))
        self.actionGray.setText(_translate("MainWindow", "Gray"))
        self.actionBlue.setText(_translate("MainWindow", "Blue"))
        self.actionNavy.setText(_translate("MainWindow", "Navy"))
        self.actionClassic.setText(_translate("MainWindow", "Classic"))
        self.actionLight.setText(_translate("MainWindow", "Light"))
