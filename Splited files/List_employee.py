# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'list_employee.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Services_User import *
import sqlite3
from datetime import date
import sys
from employers import *
from Services_User import *
from costumer_panel import *
from Login import *

class Service_info:
    def __init__(self, name, price, point):
        self.name= name
        self.price= int(price)
        self.point= int(point)

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_point(self):
        return self.point


s1= Service_info('Cooking', 35000, 6) #per food
s2= Service_info('Catering', 20000, 3) #per hour
s3= Service_info('House Cleaning', 15000, 2) #per hour
s4= Service_info('Building Cleaning', 19000, 3) #per hour
s5= Service_info('Laundry', 10000, 1) #minimum per cloth
s6= Service_info('Indoor Spraying', 20000, 5) #per hour
s7= Service_info('Cooling System', 350000, 7) #per system
s8= Service_info('Heating System', 80000, 7) #per system
s9= Service_info('Water Plumbing', 100000, 4) #per hour
s10= Service_info('Gas Plumbing', 150000, 6) #per hour
s11= Service_info('Water Refinary', 120000, 4) #per system
s12= Service_info('Big Appliance', 80000, 4) #per system
s13= Service_info('Building', 250000, 7) #per day
s14= Service_info('Woodworking', 250000, 7) #per piece
s15= Service_info('Wallpaper/Parquet', 90000, 3) #per m^2
s16= Service_info('Ceramic and Tiling', 120000, 3) #per m^2
s17= Service_info('Plastering', 250000, 4) #per day
s18= Service_info('Painting', 250000, 3) #per day
s19= Service_info('Smithery and Welding', 300000, 7) #per day
s20= Service_info('Doors And Windows', 100000, 3) #each window/door
s21= Service_info('Interior Design', 200000, 8) #per room
s21= Service_info('Garden Spraying', 26000, 5) #per hour
s22= Service_info('Outdoor Design', 250000, 8)
s23= Service_info('Gardening', 15000, 4) #per hour
s24= Service_info('Laptop Repiring', 50000, 7) #per system
s25= Service_info('Mobile/ Tablet Repairing', 50000, 7) 
s26= Service_info('Game Console Repairing', 70000, 7)
s27= Service_info('Wiring', 250000, 7) #per day
s28= Service_info('Generators', 300000, 5) #per day
s29= Service_info('Security Alarms', 80000, 5) #per system
s30= Service_info('Security Cameras', 80000, 5) #per system
s31= Service_info('Repairing', 100000, 4) #per car
s32= Service_info('Car Wash', 30000, 1)
s33= Service_info('Home Furniture', 35000, 3) #per hour
s34= Service_info('Packages', 15000, 2) #per hour
s35= Service_info('Sewing', 120000, 6) #minimum
s36= Service_info('Cloth Restoration', 20000, 5) #minimum 
s37= Service_info('Hair', 50000, 6) #minimum
s38= Service_info('Make-up', 80000, 7) #minimum per hour
s39= Service_info('Nails', 100000, 6)
s40= Service_info('Injections/ Bandages/ Stiches', 25000, 7) #minimum
s41= Service_info('Nanny', 80000, 7) #per day
s42= Service_info('Elderly Nursing and Care', 90000, 8) #per day
s43= Service_info('Patient Care', 90000, 9) #per day
s44= Service_info('Grooming', 140000, 7) #per pet
s45= Service_info('Walking', 45000, 2) #per hour
s46= Service_info('Training', 80000, 9) #per hour
s47= Service_info('Veterinary', 200000, 10)
s48= Service_info('Teaching All Grades', 50000, 10) #minimum per hour
s49= Service_info('Enterance Exam', 120000, 10) #minimum per hour(depends on the course)
s50= Service_info('Teaaching University Courses', 130000, 10) #minimum per hour(depends on the course)
s51= Service_info('Music', 200000, 10) #per hour
s52= Service_info('Important Sofwares/ Programming', 140000, 10) #minimum per hour(depends on the software)
s53= Service_info('Law', 150000, 10) #per hour
s54= Service_info('Graduation', 50000, 10) #per hour
s55= Service_info('Psychology', 180000, 10) #per hour
s56= Service_info('Food and Diet', 100000, 10) #per hour
s57= Service_info('Finger Food', 100000, 6)
s58= Service_info('Photography', 160000, 9) #per hour
s59= Service_info('Musician', 200000, 9) #per hour
s60= Service_info('Key Making', 50000, 7) #per key
s61= Service_info('Disinfect Home and Workplace', 130000, 9) #per room
s62= Service_info('Medical Lab Tests', 50000, 9)
s63= Service_info('Car Opening', 15000, 7)
s64= Service_info('other', 50000, 5)
sall= [s1]+[s2]+[s3]+[s4]+[s5]+[s6]+[s7]+[s8]+[s9]+[s10]+[s11]+[s12]+[s13]+[s14]+[s15]+[s16]+[s17]+[s18]+[s19]+[s20]+[s21]+[s22]+[s23]+[s24]+[s25]+[s26]+[s27]+[s28]+[s29]+[s30]+[s31]+[s32]+[s33]+[s34]+[s35]+[s36]+[s37]+[s38]+[s39]+[s40]+[s41]+[s42]+[s43]+[s44]+[s45]+[s46]+[s47]+[s48]+[s49]+[s50]+[s51]+[s52]+[s53]+[s54]+[s55]+[s56]+[s57]+[s58]+[s59]+[s60]+[s61]+[s62]+[s63]+[s64]

