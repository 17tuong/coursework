import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sqlite3 as lite

forgotwin = uic.loadUiType(r"C:\Users\chomp\Documents\VSC\Coursework\UI\forgot.ui")[0]
usersdb = r"C:\Users\chomp\Documents\VSC\Coursework\Databases\users.db"

class WindowClass(QtWidgets.QMainWindow, forgotwin):
    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self); 
        self.enterbtn.clicked.connect(self.enter)
        self.backbtn.clicked.connect(self.back)

    def enter(self):
        fname = self.fnamein.text()
        sname = self.snamein.text()
        email = self.emailin.text()
        con = lite.connect(usersdb)
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE 'first name' = ? AND 'surname' = ? AND 'email' = ?", (fname, sname, email))
        result = cur.fetchone()

        if result:
            cur.execute("SELECT username, password FROM users WHERE 'first name' = ? AND 'surname' = ? AND 'email' = ?", (fname, sname, email))
            result = cur.fetchone()
            self.userlbl.setText(result[0])
            self.userlbl.resize(self.userlbl.sizeHint())
            self.passlbl.setText(result[1])
            self.passlbl.resize(self.passlbl.sizeHint())
        else:
            self.errorlbl.setText("Invalid details.")
            self.errorlbl.setStyleSheet("color: red;")
            self.errorlbl.resize(self.errorlbl.sizeHint())

    def back(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = uic.loadUi(r"C:\Users\chomp\Documents\VSC\Coursework\UI\login.ui", self.window)
        self.window.show()
        self.close()

app = QtWidgets.QApplication(sys.argv)
forgotw = WindowClass(None)
forgotw.show()
app.exec_()