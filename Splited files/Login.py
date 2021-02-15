from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt5.QtGui import QIcon
import csv
import re
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from employers import *
from register import *
from MainMenu import *
from employer_panel import *
from admin import *
from costumer_panel import *

class Ui_Login_Page(object):

    def openmainmeenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Mainpage()
        self.ui.setupUi(self.window)
        self.window.show()

    def openemployer_panel(self,x):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_employer_panel()
        self.ui.setupUi(self.window,self.x)
        self.window.show()

    def openadmin(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Admin()
        self.ui.setupUi(self.window)
        self.window.show()

    def opencostumer_panel(self, y):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_costumer_panel()
        self.ui.setupUi(self.window, self.y)
        self.window.show()


    def setupUi(self, Login_Page):
        Login_Page.setObjectName("Login_Page")
        Login_Page.resize(666, 413)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Minoo/.designer/backup/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Login_Page.setWindowIcon(icon)
        Login_Page.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Login_Page)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 631, 291))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.user_login = QtWidgets.QPushButton(self.tab)
        self.user_login.setGeometry(QtCore.QRect(510, 200, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.user_login.setFont(font)
        self.user_login.setStyleSheet("background-color: rgb(0, 0, 127);\n"
        "color: rgb(255, 255, 255);")
        self.user_login.setObjectName("user_login")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(30, 70, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(70, 120, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.user_info = QtWidgets.QLineEdit(self.tab)
        self.user_info.setGeometry(QtCore.QRect(280, 70, 260, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.user_info.setFont(font)
        self.user_info.setObjectName("user_info")
        self.user_pass = QtWidgets.QLineEdit(self.tab)
        self.user_pass.setGeometry(QtCore.QRect(280, 130, 260, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.user_pass.setFont(font)
        self.user_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.user_pass.setObjectName("user_pass")
        self.user_label = QtWidgets.QLabel(self.tab)
        self.user_label.setGeometry(QtCore.QRect(280, 20, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Simplified Arabic")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.user_label.setFont(font)
        self.user_label.setStyleSheet("font: 10pt \"Simplified Arabic\";\n"
        "color: rgb(197, 0, 0);")
        self.user_label.setText("")
        self.user_label.setAlignment(QtCore.Qt.AlignCenter)
        self.user_label.setObjectName("user_label")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.e_login = QtWidgets.QPushButton(self.tab_2)
        self.e_login.setGeometry(QtCore.QRect(510, 200, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.e_login.setFont(font)
        self.e_login.setStyleSheet("background-color: rgb(0, 0, 127);\n"
        "color: rgb(255, 255, 255);")
        self.e_login.setObjectName("e_login")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(30, 70, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(70, 120, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.e_info = QtWidgets.QLineEdit(self.tab_2)
        self.e_info.setGeometry(QtCore.QRect(280, 70, 260, 40))
        self.e_info.setObjectName("e_info")
        self.e_pass = QtWidgets.QLineEdit(self.tab_2)
        self.e_pass.setGeometry(QtCore.QRect(280, 130, 260, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.e_pass.setFont(font)
        self.e_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.e_pass.setObjectName("e_pass")
        self.employer_login = QtWidgets.QLabel(self.tab_2)
        self.employer_login.setGeometry(QtCore.QRect(280, 20, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Simplified Arabic")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.employer_login.setFont(font)
        self.employer_login.setStyleSheet("font: 10pt \"Simplified Arabic\";\n"
        "color: rgb(197, 0, 0);")
        self.employer_login.setText("")
        self.employer_login.setAlignment(QtCore.Qt.AlignCenter)
        self.employer_login.setObjectName("employer_login")
        self.tabWidget.addTab(self.tab_2, "")
        self.backbutton = QtWidgets.QPushButton(self.centralwidget)
        self.backbutton.setGeometry(QtCore.QRect(220, 320, 240, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.backbutton.setFont(font)
        self.backbutton.setStyleSheet("background-color: rgb(0, 0, 127);\n"
        "color: rgb(255, 255, 255);")
        self.backbutton.setObjectName("backbutton")
        self.backbutton.clicked.connect(self.Back_page)
        self.backbutton.clicked.connect(self.Mainmenu_page)
        Login_Page.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Login_Page)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 666, 26))
        self.menubar.setObjectName("menubar")
        Login_Page.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Login_Page)
        self.statusbar.setObjectName("statusbar")
        Login_Page.setStatusBar(self.statusbar)
        self.retranslateUi(Login_Page)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Login_Page)

        self.Login_Page= Login_Page

        self.user_login.clicked.connect(self.userlogin)
        self.e_login.clicked.connect(self.emplogin)
        self.Login_Page= Login_Page

    def userlogin(self):
        for i in listusers:
                if self.user_info.text() == i.Email:
                        if self.user_pass.text() == i.Password:
                                self.y = self.user_info.text()
                                self.Login_Page.close()
                                self.opencostumer_panel(self.y)
                        else:
                                self.user_label.setText("Your information is incorrect.")
                self.user_label.setText("Your information is incorrect.")

    def emplogin(self):
        if self.e_info.text() == "Technerds.team@gmail.com":
                if self.e_pass.text() == "3tms.team":
                        self.Login_Page.close()
                        self.openadmin()
        else:
                for i in listemployer:
                        if self.e_info.text() == i.email:
                                if self.e_pass.text() == i.password:
                                        self.x = self.e_info.text()
                                        self.Login_Page.close()
                                        self.openemployer_panel(self.x)
                                #employer panel
                        else:
                                self.employer_login.setText("Your information is incorrect.")
                self.employer_login.setText("Your information is incorrect.")

    def Back_page(self):
        Login_Page.close()

    def Mainmenu_page(self):
        self.openmainmeenu()

    def admin_page(self):
        self.openadmin()

    def retranslateUi(self, Login_Page):
        _translate = QtCore.QCoreApplication.translate
        Login_Page.setWindowTitle(_translate("Login_Page", "Login Page"))
        Login_Page.setWindowIcon(QIcon('login.png'))
        self.user_login.setText(_translate("Login_Page", "Login"))
        self.label.setText(_translate("Login_Page", "Email:"))
        self.label_2.setText(_translate("Login_Page", "Password:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Login_Page", "User Login"))
        self.e_login.setText(_translate("Login_Page", "Login"))
        self.label_3.setText(_translate("Login_Page", "Email:"))
        self.label_4.setText(_translate("Login_Page", "Password:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Login_Page", "Employer Login"))
        self.backbutton.setText(_translate("Login_Page", "Back"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login_Page = QtWidgets.QMainWindow()
    ui = Ui_Login_Page()
    ui.setupUi(Login_Page)
    Login_Page.show()
    sys.exit(app.exec_()) 