from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import sqlite3

class Ui_Admin(object):
    def setupUi(self, Admin):
        Admin.setObjectName("Admin")
        Admin.resize(550, 500)
        Admin.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Admin)
        self.label.setGeometry(QtCore.QRect(125, 360, 300, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.search_number = QtWidgets.QLineEdit(Admin)
        self.search_number.setGeometry(QtCore.QRect(190, 390, 150, 25))
        self.search_number.setObjectName("search_number")
        self.search_button = QtWidgets.QPushButton(Admin)
        self.search_button.setGeometry(QtCore.QRect(350, 390, 35, 25))
        self.search_button.setStyleSheet("background-color: rgb(75, 136, 216);")
        self.search_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Pics/search (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_button.setIcon(icon)
        self.search_button.setObjectName("search_button")
        self.employers_check = QtWidgets.QPushButton(Admin)
        self.employers_check.setGeometry(QtCore.QRect(200, 100, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.employers_check.setFont(font)
        self.employers_check.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 127);")
        self.employers_check.setObjectName("employers_check")
        self.user_check = QtWidgets.QPushButton(Admin)
        self.user_check.setGeometry(QtCore.QRect(200, 180, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_check.setFont(font)
        self.user_check.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 127);")
        self.user_check.setObjectName("user_check")
        self.pushButton = QtWidgets.QPushButton(Admin)
        self.pushButton.setGeometry(QtCore.QRect(200, 260, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 127);")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Admin)
        QtCore.QMetaObject.connectSlotsByName(Admin)

        self.employers_check.clicked.connect(self.write_employer)
        self.user_check.clicked.connect(self.write_user)
        self.search_button.clicked.connect(self.search)

    def write_employer(self):
        conn = sqlite3.connect('Employers.db')
        cursor = conn.execute("""SELECT * FROM employers""")
        for row in cursor.fetchall():
            print(row)

    def write_user(self):
        conn = sqlite3.connect('Users.db')
        cursor = conn.execute("""SELECT * FROM users""")
        for row in cursor.fetchall():
            print(row)

    def search(self):
        pass

                


    def retranslateUi(self, Admin):
        _translate = QtCore.QCoreApplication.translate
        Admin.setWindowTitle(_translate("Admin", "Technerds Team"))
        Admin.setWindowIcon(QIcon('null.png'))
        self.label.setText(_translate("Admin", "Serching for the costumer number:"))
        self.employers_check.setText(_translate("Admin", "Employers"))
        self.user_check.setText(_translate("Admin", "Users"))
        self.pushButton.setText(_translate("Admin", "Profit"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Admin = QtWidgets.QWidget()
    ui = Ui_Admin()
    ui.setupUi(Admin)
    Admin.show()
    sys.exit(app.exec_())
