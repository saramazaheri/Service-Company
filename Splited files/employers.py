# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'employers.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from Services import *
import csv
import re
import sqlite3


class base_empo:
    def __init__(self, name, lastname, email, password, phone, id, birth_place, city, education, gender, unemployed, emergency, point, income):
        self.name = name
        self.lastname= lastname
        self.email= email
        self.password= password
        self.phone= int(phone)
        self.id= int(id)
        self.birth_place= birth_place
        self.city= city
        self.education= education
        self.gender= gender
        self.unemployed= unemployed
        self.emergency= int(emergency)
        self.point= point
        self.income= income

        def getname(self):
            return self.name and self.lastname

        def getemail(self):
            return self.email

        def getpass(self):
            return self.password    
            
        def getphone(self):
            return self.phone

        def get_id(self):
            return self.id

        def get_education(self):
            return self.education

        def get_gender(self):
            return self.gender

        def getpoint(self):
            return self.point

        def get_income(self):
            return self.income


conn = sqlite3.connect('Employers.db')
cursor = conn.execute("""SELECT Name, Last_Name, Email,Password,Phone_number, ID, Birth_Place, City, Education, Gender,
Unemployed, Emergency_Number from employers""")
cc=cursor.fetchall()
listemployer= []
for i in range(len(cc)):
   listemployer.append(base_empo(str(cc[i][0]),str(cc[i][1]),str(cc[i][2]),str(cc[i][3]),int(cc[i][4]),int(cc[i][5]),str(cc[i][6]),
   str(cc[i][7]),str(cc[i][8]),str(cc[i][9]),str(cc[i][10]),int(cc[i][11]), 0, 0))

