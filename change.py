from PyQt5.QtCore import *
from PyQt5.QtWidgets import QDialog, QWidget, QMessageBox

import example
import Ui_change


class Change_Dialog(QDialog, Ui_change.Ui_Dialog_change):
    Signal_change = pyqtSignal()
    def __init__(self, parent=None):
        super(Change_Dialog, self).__init__(parent)
        self.setupUi(self)

        self.buttonBox.accepted.connect(self.change)

    def change(self):
        name = self.lineEdit_name.text()
        tel = self.lineEdit_tel.text()
        email = self.lineEdit_email.text()
        button = QMessageBox.question(self, '修改联系人', '是否将联系人{}的信息修改为：\n电话：{}\n邮箱：{}'.format(name,tel,email),QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
        if button == QMessageBox.Yes:
            example.edit_person(name, tel, email)
        else:
            pass

        self.Signal_change.emit()

