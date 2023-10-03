import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import yfinance as yf

symbolwin = uic.loadUiType(r"C:\Users\chomp\Documents\VSC\Coursework\UI\symbol.ui")[0]

class WindowClass(QtWidgets.QMainWindow, symbolwin):
    def __init__(self, stock_data, parent = None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self); 
        self.active_data(stock_data)
        
    def active_data(self, stock_data):
        symboltable = self.symboltable
        rows, cols = len(stock_data), len(stock_data[0])
        symboltable.setRowCount(rows)
        symboltable.setColumnCount(cols)
        headers = ['Symbol', 'Company Name', 'Last Price', 'Volume', 'Market Cap']
        self.symboltable.setHorizontalHeaderLabels(headers)
        for i, row_data in enumerate(stock_data):
            for j, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                symboltable.setItem(i, j, item)

    def mas():
        most_active = yf.Tickers("GME AAPL TSLA MSFT AMC")
        stock_data = []

        for ticker_symbol in most_active.tickers:
            ticker = yf.Ticker(ticker_symbol)
            symbol = ticker_symbol
            company_name = ticker.info.get('longName', '')
            last_price = ticker.history(period="1d")['Close'][0]
            volume = ticker.info.get('volume', '')
            market_cap = ticker.info.get('marketCap', '')
        
            stock_data.append([symbol, company_name, last_price, volume, market_cap])

        return stock_data
    
app = QtWidgets.QApplication(sys.argv)
symbolw = WindowClass(None) 
symbolw.show()
app.exec_()