class Ui_list_for_users(object):
    def setupUi(self, list_for_users, username, servicename):
        self.username = username
        self.servicename = servicename
        list_for_users.setObjectName("list_for_users")
        list_for_users.resize(555, 511)
        list_for_users.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listWidget = QtWidgets.QListWidget(list_for_users)
        self.listWidget.setGeometry(QtCore.QRect(30, 70, 491, 361))
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(list_for_users)
        self.label.setGeometry(QtCore.QRect(30, 20, 501, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(list_for_users)
        self.pushButton.setGeometry(QtCore.QRect(412, 450, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(0, 0, 127);")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(list_for_users)
        QtCore.QMetaObject.connectSlotsByName(list_for_users)

        self.list_for_users = list_for_users

        self.view()

    def view(self):
        conn= sqlite3.connect("Employers.db")
        c = conn.cursor()
        d = conn.cursor()
        l = conn.cursor()
        c.execute("SELECT * FROM service WHERE Services=(?)", (self.servicename,))
        l.execute("SELECT * FROM service WHERE Services=(?)", (self.servicename,))
        sortedlist= []
        for row in c.fetchall():
            for j in listemployer:
                if row[0]== j.email:
                    d.execute("SELECT * FROM points_and_income WHERE Email=(?)", (row[0],))
                    for row1 in d.fetchall():
                        sortedlist.append(row1)

        self.Sort(sortedlist)
        for i in range(len(sortedlist)):
            self.listWidget.addItem(f""" Name: {sortedlist[i][0]} {sortedlist[i][1]} -Phone Number: {sortedlist[i][2]} - Email: {sortedlist[i][4]} - Education: {sortedlist[i][5]} - Gender: {sortedlist[i][6]} - Score: {sortedlist[i][-2]}""")

        self.pushButton.clicked.connect(self.sub)

    def Sort(self, sortedlist): 
        # reverse = None (Sorts in Ascending order) 
        # key is set to sort using second element of  
        # sublist lambda has been used 
        sortedlist.sort(key = lambda x: x[7], reverse=True) 
        return sortedlist
    
    def sub(self):
        conn= sqlite3.connect("Employers.db")
        c = conn.cursor()
        d = conn.cursor()
        b = conn.cursor()
        count= 0
        item = self.listWidget.currentItem()
        txt = item.text()
        listmaker= txt.split(" ")
        c.execute("SELECT * FROM points_and_income WHERE Email=(?);", (listmaker[9],))


        for row in c.fetchall():
            for i in sall:
                if i.get_name()== self.servicename:
                    d.execute("UPDATE points_and_income SET Points=(?)  WHERE Email=(?);", (row[-2]+i.get_point(), listmaker[9]))
                    d.execute("UPDATE points_and_income SET Income=(?) WHERE Email=(?);", (row[-1]+i.get_price(),listmaker[9]))
                    conn.commit()
                    count+=1
        
        if count==0:
            for row in c.fetchall():
                for i in sall:
                    if i.get_name()== self.servicename:
                        d.execute("UPDATE points_and_income SET Points= (?) WHERE Email=(?);", (row[-2]+sall[-1].get_point(),listmaker[9],))
                        d.execute("UPDATE points_and_income SET Income= (?) WHERE Email=(?);", (row[-1]+sall[-1].get_price(),listmaker[9],))
                        conn.commit()

        b.execute("SELECT * FROM points_and_income WHERE Email=(?);", (listmaker[9],))

        conn1 = sqlite3.connect("Finances.db")
        c1 = conn1.cursor()

        for row in b.fetchall():
            for i in listemployer:
                if row[4]== i.email:
                    c1.execute("INSERT INTO Employers_Finances VALUES (?, ?, ?, ?, ?, ?, ?);", (i.name,i.lastname,i.email,i.phone,self.servicename,row[-1],date.today()))
                    conn1.commit()

        c2 = conn1.cursor()

        for i in listusers:
            if self.username == i.Email:
                for j in sall:
                    if j.name== self.servicename:
                        c1.execute("INSERT INTO Users_Finances VALUES (?, ?, ?, ?, ?, ?, ?);", (i.Name,i.Last_Name,i.Email,i.Phone_Number,self.servicename,j.price,date.today()))
                        conn1.commit()

        self.list_for_users.close()


    def retranslateUi(self, list_for_users):
        _translate = QtCore.QCoreApplication.translate
        list_for_users.setWindowTitle(_translate("list_for_users", "List of employees"))
        self.label.setText(_translate("list_for_users", "Please select your desired employees. This list is sorted by ascending rank."))
        self.pushButton.setText(_translate("list_for_users", "Submit"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    list_for_users = QtWidgets.QWidget()
    ui = Ui_list_for_users()
    ui.setupUi(list_for_users, 'None', 'None')
    list_for_users.show()
    sys.exit(app.exec_())
