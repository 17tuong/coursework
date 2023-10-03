import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sqlite3 as lite
from menu import MenuWindow

loginwin = uic.loadUiType(r"C:\Users\chomp\Documents\VSC\Coursework\UI\login.ui")[0]
usersdb = r"C:\Users\chomp\Documents\VSC\Coursework\Databases\users.db"

class LoginWindow(QtWidgets.QMainWindow, loginwin):
    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self); 
        self.loginbtn.clicked.connect(self.login)
        self.signupbtn.clicked.connect(self.signup)
        self.forgotbtn.clicked.connect(self.forgot)
        
    def login(self):
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
            self.errorlbl.setStyleSheet("color: red;")
            self.errorlbl.resize(self.errorlbl.sizeHint())

    def open_menu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = MenuWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def signup(self):
        fname = self.fnamein.text()
        sname = self.snamein.text()
        email = self.emailin.text()
        username = self.userin.text()
        password = self.passin.text()
        rpassword = self.rpassin.text()
        if password != rpassword:
            self.errorlbl_2.setText("Passwords do not match.")
            self.errorlbl_2.setStyleSheet("color: red;")
            self.errorlbl_2.resize(self.errorlbl_2.sizeHint())
        else:
            con = lite.connect(usersdb)
            cur = con.cursor()
            cur.execute("INSERT INTO users ('first name', 'surname', 'email', 'username', 'password') VALUES (?, ?, ?, ?, ?)", (fname, sname, email, username, password))
            con.commit()
            con.close()
            self.errorlbl_2.setText("Account created successfully.")
            self.errorlbl_2.setStyleSheet("color: green;")
            self.errorlbl_2.resize(self.errorlbl_2.sizeHint())

    def forgot(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = uic.loadUi(r"C:\Users\chomp\Documents\VSC\Coursework\UI\forgot.ui", self.window)
        self.window.show()
        self.close()

app = QtWidgets.QApplication(sys.argv)
w1 = LoginWindow(None) 
w1.show()
app.exec_()
