# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\vampi\Desktop\dressbook\book.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(445, 457)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\vampi\\Desktop\\dressbook\\address-book.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton_search = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_search.setObjectName("pushButton_search")
        self.horizontalLayout.addWidget(self.pushButton_search)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 7)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabletable = QtWidgets.QTableWidget(self.centralwidget)
        self.tabletable.setObjectName("tabletable")
        self.tabletable.setColumnCount(4)
        self.tabletable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabletable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabletable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabletable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabletable.setHorizontalHeaderItem(3, item)
        self.tabletable.horizontalHeader().setStretchLastSection(True)
        self.tabletable.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tabletable)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_create = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create.setObjectName("pushButton_create")
        self.horizontalLayout_2.addWidget(self.pushButton_create)
        self.pushButton_change = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_change.setObjectName("pushButton_change")
        self.horizontalLayout_2.addWidget(self.pushButton_change)
        self.pushButton_del = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_del.setObjectName("pushButton_del")
        self.horizontalLayout_2.addWidget(self.pushButton_del)
        self.pushButton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.horizontalLayout_2.addWidget(self.pushButton_exit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actioncreate = QtWidgets.QAction(MainWindow)
        self.actioncreate.setObjectName("actioncreate")
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")

        self.retranslateUi(MainWindow)
        self.pushButton_exit.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "电话簿"))
        self.label.setText(_translate("MainWindow", "电话簿"))
        self.label_2.setText(_translate("MainWindow", "请输入查询信息"))
        self.pushButton_search.setText(_translate("MainWindow", "搜索"))
        self.tabletable.setSortingEnabled(False)
        item = self.tabletable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "序号"))
        item = self.tabletable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.tabletable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "电话"))
        item = self.tabletable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "邮箱"))
        self.pushButton_create.setText(_translate("MainWindow", "新建联系人"))
        self.pushButton_change.setText(_translate("MainWindow", "修改信息"))
        self.pushButton_del.setText(_translate("MainWindow", "删除选中联系人"))
        self.pushButton_exit.setText(_translate("MainWindow", "退出程序"))
        self.actioncreate.setText(_translate("MainWindow", "新建联系人"))
        self.actionexit.setText(_translate("MainWindow", "退出"))
