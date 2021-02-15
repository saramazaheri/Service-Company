# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confirmation.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from employers import *


class Ui_Sure(object):
    def setupUi(self, Sure):
        self.P, self.S, self.E, self.D= False, False, False, False
        Sure.setObjectName("Sure")
        Sure.resize(500, 350)
        font = QtGui.QFont()
        font.setPointSize(12)
        Sure.setFont(font)
        Sure.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Sure)
        self.label.setGeometry(QtCore.QRect(40, 20, 441, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Sure)
        self.label_2.setGeometry(QtCore.QRect(30, 130, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(Sure)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 280, 121, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(0, 0, 127);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.confirm_email_box = QtWidgets.QLineEdit(Sure)
        self.confirm_email_box.setGeometry(QtCore.QRect(140, 140, 300, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.confirm_email_box.setFont(font)
        self.confirm_email_box.setInputMethodHints(QtCore.Qt.ImhNone)
        self.confirm_email_box.setObjectName("confirm_email_box")
        self.passwordconfirmation = QtWidgets.QLineEdit(Sure)
        self.passwordconfirmation.setGeometry(QtCore.QRect(140, 200, 300, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.passwordconfirmation.setFont(font)
        self.passwordconfirmation.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.passwordconfirmation.setObjectName("passwordconfirmation")
        self.label_3 = QtWidgets.QLabel(Sure)
        self.label_3.setGeometry(QtCore.QRect(30, 190, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.error = QtWidgets.QLabel(Sure)
        self.error.setGeometry(QtCore.QRect(140, 240, 271, 31))
        self.error.setStyleSheet("color: rgb(218, 0, 0);")
        self.error.setText("")
        self.error.setObjectName("error")

        self.retranslateUi(Sure)
        QtCore.QMetaObject.connectSlotsByName(Sure)

        self.pushButton_3.clicked.connect(self.deleted)

    def deleted(self):
        self.detail_delete()
        self.point_delete()
        self.service_delete()
        self.emp_delete()
        if self.D==True and self.P==True and self.S==True and self.E==True:
            Sure.close()

    def emp_delete(self):
        conn= sqlite3.connect("Employers.db")
        c = conn.cursor()

        for i in listemployer:
                if self.confirm_email_box.text()== i.email:
                        if self.passwordconfirmation.text()== i.password:
                            c.execute("DELETE FROM employers WHERE Email=(?)", (i.email,))
                            self.E= True
                        else:
                            self.error.setText("Your information is incorrect.\nWe can not delete your account.")
                else:
                    self.error.setText("Your information is incorrect.\nWe can not delete your account.")
        
        conn.commit()

    def point_delete(self):
        conn= sqlite3.connect("Employers.db")
        c = conn.cursor()

        for i in listemployer:
                if self.confirm_email_box.text()== i.email:
                        if self.passwordconfirmation.text()== i.password:
                            c.execute("DELETE FROM points_and_income WHERE ID=(?)", (i.id,))
                            self.P= True
                        else:
                            self.error.setText("Your information is incorrect.\nWe can not delete your account.")
                else:
                    self.error.setText("Your information is incorrect.\nWe can not delete your account.")

    def service_delete(self):
        conn= sqlite3.connect("Employers.db")
        c = conn.cursor()

        for i in listemployer:
                if self.confirm_email_box.text()== i.email:
                        if self.passwordconfirmation.text()== i.password:
                            c.execute("DELETE FROM service WHERE Name=(?)", (i.email,))
                            self.S= True
                        else:
                            self.error.setText("Your information is incorrect.\nWe can not delete your account.")
                else:
                    self.error.setText("Your information is incorrect.\nWe can not delete your account.")

        conn.commit()

    def detail_delete(self):
        conn= sqlite3.connect("Employers.db")
        c = conn.cursor()

        for i in listemployer:
                if self.confirm_email_box.text()== i.email:
                        if self.passwordconfirmation.text()== i.password:
                            c.execute("DELETE FROM details WHERE Name=(?)", (i.email,))
                            self.D= True
                        else:
                            self.error.setText("Your information is incorrect.\nWe can not delete your account.")
                else:
                    self.error.setText("Your information is incorrect.\nWe can not delete your account.")

        conn.commit()

    def retranslateUi(self, Sure):
        _translate = QtCore.QCoreApplication.translate
        Sure.setWindowTitle(_translate("Sure", "Are you sure?"))
        self.label.setText(_translate("Sure", "To be sure it\'s you again,\n"
        "please enter you email and password.\n"
        "Your account will be deleted afterward\n"
        "and can NOT be active again.."))
        self.label_2.setText(_translate("Sure", "Email:"))
        self.pushButton_3.setText(_translate("Sure", "Delete Account"))
        self.label_3.setText(_translate("Sure", "Password:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Sure = QtWidgets.QWidget()
    ui = Ui_Sure()
    ui.setupUi(Sure)
    Sure.show()
    sys.exit(app.exec_())
