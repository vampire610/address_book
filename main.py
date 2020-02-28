import sys
from PyQt5.QtWidgets import *
import Ui_book
import create
import change

personList = {}


class My_window(QMainWindow, Ui_book.Ui_MainWindow):
    def __init__(self):
        super(My_window, self).__init__()
        self.setupUi(self)

        # 禁止编辑
        self.tabletable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 只能选中一行
        self.tabletable.setSelectionMode(QAbstractItemView.SingleSelection)
        # 选中整行
        self.tabletable.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 第一列不显示
        self.tabletable.verticalHeader().setVisible(False)
        self.display()
        # 信号与槽链接
        self.pushButton_create.clicked.connect(self.save)
        self.pushButton_del.clicked.connect(self.delete)
        self.pushButton_change.clicked.connect(self.change)
        self.pushButton_search.clicked.connect(self.search)

    def display(self):
        personList = create.example.get_data()

        if personList:

            r = len(personList)

            self.tabletable.setRowCount(r)
            i = 0
            num = 1
            for v in personList.values():
                numItem = QTableWidgetItem(str(num))
                self.tabletable.setItem(i, 0, numItem)

                nameItem = QTableWidgetItem(v.name)
                self.tabletable.setItem(i, 1, nameItem)

                telItem = QTableWidgetItem(v.number)
                self.tabletable.setItem(i, 2, telItem)

                emailItem = QTableWidgetItem(v.email)
                self.tabletable.setItem(i, 3, emailItem)
                i += 1
                num += 1
        else:
            self.tabletable.setRowCount(0)
            QMessageBox.warning(self, '提示', '没有读取到联系人，请确认数据文件位置或新建联系人。')

    def save(self):
        dialog = create.My_Dialog(self)
        dialog.Signal_save.connect(self.display)
        dialog.show()

    def delete(self):
        r = self.tabletable.currentRow()
        if r >= 0:
            name = self.tabletable.selectedItems()[1].text()
            r = self.tabletable.selectedItems()[1].row()

            button = QMessageBox.question(self, '确认删除', '确认删除联系人{}吗？'.format(
                name), QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if button == QMessageBox.Yes:
                create.example.delete_person(name)
            else:
                pass
            self.display()
        else:
            QMessageBox.critical(self, 'ERROE', '未选中联系人！')

    def change(self):
        dailog = change.Change_Dialog(self)
        r = self.tabletable.currentRow()
        if r >= 0:
            name = self.tabletable.selectedItems()[1].text()
            tel = self.tabletable.selectedItems()[2].text()
            email = self.tabletable.selectedItems()[3].text()
            dailog.lineEdit_name.setText(name)
            dailog.lineEdit_tel.setText(tel)
            dailog.lineEdit_email.setText(email)

            dailog.Signal_change.connect(self.display)
            dailog.show()
        else:
            QMessageBox.critical(self, 'ERROE', '未选中联系人！')

    def search(self):
        print('search')
        choose = self.comboBox.currentText()
        if choose == '按姓名':
            print('按姓名')
        elif choose == '按电话':
            print('按电话')
        elif choose == '按邮箱':
            print('按邮箱')
        else:
            print('请选择查询方式')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = My_window()

    window.show()
    sys.exit(app.exec_())
