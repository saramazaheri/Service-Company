from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import sqlite3
from employers import *


class Ui_remove_service_list(object):
    def setupUi(self, remove_service_list):
        remove_service_list.setObjectName("remove_service_list")
        remove_service_list.resize(354, 450)
        font = QtGui.QFont()
        font.setPointSize(10)
        remove_service_list.setFont(font)
        remove_service_list.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget = QtWidgets.QListWidget(remove_service_list)
        self.listWidget.setGeometry(QtCore.QRect(20, 80, 311, 281))
        self.listWidget.setObjectName("listWidget")
        self.remove_pushButton = QtWidgets.QPushButton(remove_service_list)
        self.remove_pushButton.setGeometry(QtCore.QRect(230, 380, 100, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.remove_pushButton.setFont(font)
        self.remove_pushButton.setStyleSheet("background-color: rgb(0, 0, 127);\n"
        "color: rgb(255, 255, 255);")
        self.remove_pushButton.setObjectName("remove_pushButton")
        self.label = QtWidgets.QLabel(remove_service_list)
        self.label.setGeometry(QtCore.QRect(20, 9, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(remove_service_list)
        self.lineEdit.setGeometry(QtCore.QRect(20, 50, 251, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(remove_service_list)
        self.label_2.setGeometry(QtCore.QRect(20, 380, 201, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(200, 0, 0);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(remove_service_list)
        self.pushButton.setGeometry(QtCore.QRect(280, 50, 51, 28))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(0, 0, 127);")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(remove_service_list)
        QtCore.QMetaObject.connectSlotsByName(remove_service_list)

        self.pushButton.clicked.connect(self.submit)
        self.remove_pushButton.clicked.connect(self.removeitem)

    def submit(self):
        conn= sqlite3.connect("Employers.db")
        c = conn.cursor()
        c.execute("SELECT * FROM service")
        newlist= []
        self.listWidget.clear()
        for row in c.fetchall():
            if row[0]== self.lineEdit.text():
                self.listWidget.addItem(row[1])

    def removeitem(self):
        item= self.listWidget.currentItem()
        self.item= item.text()
        self.listWidget.removeItemWidget(item)
        conn= sqlite3.connect("Employers.db")
        c = conn.cursor()
        c.execute("DELETE FROM service WHERE Services=(?)", (self.item,))
        conn.commit()
        self.submit()
        
    def retranslateUi(self, remove_service_list):
        _translate = QtCore.QCoreApplication.translate
        remove_service_list.setWindowTitle(_translate("remove_service_list", "Form"))
        remove_service_list.setWindowIcon(QIcon('null.png'))
        self.remove_pushButton.setText(_translate("remove_service_list", "Remove"))
        self.label.setText(_translate("remove_service_list", "For security, enter your email:"))
        self.pushButton.setText(_translate("remove_service_list", "Submit"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    remove_service_list = QtWidgets.QWidget()
    ui = Ui_remove_service_list()
    ui.setupUi(remove_service_list)
    remove_service_list.show()
    sys.exit(app.exec_())