class Ui_employers(object):
    def openservices(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Services()
        self.ui.setupUi(self.window)
        self.window.show()
        self.employers.close()

    def setupUi(self, employers):
        self.fn, self.ln, self.eml, self.pw, self.mn, self.mpw = False, False, False, False, False, False
        employers.setObjectName("employers")
        employers.resize(908, 856)
        employers.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(employers)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 20, 601, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 80, 801, 541))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.password = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 2, 1, 1, 1)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 4, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 3, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 2, 1, 1)
        self.birthcombo = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.birthcombo.setFont(font)
        self.birthcombo.setObjectName("birthcombo")
        self.birthcombo.addItem("")
        self.birthcombo.addItem("")
        self.birthcombo.addItem("")
        self.birthcombo.addItem("")
        self.birthcombo.addItem("")
        self.birthcombo.addItem("")
        self.birthcombo.addItem("")
        self.birthcombo.addItem("")
        self.birthcombo.addItem("")
        self.birthcombo.addItem("")
        self.birthcombo.addItem("")
        self.birthcombo.addItem("")
        self.birthcombo.addItem("")
        self.birthcombo.addItem("")
        self.birthcombo.addItem("")
        self.birthcombo.addItem("")
        self.birthcombo.addItem("")
        self.birthcombo.addItem("")
        self.birthcombo.addItem("")
        self.birthcombo.addItem("")
        self.birthcombo.addItem("")
        self.birthcombo.addItem("")
        self.birthcombo.addItem("")
        self.birthcombo.addItem("")
        self.birthcombo.addItem("")
        self.birthcombo.addItem("")
        self.birthcombo.addItem("")
        self.birthcombo.addItem("")
        self.birthcombo.addItem("")
        self.birthcombo.addItem("")
        self.birthcombo.addItem("")
        self.birthcombo.setCurrentIndex(27)
        self.gridLayout.addWidget(self.birthcombo, 3, 1, 1, 1)
        self.id = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.id.setObjectName("id")
        self.gridLayout.addWidget(self.id, 1, 3, 1, 1)
        self.email = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.email.setObjectName("email")
        self.gridLayout.addWidget(self.email, 1, 1, 1, 1)
        self.education = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.education.setObjectName("education")
        self.gridLayout.addWidget(self.education, 4, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        self.confirm = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.confirm.setObjectName("confirm")
        self.confirm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout.addWidget(self.confirm, 2, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 2, 1, 1)
        self.city = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.city.setObjectName("city")
        self.gridLayout.addWidget(self.city, 3, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 0, 1, 1, 1)
        self.lastname = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lastname.setObjectName("lastname")
        self.gridLayout.addWidget(self.lastname, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 7, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.emergency = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.emergency.setObjectName("emergency")
        self.gridLayout.addWidget(self.emergency, 6, 3, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 6, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 8, 0, 1, 1)
        self.unemployedcombo = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.unemployedcombo.setFont(font)
        self.unemployedcombo.setObjectName("unemployedcombo")
        self.unemployedcombo.addItem("")
        self.unemployedcombo.addItem("")
        self.gridLayout.addWidget(self.unemployedcombo, 8, 1, 1, 1)
        self.address = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.address.setObjectName("address")
        self.gridLayout.addWidget(self.address, 7, 1, 1, 3)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 6, 0, 1, 1)
        self.phone = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.phone.setObjectName("phone")
        self.gridLayout.addWidget(self.phone, 6, 1, 1, 1)
        self.male = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.male.setObjectName("male")
        self.gridLayout.addWidget(self.male, 5, 2, 1, 1)
        self.female = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.female.setObjectName("female")
        self.gridLayout.addWidget(self.female, 5, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 5, 0, 1, 1)
        self.other = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.other.setObjectName("other")
        self.gridLayout.addWidget(self.other, 5, 3, 1, 1)
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(750, 720, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.next.setFont(font)
        self.next.setStyleSheet("background-color: rgb(0, 0, 127);\n"
        "color: rgb(255, 255, 255);")
        self.next.setObjectName("next")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(60, 630, 691, 171))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.mailerror = QtWidgets.QLabel(self.frame)
        self.mailerror.setText("")
        self.mailerror.setAlignment(QtCore.Qt.AlignCenter)
        self.mailerror.setObjectName("mailerror")
        self.gridLayout_2.addWidget(self.mailerror, 0, 1, 1, 1)
        self.passerror = QtWidgets.QLabel(self.frame)
        self.passerror.setText("")
        self.passerror.setObjectName("passerror")
        self.gridLayout_2.addWidget(self.passerror, 1, 0, 1, 1)
        self.nameerror = QtWidgets.QLabel(self.frame)
        self.nameerror.setText("")
        self.nameerror.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.nameerror.setObjectName("nameerror")
        self.gridLayout_2.addWidget(self.nameerror, 0, 0, 1, 1)
        self.numbererror = QtWidgets.QLabel(self.frame)
        self.numbererror.setText("")
        self.numbererror.setObjectName("numbererror")
        self.gridLayout_2.addWidget(self.numbererror, 0, 2, 1, 1)
        self.notmatch = QtWidgets.QLabel(self.frame)
        self.notmatch.setText("")
        self.notmatch.setObjectName("notmatch")
        self.gridLayout_2.addWidget(self.notmatch, 1, 1, 1, 1)
        self.emptyerror = QtWidgets.QLabel(self.frame)
        self.emptyerror.setText("")
        self.emptyerror.setObjectName("emptyerror")
        self.gridLayout_2.addWidget(self.emptyerror, 1, 2, 1, 1)
        employers.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(employers)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 908, 26))
        self.menubar.setObjectName("menubar")
        employers.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(employers)
        self.statusbar.setObjectName("statusbar")
        employers.setStatusBar(self.statusbar)

        self.retranslateUi(employers)
        QtCore.QMetaObject.connectSlotsByName(employers)

        self.employers = employers

        self.next.clicked.connect(self.names)
        self.next.clicked.connect(self.correct_email)
        self.next.clicked.connect(self.Numbers)
        self.next.clicked.connect(self.correct_pass)
        self.next.clicked.connect(self.confirmation)
        self.next.clicked.connect(self.Next)


    #Names should not contain anything but letters
    def names(self):
        n= self.name.text()
        l= self.lastname.text()
        e= self.education.text()
        f_name= re.search(r'^[A-Za-z]{2,}$', n)
        l_name= re.search(r'^[A-Za-z]{2,}$', l)
        edu= re.search(r'\D+', e)
        if f_name == None or l_name == None or edu== None:
            self.nameerror.setText("First or Last name and Education field\ncan only contain letters.")
        else:
            self.nameerror.setText("")
            self.fn , self.ln = True , True 

    def correct_email(self):
        mail = self.email.text()
        # regex code for right email
        cm = re.search(r'\w.+\w+@[\w]+\..{2,4}', mail)
        if cm == None:
            self.mailerror.setText("Your Email is invalid.")
        else:
            self.mailerror.setText("")
            self.eml = True
    
    #Mobile numbers should contain 11 digits
    def Numbers(self):
        num= self.phone.text()
        m_num= re.search(r'^09\d{9}$', num)
        check_id= self.id.text()
        checker= re.search(r'\d+', check_id)
        if m_num== None or checker== None:
            self.numbererror.setText("ID\Phone number can\nonly contain digits.")
        elif m_num!= None and checker!= None:
            self.numbererror.setText("")
            self.mn = True

    # checking if the password contains what its needed(at least 1 lower case, 1 Capital, 1 number. Between 8 - 16.)
    def  correct_pass(self):
        code = self.password.text()
        # regex code for right password
        cp = re.search(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,16}$', code)
        if cp == None:
            self.passerror.setText("Password:\nMinimum eight characters, "
            "\nat least one uppercase letter, \none lowercase letter and one number.")
        else:
            self.passerror.setText("")
            self.pw = True
    
    # checking if two passwords match
    def confirmation(self):
        if self.password.text() != self.confirm.text():
            self.notmatch.setText("             Passwords don't match.")

        else:
            self.notmatch.setText("")
            self.mpw = True
        
    #if everything was right, save everything and go to the next step.
    def Next(self):
        if self.fn == True and self.ln == True and self.eml == True and self.pw == True and self.mn == True and self.mpw== True:
            if self.female.isChecked():
                btn = self.female.text()
            if self.male.isChecked():
                btn = self.male.text()
            if self.other.isChecked():
                btn = self.other.text()
            conn= sqlite3.connect("Employers.db")
            c = conn.cursor()
            d = conn.cursor()
            # Create table
            # c.execute('''CREATE TABLE employers
            # (Name text, Last_Name text, Email text, Password text, Phone_Number integer, ID integer, Birth_Place text,
            # City text, Education text, Gender text, Unemployed text, Emergency_Number integer )''')
            
            # c.execute('''CREATE TABLE points_and_income
            # (Name text, Last_Name text, Phone_Number integer, ID integer, Points integer, Income integer )''')

            v= [self.name.text(), self.lastname.text() , self.email.text() , self.password.text() , self.phone.text() , self.id.text(),
            self.birthcombo.currentText() , self.city.text() , self.education.text() , btn, self.unemployedcombo.currentText(), self.emergency.text()]

            c.execute("""
                INSERT INTO employers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            """, v)

            pi = [self.name.text(), self.lastname.text(), self.phone.text() , self.id.text(), self.email.text(), self.education.text(), btn, 0, 0]
            d.execute("INSERT INTO points_and_income VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?) ;", pi)

            conn.commit()

            listemployer.append(base_empo(self.name.text(), self.lastname.text() , self.email.text() , self.password.text() , self.phone.text() , self.id.text(),
            self.birthcombo.currentText() , self.city.text() , self.education.text() , btn, self.unemployedcombo.currentText(), self.emergency.text(), 0, 0))
            
            self.services_page()
            
    def services_page(self):
        self.openservices()

    def retranslateUi(self, employers):
        _translate = QtCore.QCoreApplication.translate
        employers.setWindowTitle(_translate("employers", "Employers Registration"))
        self.label.setText(_translate("employers", "Registration Form For Employers"))
        self.label_6.setText(_translate("employers", "Confirm Password:"))
        self.label_16.setText(_translate("employers", "City You Live In:"))
        self.label_10.setText(_translate("employers", "ID:"))
        self.birthcombo.setItemText(0, _translate("employers", "Alborz"))
        self.birthcombo.setItemText(1, _translate("employers", "Ardabil"))
        self.birthcombo.setItemText(2, _translate("employers", "Bushehr"))
        self.birthcombo.setItemText(3, _translate("employers", "Chaharmahal and Bakhtiari"))
        self.birthcombo.setItemText(4, _translate("employers", "East Azarbaijan"))
        self.birthcombo.setItemText(5, _translate("employers", "Fars"))
        self.birthcombo.setItemText(6, _translate("employers", "Guilan"))
        self.birthcombo.setItemText(7, _translate("employers", "Golestan"))
        self.birthcombo.setItemText(8, _translate("employers", "Hamedan"))
        self.birthcombo.setItemText(9, _translate("employers", "Hormozgan"))
        self.birthcombo.setItemText(10, _translate("employers", "Ilam"))
        self.birthcombo.setItemText(11, _translate("employers", "Isfahan"))
        self.birthcombo.setItemText(12, _translate("employers", "Kerman"))
        self.birthcombo.setItemText(13, _translate("employers", "Kermanshah"))
        self.birthcombo.setItemText(14, _translate("employers", "Khuzestan"))
        self.birthcombo.setItemText(15, _translate("employers", "Kohgiluyeh and Boyer-Ahmad"))
        self.birthcombo.setItemText(16, _translate("employers", "Kurdestan"))
        self.birthcombo.setItemText(17, _translate("employers", "Lorestan"))
        self.birthcombo.setItemText(18, _translate("employers", "Markazi"))
        self.birthcombo.setItemText(19, _translate("employers", "Mazandaran"))
        self.birthcombo.setItemText(20, _translate("employers", "North Khorasan"))
        self.birthcombo.setItemText(21, _translate("employers", "Qazvin"))
        self.birthcombo.setItemText(22, _translate("employers", "Qom"))
        self.birthcombo.setItemText(23, _translate("employers", "Razavi Khorasan"))
        self.birthcombo.setItemText(24, _translate("employers", "Semnan"))
        self.birthcombo.setItemText(25, _translate("employers", "Sistan and Baluchestan"))
        self.birthcombo.setItemText(26, _translate("employers", "South Khorasan"))
        self.birthcombo.setItemText(27, _translate("employers", "Tehran"))
        self.birthcombo.setItemText(28, _translate("employers", "West Azarbaijan"))
        self.birthcombo.setItemText(29, _translate("employers", "Yazd"))
        self.birthcombo.setItemText(30, _translate("employers", "Zanjan"))
        self.label_8.setText(_translate("employers", "Date Of Birth:"))
        self.label_9.setText(_translate("employers", "Education(Major):"))
        self.label_3.setText(_translate("employers", "Last Name:"))
        self.label_7.setText(_translate("employers", "Birth Place:"))
        self.label_4.setText(_translate("employers", "Email:"))
        self.label_14.setText(_translate("employers", "Address:"))
        self.label_2.setText(_translate("employers", "First Name:"))
        self.label_13.setText(_translate("employers", "Emergengy Phone Call:"))
        self.label_15.setText(_translate("employers", "Are you currently Unemployed?"))
        self.unemployedcombo.setItemText(0, _translate("employers", "Yes"))
        self.unemployedcombo.setItemText(1, _translate("employers", "No"))
        self.label_12.setText(_translate("employers", "Phone Number:"))
        self.male.setText(_translate("employers", "Male"))
        self.female.setText(_translate("employers", "Female"))
        self.label_5.setText(_translate("employers", "Password:"))
        self.label_11.setText(_translate("employers", "Gender:"))
        self.other.setText(_translate("employers", "Other"))
        self.next.setText(_translate("employers", "Next"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    employers = QtWidgets.QMainWindow()
    ui = Ui_employers()
    ui.setupUi(employers)
    employers.show()
    sys.exit(app.exec_())
