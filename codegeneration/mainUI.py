# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 581)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 761, 521))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.cBox_mode = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.cBox_mode.setObjectName("cBox_mode")
        self.cBox_mode.addItem("")
        self.cBox_mode.addItem("")
        self.cBox_mode.addItem("")
        self.gridLayout.addWidget(self.cBox_mode, 2, 1, 1, 1)
        self.pushButton_clear = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.gridLayout.addWidget(self.pushButton_clear, 4, 1, 1, 1)
        self.label_mode = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_mode.setObjectName("label_mode")
        self.gridLayout.addWidget(self.label_mode, 2, 0, 1, 1)
        self.label_data = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_data.setObjectName("label_data")
        self.gridLayout.addWidget(self.label_data, 5, 0, 1, 4)
        self.label_packagename = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_packagename.setObjectName("label_packagename")
        self.gridLayout.addWidget(self.label_packagename, 2, 2, 1, 1)
        self.lineEdit_packagename = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_packagename.setObjectName("lineEdit_packagename")
        self.gridLayout.addWidget(self.lineEdit_packagename, 2, 3, 1, 1)
        self.textEdit_data = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_data.setObjectName("textEdit_data")
        self.gridLayout.addWidget(self.textEdit_data, 6, 0, 1, 4)
        self.pushButton_OK = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_OK.setObjectName("pushButton_OK")
        self.gridLayout.addWidget(self.pushButton_OK, 4, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "自动生成代码"))
        self.cBox_mode.setItemText(0, _translate("MainWindow", "生成mapper"))
        self.cBox_mode.setItemText(1, _translate("MainWindow", "生成typehandler"))
        self.cBox_mode.setItemText(2, _translate("MainWindow", "生成pojo类"))
        self.pushButton_clear.setText(_translate("MainWindow", "清空"))
        self.label_mode.setText(_translate("MainWindow", "模式："))
        self.label_data.setText(_translate("MainWindow", "要生成的PROCEDURE或者TYPE代码等原数据："))
        self.label_packagename.setText(_translate("MainWindow", "包名："))
        self.pushButton_OK.setText(_translate("MainWindow", "生成"))

