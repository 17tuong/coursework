import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sqlite3 as lite

menuwin = uic.loadUiType(r"C:\Users\chomp\Documents\VSC\Coursework\UI\menu.ui")[0]

class MenuWindow(QtWidgets.QMainWindow, menuwin):
    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self); 
        self.symbolbtn.clicked.connect(self.symbol)
        self.stockbtn.clicked.connect(self.stock)
        self.logoutbtn.clicked.connect(self.logout)

    def symbol(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = uic.loadUi(r"C:\Users\chomp\Documents\VSC\Coursework\UI\symbol.ui", self.window)
        self.window.show()
        self.hide()
        
    def stock(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = uic.loadUi(r"C:\Users\chomp\Documents\VSC\Coursework\UI\data.ui", self.window)
        self.window.show()
        self.hide()

    def logout(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = uic.loadUi(r"C:\Users\chomp\Documents\VSC\Coursework\UI\login.ui", self.window)
        self.window.show()
        self.hide()

app = QtWidgets.QApplication(sys.argv)
menuw = MenuWindow(None)
menuw.show()
app.exec_()