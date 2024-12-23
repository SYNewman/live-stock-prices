import yfinance as yf
import time
import os
from termcolor import colored

def get_stocks(): #Needs to be worked on
    tickers = []
    special_characters = {'^', '$', '/', '!', '&', '#'}
    try:
        with open("tickers.txt", "r") as file:
            for i in file:
                try:
                    stock = i.strip()
                    if any(char in stock for char in special_characters):
                        continue
                    tickers.append(stock)
                except Exception as exception_type:
                    print(f"{stock} could not be loaded. The problem was: {exception_type}")
        return tickers
    except Exception as exception_type:
        print(f"List of Stocks could not be loaded. The problem was: {exception_type}")
        raise

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
            print(f"{'Stock':<10} {'Price':<10} {'Change':<10}")
            
            for ticker, price in prices.items():
                # Calculate the change
                change = None
                if previous_prices[ticker] is not None:
                    change = price - previous_prices[ticker]
                
                # Sets the code for the change
                change_display = "N/A"
                if change is not None:
                    change_display = f"{change:+.2f}"
                    
                colour = "yellow"
                if change is not None:    
                    if change > 0:
                        colour = "green"
                    elif change < 0:
                        colour = "red"
                
                print(colored(f"{ticker:<10} {price:<10.2f} {change_display:<10}", colour))
                previous_prices[ticker] = price
            time.sleep(refresh_rate)
    except KeyboardInterrupt:
        print("\nExiting live ticker display.")

if __name__ == "__main__":  # Ensures code is not run when imported as a module
    tickers = ["AAPL", "GOOGL", "AMZN", "MSFT", "TSLA"]
    refresh_rate = 5
    display_live_prices(tickers, refresh_rate)