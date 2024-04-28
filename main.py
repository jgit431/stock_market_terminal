import sys
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from strategy import calculate_bollinger_bands, calculate_rsi, calculate_atr, generate_signals
from backtest import backtest_strategy
from data import fetch_data, get_company_name

class TradingSystemGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("Trading System GUI")
        self.setGeometry(100, 100, 800, 600)

        # Create a central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create a QLabel for displaying the stock ticker
        self.ticker_label = QLabel("Stock Ticker:")
        layout.addWidget(self.ticker_label)

        # Create a QLineEdit for entering the stock ticker
        self.ticker_input = QLineEdit()
        layout.addWidget(self.ticker_input)

        # Create a QPushButton to fetch data for the entered ticker
        fetch_button = QPushButton("Fetch Data")
        fetch_button.clicked.connect(self.fetch_data_button_clicked)
        layout.addWidget(fetch_button)

        # Create a QLabel for displaying the company name
        self.company_name_label = QLabel("Company Name:")
        layout.addWidget(self.company_name_label)

        # Create a Matplotlib figure canvas
        self.canvas = FigureCanvas(plt.figure())

        # Add the canvas to the layout
        layout.addWidget(self.canvas)

        # Initialize variables
        self.stock_data = None
        self.upper_band = None
        self.lower_band = None
        self.rsi = None
        self.atr = None
        self.signals = None
        self.portfolio_value = None

    def fetch_data_button_clicked(self):
        # Fetch data for the entered ticker
        ticker = self.ticker_input.text()
        if ticker:
            self.stock_data = fetch_data(ticker, '2019-01-01', '2020-01-01')

            # Get the company name
            company_name = get_company_name(ticker)
            self.company_name_label.setText(f"Company Name: {company_name}")

            # Calculate indicators
            self.upper_band, self.lower_band = calculate_bollinger_bands(self.stock_data)
            self.rsi = calculate_rsi(self.stock_data)
            self.atr = calculate_atr(self.stock_data)

            # Generate signals
            self.signals = generate_signals(self.stock_data, self.upper_band, self.lower_band, self.rsi, self.atr)

            # Backtest strategy
            self.portfolio_value = backtest_strategy(self.stock_data, self.signals)

            # Plot the data
            self.plot_data()

    def plot_data(self):
        # Clear previous plot
        plt.clf()

        # Plot stock data
        plt.plot(self.stock_data.index, self.stock_data['Adj Close'], label='Stock Price')

        # Plot Bollinger Bands
        plt.plot(self.stock_data.index, self.upper_band, label='Upper Band', linestyle='--')
        plt.plot(self.stock_data.index, self.lower_band, label='Lower Band', linestyle='--')

        # Plot RSI
        plt.plot(self.rsi.index, self.rsi, label='RSI', linestyle='--')

        # Plot ATR
        plt.plot(self.atr.index, self.atr, label='ATR', linestyle='--')

        # Add legend
        plt.legend()

        # Update the canvas
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = TradingSystemGUI()
    gui.show()
    sys.exit(app.exec_())
