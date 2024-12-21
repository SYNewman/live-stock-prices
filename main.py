'''
To-Do:
- make it only show once
- only show 2 decimal places
- show the increase / decrease
- be green if increased, red if decreased
- maybe turn into desktop/mobile/web app
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
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear') #Clears the console screen
            
            # Print table header
            print(f"{'Ticker':<10} {'Price':<10}") #Format column titles
            print("=" * 20)
            
            prices = get_stock_prices(tickers)
            for ticker, price in prices.items():
                print(f"{ticker:<10} {price:<10}")
            
            time.sleep(refresh_rate)
    except KeyboardInterrupt:
        print("\nExiting live ticker display.")

if __name__ == "__main__":  # Ensures code is not run when imported as a module
    tickers = ["AAPL", "GOOGL", "AMZN", "MSFT", "TSLA"]
    refresh_rate = 5
    display_live_prices(tickers, refresh_rate)
