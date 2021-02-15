from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt5.QtGui import QIcon
import csv
import re
import sqlite3
from PyQt5.QtWidgets import QMessageBox

class base_user():
    def __init__(self,Name,Last_Name,Email,Password,Phone_Number,Gender):
        self.Name = Name
        self.Last_Name = Last_Name
        self.Email = Email
        self.Password = Password
        self.Phone_Number = int(Phone_Number)
        self.Gender = Gender

    def get_name(self):
        return self.Name and self.Last_Name

    def getemail(self):
        return self.getemail

    def getpass(self):
        return self.getpass

    def getphone(self):
        return self.Phone_Number

    def getgender(self):
        return self.Gender

conn = sqlite3.connect("Users.db")
c = conn.cursor()
c.execute("""SELECT Name, Last_Name, Email,Password,
 Phone_number,Gender from users """)
cc=c.fetchall()
listusers= []
for i in range(len(cc)):
   listusers.append(base_user(str(cc[i][0]),str(cc[i][1]),str(cc[i][2]),str(cc[i][3]),int(cc[i][4]),str(cc[i][5])))




class RF_Form(object):
    
    def setupUi(self, Registration):
        self.fn, self.ln, self.eml, self.pw, self.mn = False, False, False, False, False, 
        Registration.setObjectName("Registration")
        Registration.resize(1045, 860)
        Registration.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Registration)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, -20, 581, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.done = QtWidgets.QPushButton(self.centralwidget)
        self.done.setGeometry(QtCore.QRect(840, 610, 171, 51))
        self.done.setStyleSheet("background-color : rgb(0,0,127);\n"
        "color : rgb(129,201,255);\n"
        "font : 75 14pt \"2 Bardiya\";")
        self.done.setObjectName("Done")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.done.clicked.connect(self.correct_email)
        self.done.clicked.connect(self.correct_pass)
        self.done.clicked.connect(self.confirmation)
        self.done.clicked.connect(self.names)
        self.done.clicked.connect(self.mobile_num)
        self.done.clicked.connect(self.Done)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 70, 321, 521))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(399, 79, 611, 271))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.firstname = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.firstname.setFrame(True)
        self.firstname.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.firstname.setReadOnly(False)
        self.firstname.setObjectName("firstname")
        self.verticalLayout.addWidget(self.firstname)
        self.lastname = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lastname.setObjectName("lastname")
        self.verticalLayout.addWidget(self.lastname)
        self.email = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.email.setObjectName("email")
        self.verticalLayout.addWidget(self.email)
        self.password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.verticalLayout.addWidget(self.password)
        self.confirmpassword = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.confirmpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpassword.setObjectName("confirmpassword")
        self.verticalLayout.addWidget(self.confirmpassword)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(400, 350, 611, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout.addWidget(self.radioButton_3)
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(399, 410, 611, 121))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.dateEdit = QtWidgets.QDateEdit(self.verticalLayoutWidget_3)
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout_3.addWidget(self.dateEdit)
        self.mobile = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.mobile.setObjectName("mobile")
        self.verticalLayout_3.addWidget(self.mobile)
        self.address = QtWidgets.QTextEdit(self.centralwidget)
        self.address.setGeometry(QtCore.QRect(400, 530, 611, 71))
        self.address.setObjectName("address")
        self.mail_error = QtWidgets.QLabel(self.centralwidget)
        self.mail_error.setGeometry(QtCore.QRect(30, 610, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setUnderline(True)
        self.mail_error.setFont(font)
        self.mail_error.setText("")
        self.mail_error.setAlignment(QtCore.Qt.AlignCenter)
        self.mail_error.setObjectName("mail_error")
        self.pass_error = QtWidgets.QLabel(self.centralwidget)
        self.pass_error.setGeometry(QtCore.QRect(320, 610, 261, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setUnderline(True)
        self.pass_error.setFont(font)
        self.pass_error.setText("")
        self.pass_error.setObjectName("pass_error")
        self.confirm_error = QtWidgets.QLabel(self.centralwidget)
        self.confirm_error.setGeometry(QtCore.QRect(610, 610, 261, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setUnderline(True)
        self.confirm_error.setFont(font)
        self.confirm_error.setText("")
        self.confirm_error.setObjectName("confirm_error")
        self.name_error = QtWidgets.QLabel(self.centralwidget)
        self.name_error.setGeometry(QtCore.QRect(30, 710, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setUnderline(True)
        self.name_error.setFont(font)
        self.name_error.setText("")
        self.name_error.setObjectName("name_error")
        self.mobile_error = QtWidgets.QLabel(self.centralwidget)
        self.mobile_error.setGeometry(QtCore.QRect(260, 710, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setUnderline(True)
        self.mobile_error.setFont(font)
        self.mobile_error.setText("")
        self.mobile_error.setObjectName("mobile_error")
        Registration.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Registration)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1043, 31))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuContanct = QtWidgets.QMenu(self.menubar)
        self.menuContanct.setObjectName("menuContanct")
        Registration.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Registration)
        self.statusbar.setObjectName("statusbar")
        Registration.setStatusBar(self.statusbar)
        self.actionUs = QtWidgets.QAction(Registration)
        self.actionUs.setObjectName("actionUs")
        self.actionThis_App = QtWidgets.QAction(Registration)
        self.actionThis_App.setObjectName("actionThis_App")
        self.actionVia_E_mail = QtWidgets.QAction(Registration)
        self.actionVia_E_mail.setObjectName("actionVia_E_mail")
        self.menuAbout.addAction(self.actionUs)
        self.menuAbout.addAction(self.actionThis_App)
        self.menuContanct.addAction(self.actionVia_E_mail)
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuContanct.menuAction())

        self.retranslateUi(Registration)
        QtCore.QMetaObject.connectSlotsByName(Registration)

        self.Registration = Registration
    

    # checking if the email is correct or not with regext
    def correct_email(self):
        mail = self.email.text()
        # regex code for right email
        cm = re.search(r'\w.+\w+@[\w]+\..{2,4}', mail)
        if cm == None:
            self.mail_error.setText("Your Email is invalid.\nPlease enter a correct email")
        else:
            self.mail_error.setText("")
            self.eml = True
            


# checking if the password contains what its needed(at least 1 lower case, 1 Capital, 1 number. Between 8 - 16.)

    def  correct_pass(self):
        code = self.password.text()
        # regex code for right password
        cp = re.search(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,16}$', code)
        if cp == None:
            self.pass_error.setText("Your password must contain \nminimum eight characters,\n"
            "at least one uppercase letter,\none lowercase letter\nand one number.")
        else:
            self.pass_error.setText("")
            self.pw = True
    
    # checking if two passwords match
    def confirmation(self):
        if self.password.text() != self.confirmpassword.text():
            self.confirm_error.setText("Your Passwords don't match.")
        else:
            self.confirm_error.setText("")


#Names should not contain anything but letters
    def names(self):
        n= self.firstname.text()
        l= self.lastname.text()
        f_name= re.search(r'^[A-Za-z]{2,}$', n)
        l_name= re.search(r'^[A-Za-z]{2,}$', l)
        if f_name == None or l_name == None:
            self.name_error.setText("First or Last name\ncan't contain anything\nbut letters.")
        else:
            self.name_error.setText("")
            self.fn , self.ln = True , True 
    
 #Mobile numbers should contain 11 digits
    def mobile_num(self):
        num= self.mobile.text()
        m_num= re.search(r'^09\d{9}$', num)
        if m_num== None:
            self.mobile_error.setText("Mobile Number only contains\n11 digits.")
        else:
            self.mobile_error.setText("")
            self.mn = True

    def address_check(self):
        # if self.address.QtWidgets.QTextEdit == " " :
            
        pass
#if everything was right,it's done.
    def Done(self):
        if self.fn == True and self.ln == True and self.eml == True and self.pw == True and self.mn == True:
            if self.radioButton_3.isChecked():
                btn = self.radioButton_3.text()
            if self.radioButton_2.isChecked():
                btn = self.radioButton_2.text()
            if self.radioButton.isChecked():
                btn = self.radioButton.text()
            conn= sqlite3.connect("Users.db")
            c = conn.cursor()
            # Create table
            # c.execute('''CREATE TABLE users
            #  (Name text, Last_Name text, Email text, Password text, Phone_Number real, Gender text,
            #  Birthday text, Address text)''')
            
            temp_var = self.dateEdit.date() 
            get_date = temp_var.toPyDate()

            v = [self.firstname.text(), self.lastname.text(), self.email.text(), self.password.text(), self.mobile.text(), btn,
            get_date, self.address.toPlainText()]

            c.execute("""
                INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?); 
            """, v)

            conn.commit()
            self.show_popup2()

            self.Registration.close()
        
    def show_popup2(self):
        msg = QMessageBox()
        msg.setWindowTitle("Customer Number")
        msg.setText("Do you want a Specific Customer Number?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        y = QMessageBox.Yes
        self.Registration.close()
        x = msg.exec_()
        if x == y:
            self.popup_yes()
        else:
            self.popup_no()
        
    def popup_yes(self):
        cnt = sqlite3.connect('Users.db')
        c = cnt.cursor()
        # c.execute("""
        #     CREATE TABLE CustomerN (Name text , Last_Name text , Email text , Phone_Number integer , Customer_Number integer);
        # """)
        # c.execute("""
        #          INSERT INTO CustomerN (Name , Last_Name , Email , Phone_Number , Customer_Number) VALUES ('Sheida','Babaee',
        #          'Sheidasba@gmail.com','09381407925','250050')
        # """)
        c.execute(""" 
                 SELECT Customer_Number from CustomerN
        """)
        cnt.commit()
        newlist = []
        for row in c.fetchall():
            newlist.append(row)
        y = int(newlist[-1][0])+1
        allinfo = [self.firstname.text() , self.lastname.text() , self.email.text() , self.mobile.text() , y]
        cnt = sqlite3.connect('Users.db')
        c = cnt.cursor()
        c.execute("""
                INSERT INTO CustomerN  VALUES (?,?,?,?,?);""" , allinfo)
        cnt.commit()
        # these are the next popup message code
        msg = QMessageBox()
        msg.setWindowTitle("Customer Number:")
        msg.setIcon(QMessageBox.Information)
        msg.setText(f"This is your Customer Number: {y}")
        msg.setInformativeText("Thanks for registration")
        msg.setStandardButtons(QMessageBox.Close)

        x = msg.exec_()

    def popup_no(self):
        msg = QMessageBox()
        msg.setWindowTitle("Done!")
        msg.setText("Your registration is successfully completed")
        msg.setInformativeText("Thanks for registration")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Close)

        x = msg.exec_()

    def retranslateUi(self, Registration):
        _translate = QtCore.QCoreApplication.translate
        Registration.setWindowTitle(_translate("Registration", "Service Company"))
        Registration.setWindowIcon(QIcon('null.png'))
        self.label.setText(_translate("Registration", "Registration Form"))
        self.done.setText(_translate("Registration", "Done"))
        self.label_3.setText(_translate("Registration", "First Name:"))
        self.label_8.setText(_translate("Registration", "Last Name:"))
        self.label_10.setText(_translate("Registration", "Email:"))
        self.label_9.setText(_translate("Registration", "Password:"))
        self.label_7.setText(_translate("Registration", "Confirm Password:"))
        self.label_6.setText(_translate("Registration", "Gender:"))
        self.label_5.setText(_translate("Registration", "Date of Birth:"))
        self.label_4.setText(_translate("Registration", "Mobile:"))
        self.label_2.setText(_translate("Registration", "Address:"))
        self.radioButton_3.setText(_translate("Registration", "Female"))
        self.radioButton_2.setText(_translate("Registration", "Male"))
        self.radioButton.setText(_translate("Registration", "Others"))
        self.menuAbout.setTitle(_translate("Registration", "About..."))
        self.menuContanct.setTitle(_translate("Registration", "Contanct"))
        self.actionUs.setText(_translate("Registration", "Us!"))
        self.actionThis_App.setText(_translate("Registration", "This App!"))
        self.actionVia_E_mail.setText(_translate("Registration", "Via E_mail"))
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Registration = QtWidgets.QMainWindow()
    ui = RF_Form()
    ui.setupUi(Registration)
    Registration.show()
    sys.exit(app.exec_())

