import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

datawin = uic.loadUiType(r"C:\Users\chomp\Documents\VSC\QtDesigner\designs\data.ui")[0]

class Ui_DataWindow(QMainWindow, datawin):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self); 
        layout = QVBoxLayout(self.display)
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)
        self.ticker_symbol = "GLD"
        self.fetch_data()
        self.plot_graph()

    def fetch_data(self):
        self.data = yf.download(self.ticker_symbol, start="2010-01-01", end="2025-01-01")
        self.data.reset_index(inplace=True)

    def plot_graph(self):
        x = np.arange(len(self.data))
        y = self.data['Close'].values
        x = x.reshape(-1, 1)
        model = LinearRegression()
        model.fit(x, y)
        y_pred = model.predict(x)
        self.ax.clear()
        self.ax.plot(self.data['Date'], y, label="Close Price")
        self.ax.plot(self.data['Date'], y_pred, label="Linear Regression", linestyle="--")
        self.ax.legend()
        self.ax.set_xlabel("Date")
        self.ax.set_ylabel("Price")
        self.figure.autofmt_xdate()
        self.canvas.draw()
        self.datatable.setRowCount(len(self.data))
        self.datatable.setColumnCount(len(self.data.columns))
        self.datatable.setHorizontalHeaderLabels(self.data.columns)
        for row in range(len(self.data)):
            for column in range(len(self.data.columns)):
                item = QTableWidgetItem(str(self.data.iloc[row, column]))
                self.datatable.setItem(row, column, item)
        header = self.datatable.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Ui_DataWindow()
    mainWindow.show()
    sys.exit(app.exec_())
