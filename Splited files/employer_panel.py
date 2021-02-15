from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from Servicelist import *
from confirmation import *
from Services_2 import *
from worker import *

class Ui_employer_panel(object):
    def openremove(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_remove_service_list()
        self.ui.setupUi(self.window)
        self.window.show()

    def opendelete(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Sure()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def openadd(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Services_2()
        self.ui.setupUi(self.window,self.username)
        self.window.show()

    def setupUi(self, employer_panel,username):
        self.username=username
        employer_panel.setObjectName("employer_panel")
        employer_panel.resize(650, 550)
        self.verticalLayout = QtWidgets.QVBoxLayout(employer_panel)
        self.verticalLayout.setObjectName("verticalLayout")
        self.add_button = QtWidgets.QPushButton(employer_panel)
        self.add_button.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
        "background-color: rgb(0, 0, 127);\n"
        "color: rgb(255, 255, 255);")
        self.add_button.setObjectName("add_button")
        self.verticalLayout.addWidget(self.add_button)
        self.remove_button = QtWidgets.QPushButton(employer_panel)
        self.remove_button.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
        "background-color: rgb(0, 0, 127);\n"
        "color: rgb(255, 255, 255);")
        self.remove_button.setObjectName("remove_button")
        self.verticalLayout.addWidget(self.remove_button)
        self.finances_button = QtWidgets.QPushButton(employer_panel)
        self.finances_button.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
        "color: rgb(255, 255, 255);\n"
        "background-color: rgb(0, 0, 127);")
        self.finances_button.setObjectName("finances_button")
        self.verticalLayout.addWidget(self.finances_button)
        self.delete_A = QtWidgets.QPushButton(employer_panel)
        self.delete_A.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(0, 0, 127);\n"
        "font: 12pt \"MS Shell Dlg 2\";")
        self.delete_A.setObjectName("delete_A")
        self.verticalLayout.addWidget(self.delete_A)

        self.retranslateUi(employer_panel)
        QtCore.QMetaObject.connectSlotsByName(employer_panel)

        self.delete_A.clicked.connect(self.delete_account)
        self.add_button.clicked.connect(self.add_service)
        self.remove_button.clicked.connect(self.remove_service)
        self.add_button.clicked.connect(self.add_service)
        self.finances_button.clicked.connect(self.cal_finances)

    def add_service(self):
        self.openadd()

    def remove_service(self):
        self.openremove()
    #Serviceslist

    def cal_finances(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Finances()
        self.ui.setupUi(self.window, self.username)
        self.window.show()

    def delete_account(self):
        self.opendelete()
    #Confiramtion

    def retranslateUi(self, employer_panel):
        _translate = QtCore.QCoreApplication.translate
        employer_panel.setWindowTitle(_translate("employer_panel", "Form"))
        employer_panel.setWindowIcon(QIcon('null.png'))
        self.add_button.setText(_translate("employer_panel", "Add Service(s)"))
        self.remove_button.setText(_translate("employer_panel", "Remove Service(s)"))
        self.finances_button.setText(_translate("employer_panel", "Finances"))
        self.delete_A.setText(_translate("employer_panel", "Delete Account"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    employer_panel = QtWidgets.QWidget()
    ui = Ui_employer_panel()
    ui.setupUi(employer_panel,'None')
    employer_panel.show()
    sys.exit(app.exec_())
 