'''
To-Do:
- add column headers
- be green if increased, red if decreased
'''

import yfinance as yf
import time
import os

def get_stock_prices(tickers):
    prices = {}
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        data = stock.history(period="1d")
        if not data.empty:
            prices[ticker] = data['Close'].iloc[-1]
        else:
            prices[ticker] = "N/A"
    return prices

def display_live_prices(tickers, refresh_rate=5):
    previous_prices = {ticker: None for ticker in tickers}
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear') #Clears the console screen
            prices = get_stock_prices(tickers)
            
            for ticker, price in prices.items():
                # Calculate the change
                change = None
                if previous_prices[ticker] is not None:
                    change = price - previous_prices[ticker]
                
                # Sets the code for the change
                change_display = "N/A"
                if change is not None:
                    change_display = f"{change:+.2f}"
                
                print(f"{ticker:<10} {price:<10.2f} {change_display:<10}")
                previous_prices[ticker] = price
            time.sleep(refresh_rate)
    except KeyboardInterrupt:
        print("\nExiting live ticker display.")

if __name__ == "__main__":  # Ensures code is not run when imported as a module
    tickers = ["AAPL", "GOOGL", "AMZN", "MSFT", "TSLA"]
    refresh_rate = 5
    display_live_prices(tickers, refresh_rate)