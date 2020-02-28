import Ui_create
import example
from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5.QtCore import *


class My_Dialog(QDialog, Ui_create.Ui_Dialog):
    Signal_save = pyqtSignal()
    def __init__(self, parent=None):
        super(My_Dialog, self).__init__(parent)
        self.setupUi(self)

        self.buttonBox.accepted.connect(self.save)

    def save(self):
        name = self.line_name.text()
        tel = self.line_tel.text()
        email = self.line_email.text()
        example.add_person(name, tel, email)
        #example.show_all()
        self.Signal_save.emit()

