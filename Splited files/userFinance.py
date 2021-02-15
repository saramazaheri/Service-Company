# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'worker_finance.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_userFinances(object):
    def setupUi(self, Finances, username):
        self.username = username
        Finances.setObjectName("Finances")
        Finances.resize(567, 362)
        Finances.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Finances)
        self.label.setGeometry(QtCore.QRect(40, 29, 501, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(Finances)
        self.listWidget.setGeometry(QtCore.QRect(50, 80, 491, 211))
        self.listWidget.setObjectName("listWidget")
        self.Totall = QtWidgets.QLabel(Finances)
        self.Totall.setGeometry(QtCore.QRect(50, 305, 491, 41))
        self.Totall.setText("")
        self.Totall.setObjectName("Totall")

        self.retranslateUi(Finances)
        QtCore.QMetaObject.connectSlotsByName(Finances)

        self.write()

    def write(self):
        conn= sqlite3.connect("Finances.db")
        c = conn.cursor()

        c.execute("SELECT * FROM Users_Finances WHERE Email=(?);",(self.username,))
        sum = 0
        for row in c.fetchall():
            self.listWidget.addItem(f"{row[-2]} - {row[-1]}")
            sum += row[-2]

        self.Totall.setText(f"You have spent {sum}t till now.")

    def retranslateUi(self, Finances):
        _translate = QtCore.QCoreApplication.translate
        Finances.setWindowTitle(_translate("Finances", "Finances"))
        self.label.setText(_translate("Finances", "Your finances till now:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Finances = QtWidgets.QWidget()
    ui = Ui_userFinances()
    ui.setupUi(Finances, 'None')
    Finances.show()
    sys.exit(app.exec_())
