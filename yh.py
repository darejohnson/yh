import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd

# Define the ticker symbol for the S&P 500
ticker = "^GSPC"

# Calculate the start and end dates
end_date = datetime.now().strftime("%Y-%m-%d")
start_date = (datetime.now() - timedelta(days=1.5 * 365)).strftime("%Y-%m-%d")

# Get the historical data
data = yf.download(ticker, start=start_date, end=end_date)

data.to_csv("./sp.csv")
