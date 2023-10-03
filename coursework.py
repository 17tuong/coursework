import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sqlite3 as lite

loginwin = uic.loadUiType(r"C:\Users\chomp\Documents\VSC\Coursework\UI\login.ui")[0]
usersdb = r"C:\Users\chomp\Documents\VSC\Coursework\Databases\users.db"

class loginwindow(QtWidgets.QMainWindow, loginwin):
    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self); 
        self.loginbtn.clicked.connect(self.loginFunction)
        
    def loginFunction(self):
        username = self.userlogin.text()
        password = self.passlogin.text()
        con = lite.connect(usersdb)
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        result = cur.fetchone()
        con.close()

        if result:
            self.close()
            self.open_menu()
        else:
            self.errorlbl.setText("Invalid username or password.")

    def open_menu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = uic.loadUi(r"C:\Users\chomp\Documents\VSC\Coursework\UI\menu.ui", self.window)
        self.window.show()
        pass

app = QtWidgets.QApplication(sys.argv)
w1 = loginwindow(None) 
w1.show()
app.exec_()