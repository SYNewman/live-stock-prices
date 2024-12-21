import yfinance as yf
import time
import os

def get_stock_prices(tickers):
    """Fetches the latest stock prices for a list of tickers."""
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
    """
    Displays live stock prices in the console.
    :param tickers: List of stock tickers to track.
    :param refresh_rate: Time interval (in seconds) for updates.
    """
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{'Ticker':<10} {'Price':<10}")
            print("=" * 20)
            
            prices = get_stock_prices(tickers)
            for ticker, price in prices.items():
                print(f"{ticker:<10} {price:<10}")
            
            time.sleep(refresh_rate)
    except KeyboardInterrupt:
        print("\nExiting live ticker display.")

if __name__ == "__main__":
    tickers = ["AAPL", "GOOGL", "AMZN", "MSFT", "TSLA"]  # Example tickers
    refresh_rate = 5  # Update every 5 seconds
    display_live_prices(tickers, refresh_rate)
