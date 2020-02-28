# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\vampi\Desktop\dressbook\change.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_change(object):
    def setupUi(self, Dialog_change):
        Dialog_change.setObjectName("Dialog_change")
        Dialog_change.resize(250, 176)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog_change)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog_change)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_name = QtWidgets.QLineEdit(Dialog_change)
        self.lineEdit_name.setReadOnly(True)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.horizontalLayout.addWidget(self.lineEdit_name)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog_change)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_tel = QtWidgets.QLineEdit(Dialog_change)
        self.lineEdit_tel.setObjectName("lineEdit_tel")
        self.horizontalLayout_2.addWidget(self.lineEdit_tel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Dialog_change)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_email = QtWidgets.QLineEdit(Dialog_change)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.horizontalLayout_3.addWidget(self.lineEdit_email)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_change)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog_change)
        self.buttonBox.accepted.connect(Dialog_change.accept)
        self.buttonBox.rejected.connect(Dialog_change.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_change)

    def retranslateUi(self, Dialog_change):
        _translate = QtCore.QCoreApplication.translate
        Dialog_change.setWindowTitle(_translate("Dialog_change", "修改联系人"))
        self.label.setText(_translate("Dialog_change", "姓名"))
        self.label_2.setText(_translate("Dialog_change", "电话"))
        self.label_3.setText(_translate("Dialog_change", "邮箱"))
