from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from Services_User import *
from userFinance import *
import sqlite3

class Ui_costumer_panel(object):
    def setupUi(self, costumer_panel, username):
        self.username = username
        costumer_panel.setObjectName("costumer_panel")
        costumer_panel.resize(550, 500)
        self.verticalLayout = QtWidgets.QVBoxLayout(costumer_panel)
        self.verticalLayout.setObjectName("verticalLayout")
        self.request_service = QtWidgets.QPushButton(costumer_panel)
        self.request_service.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
        "color: rgb(255, 255, 255);\n"
        "background-color: rgb(0, 0, 127);")
        self.request_service.setObjectName("request_service")
        self.verticalLayout.addWidget(self.request_service)
        self.finances_button = QtWidgets.QPushButton(costumer_panel)
        self.finances_button.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
        "color: rgb(255, 255, 255);\n"
        "background-color: rgb(0, 0, 127);")
        self.finances_button.setObjectName("finances_button")
        self.verticalLayout.addWidget(self.finances_button)
        self.get_number = QtWidgets.QPushButton(costumer_panel)
        self.get_number.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
        "color: rgb(255, 255, 255);\n"
        "background-color: rgb(0, 0, 127);")
        self.get_number.setObjectName("get_number")
        self.verticalLayout.addWidget(self.get_number)

        self.retranslateUi(costumer_panel)
        QtCore.QMetaObject.connectSlotsByName(costumer_panel)

        self.finances_button.clicked.connect(self.finances)
        self.request_service.clicked.connect(self.Req)
        self.get_number.clicked.connect(self.ReqCN)

    def Req(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ServiceUsers()
        self.ui.setupUi(self.window, self.username)
        self.window.show()

    def finances(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_userFinances()
        self.ui.setupUi(self.window, self.username)
        self.window.show()

    def ReqCN(self):
        cnt = sqlite3.connect('Users.db')
        c = cnt.cursor()
        c.execute(""" 
                 SELECT Customer_Number from CustomerN""")
        newlist = []
        for row in c.fetchall():
            newlist.append(row)
        cn = int(newlist[-1][0])+1
        cnn = sqlite3.connect('Users.db')
        cc = cnn.cursor()
        cc.execute("""
                    SELECT Name , Last_Name , Phone_Number FROM users WHERE Email =(?);""", (self.username,))
        newCN = []
        for row in cc.fetchall():
            newCN.append(row)
        cnn1 = sqlite3.connect('Users.db')
        cc1 = cnn1.cursor()
        cc1.execute("""
                    INSERT INTO CustomerN values (?,?,?,?,?);""" ,(newCN[0][0],newCN[0][1],self.username,newCN[0][2],cn,))

        # cnt.commit()
        cnn1.commit()
    
        msg = QMessageBox()
        msg.setWindowTitle("Customer Number:")
        msg.setIcon(QMessageBox.Information)
        msg.setText(f"This is your Customer Number: {cn}")
        msg.setInformativeText("Thanks for registration")
        msg.setStandardButtons(QMessageBox.Close)

        x = msg.exec_()

    def retranslateUi(self, costumer_panel):
        _translate = QtCore.QCoreApplication.translate
        costumer_panel.setWindowTitle(_translate("costumer_panel", "Costumer Panel"))
        costumer_panel.setWindowIcon(QIcon('null.png'))
        self.request_service.setText(_translate("costumer_panel", "Request For A Service"))
        self.finances_button.setText(_translate("costumer_panel", "Finances"))
        self.get_number.setText(_translate("costumer_panel", "Request For A Costumer Number"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    costumer_panel = QtWidgets.QWidget()
    ui = Ui_costumer_panel()
    ui.setupUi(costumer_panel, 'None')
    costumer_panel.show()
    sys.exit(app.exec_())
