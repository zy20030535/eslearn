# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './easylearn_model_evaluation_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(625, 643)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_selected = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_selected.setObjectName("groupBox_selected")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_selected)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_4.addWidget(self.groupBox_selected, 2, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 200))
        self.groupBox_3.setBaseSize(QtCore.QSize(0, 0))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_3)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_kfold = QtWidgets.QWidget()
        self.tab_kfold.setObjectName("tab_kfold")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_kfold)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_8 = QtWidgets.QLabel(self.tab_kfold)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_kfold)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_kfold)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_kfold_n_splits = QtWidgets.QLineEdit(self.tab_kfold)
        self.lineEdit_kfold_n_splits.setObjectName("lineEdit_kfold_n_splits")
        self.gridLayout_3.addWidget(self.lineEdit_kfold_n_splits, 0, 2, 1, 1)
        self.comboBox_kfold_shuffle = QtWidgets.QComboBox(self.tab_kfold)
        self.comboBox_kfold_shuffle.setObjectName("comboBox_kfold_shuffle")
        self.comboBox_kfold_shuffle.addItem("")
        self.comboBox_kfold_shuffle.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_kfold_shuffle, 1, 2, 1, 1)
        self.spinBox_kfold_randomstate = QtWidgets.QSpinBox(self.tab_kfold)
        self.spinBox_kfold_randomstate.setMaximum(10000)
        self.spinBox_kfold_randomstate.setObjectName("spinBox_kfold_randomstate")
        self.gridLayout_3.addWidget(self.spinBox_kfold_randomstate, 2, 2, 1, 1)
        self.tabWidget.addTab(self.tab_kfold, "")
        self.tab_stratifiedkfold = QtWidgets.QWidget()
        self.tab_stratifiedkfold.setObjectName("tab_stratifiedkfold")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_stratifiedkfold)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_10 = QtWidgets.QLabel(self.tab_stratifiedkfold)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)
        self.lineEdit_stratifiedkfold_n_splits = QtWidgets.QLineEdit(self.tab_stratifiedkfold)
        self.lineEdit_stratifiedkfold_n_splits.setObjectName("lineEdit_stratifiedkfold_n_splits")
        self.gridLayout_2.addWidget(self.lineEdit_stratifiedkfold_n_splits, 0, 1, 1, 1)
        self.comboBox_stratifiedkfold_shuffle = QtWidgets.QComboBox(self.tab_stratifiedkfold)
        self.comboBox_stratifiedkfold_shuffle.setObjectName("comboBox_stratifiedkfold_shuffle")
        self.comboBox_stratifiedkfold_shuffle.addItem("")
        self.comboBox_stratifiedkfold_shuffle.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_stratifiedkfold_shuffle, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_stratifiedkfold)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab_stratifiedkfold)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)
        self.spinBox_stratifiedkfold_randomstate = QtWidgets.QSpinBox(self.tab_stratifiedkfold)
        self.spinBox_stratifiedkfold_randomstate.setMaximum(10000)
        self.spinBox_stratifiedkfold_randomstate.setObjectName("spinBox_stratifiedkfold_randomstate")
        self.gridLayout_2.addWidget(self.spinBox_stratifiedkfold_randomstate, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tab_stratifiedkfold, "")
        self.tab_randomsplit = QtWidgets.QWidget()
        self.tab_randomsplit.setObjectName("tab_randomsplit")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_randomsplit)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_randomsplits_n_splits = QtWidgets.QLineEdit(self.tab_randomsplit)
        self.lineEdit_randomsplits_n_splits.setObjectName("lineEdit_randomsplits_n_splits")
        self.gridLayout.addWidget(self.lineEdit_randomsplits_n_splits, 0, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_randomsplit)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.doubleSpinBox_randomsplits_testsize = QtWidgets.QDoubleSpinBox(self.tab_randomsplit)
        self.doubleSpinBox_randomsplits_testsize.setMinimum(0.01)
        self.doubleSpinBox_randomsplits_testsize.setMaximum(1.0)
        self.doubleSpinBox_randomsplits_testsize.setSingleStep(0.1)
        self.doubleSpinBox_randomsplits_testsize.setProperty("value", 0.2)
        self.doubleSpinBox_randomsplits_testsize.setObjectName("doubleSpinBox_randomsplits_testsize")
        self.gridLayout.addWidget(self.doubleSpinBox_randomsplits_testsize, 1, 1, 1, 2)
        self.doubleSpinBox_randomsplits_trainsize = QtWidgets.QDoubleSpinBox(self.tab_randomsplit)
        self.doubleSpinBox_randomsplits_trainsize.setMinimum(0.1)
        self.doubleSpinBox_randomsplits_trainsize.setMaximum(1.0)
        self.doubleSpinBox_randomsplits_trainsize.setSingleStep(0.1)
        self.doubleSpinBox_randomsplits_trainsize.setProperty("value", 0.8)
        self.doubleSpinBox_randomsplits_trainsize.setObjectName("doubleSpinBox_randomsplits_trainsize")
        self.gridLayout.addWidget(self.doubleSpinBox_randomsplits_trainsize, 3, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_randomsplit)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_randomsplit)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.tab_randomsplit)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 4, 0, 1, 1)
        self.spinBox_randomsplits_randomstate = QtWidgets.QSpinBox(self.tab_randomsplit)
        self.spinBox_randomsplits_randomstate.setMaximum(10000)
        self.spinBox_randomsplits_randomstate.setObjectName("spinBox_randomsplits_randomstate")
        self.gridLayout.addWidget(self.spinBox_randomsplits_randomstate, 4, 2, 1, 1)
        self.tabWidget.addTab(self.tab_randomsplit, "")
        self.tab_userdefined = QtWidgets.QWidget()
        self.tab_userdefined.setObjectName("tab_userdefined")
        self.tabWidget.addTab(self.tab_userdefined, "")
        self.gridLayout_7.addWidget(self.tabWidget, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_7.addItem(spacerItem, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 0, 0, 1, 2)
        self.groupBox_candidate = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_candidate.setMinimumSize(QtCore.QSize(0, 200))
        self.groupBox_candidate.setObjectName("groupBox_candidate")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_candidate)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_4.addWidget(self.groupBox_candidate, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 625, 26))
        self.menubar.setObjectName("menubar")
        self.menuConfiguration_file_F = QtWidgets.QMenu(self.menubar)
        self.menuConfiguration_file_F.setObjectName("menuConfiguration_file_F")
        self.menuSkin = QtWidgets.QMenu(self.menubar)
        self.menuSkin.setObjectName("menuSkin")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_configuration = QtWidgets.QAction(MainWindow)
        self.actionLoad_configuration.setObjectName("actionLoad_configuration")
        self.actionSave_configuration = QtWidgets.QAction(MainWindow)
        self.actionSave_configuration.setObjectName("actionSave_configuration")
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
        self.menuConfiguration_file_F.addAction(self.actionLoad_configuration)
        self.menuConfiguration_file_F.addAction(self.actionSave_configuration)
        self.menuSkin.addAction(self.actionDark)
        self.menuSkin.addAction(self.actionBlack)
        self.menuSkin.addAction(self.actionDarkOrange)
        self.menuSkin.addAction(self.actionGray)
        self.menuSkin.addAction(self.actionBlue)
        self.menuSkin.addAction(self.actionNavy)
        self.menuSkin.addAction(self.actionClassic)
        self.menubar.addAction(self.menuConfiguration_file_F.menuAction())
        self.menubar.addAction(self.menuSkin.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_selected.setTitle(_translate("MainWindow", "Selected datasets"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Cross-validation"))
        self.label_8.setText(_translate("MainWindow", "random_state"))
        self.label_7.setText(_translate("MainWindow", "shuffle"))
        self.label.setText(_translate("MainWindow", "n_splits"))
        self.lineEdit_kfold_n_splits.setText(_translate("MainWindow", "10"))
        self.comboBox_kfold_shuffle.setItemText(0, _translate("MainWindow", "False"))
        self.comboBox_kfold_shuffle.setItemText(1, _translate("MainWindow", "True"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_kfold), _translate("MainWindow", "K-fold"))
        self.label_10.setText(_translate("MainWindow", "shuffle"))
        self.lineEdit_stratifiedkfold_n_splits.setText(_translate("MainWindow", "10"))
        self.comboBox_stratifiedkfold_shuffle.setItemText(0, _translate("MainWindow", "False"))
        self.comboBox_stratifiedkfold_shuffle.setItemText(1, _translate("MainWindow", "True"))
        self.label_2.setText(_translate("MainWindow", "n_splits"))
        self.label_9.setText(_translate("MainWindow", "random_state"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_stratifiedkfold), _translate("MainWindow", "Stratified k-fold"))
        self.lineEdit_randomsplits_n_splits.setText(_translate("MainWindow", "10"))
        self.label_6.setText(_translate("MainWindow", "train_size"))
        self.label_3.setText(_translate("MainWindow", "n_splits"))
        self.label_5.setText(_translate("MainWindow", "test_size"))
        self.label_11.setText(_translate("MainWindow", "random_state"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_randomsplit), _translate("MainWindow", "Random splits"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_userdefined), _translate("MainWindow", "User-defined CV"))
        self.groupBox_candidate.setTitle(_translate("MainWindow", "Candidate datasets"))
        self.menuConfiguration_file_F.setTitle(_translate("MainWindow", "Configuration file (&F)"))
        self.menuSkin.setTitle(_translate("MainWindow", "Skin"))
        self.actionLoad_configuration.setText(_translate("MainWindow", "Load configuration"))
        self.actionSave_configuration.setText(_translate("MainWindow", "Save configuration"))
        self.actionDark.setText(_translate("MainWindow", "Dark"))
        self.actionBlack.setText(_translate("MainWindow", "Black"))
        self.actionDarkOrange.setText(_translate("MainWindow", "DarkOrange"))
        self.actionGray.setText(_translate("MainWindow", "Gray"))
        self.actionBlue.setText(_translate("MainWindow", "Blue"))
        self.actionNavy.setText(_translate("MainWindow", "Navy"))
        self.actionClassic.setText(_translate("MainWindow", "Classic"))

