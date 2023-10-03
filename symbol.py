import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import yfinance as yf
import pandas as pd

symbolwin = uic.loadUiType(r"C:\Users\chomp\Documents\VSC\Coursework\UI\symbol.ui")[0]

def get_commodity_data():
    commodity_symbols = ['GLD', 'SLV', 'USO', 'UNG', 'CORN', 'WEAT', 'SOYB', 'JO', 'NIB', 'BAL', 'SGG']
    combined_data = None
    for symbol in commodity_symbols:
        df = yf.Ticker(symbol)
        commodity_data = df.history(period='1d')
        commodity_data.insert(0, 'Symbol', df.info.get('symbol', 'N/A'))
        commodity_data.insert(1, 'Name', df.info.get('longName', 'N/A'))
        if combined_data is None:
            combined_data = commodity_data
        else:
            combined_data = pd.concat([combined_data, commodity_data])
    return combined_data

class Ui_SymbolWindow(QtWidgets.QMainWindow, symbolwin):
    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self); 
        self.update_data()

    def update_data(self):
        commodity_data = get_commodity_data()
        num_rows, num_columns = commodity_data.shape
        self.symboltable.setRowCount(num_rows)
        self.symboltable.setColumnCount(num_columns)
        self.symboltable.setHorizontalHeaderLabels(commodity_data.columns.tolist())
        for i in range(num_rows):
            for j in range(num_columns):
                item = QTableWidgetItem(str(commodity_data.iat[i, j]))
                self.symboltable.setItem(i, j, item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Ui_SymbolWindow()
    main_window.show()
    sys.exit(app.exec_())
