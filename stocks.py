#! /usr/bin/env python

# Dates and times
import datetime as dt

# Yahoo Finance
import yfinance as yf


# # Identify the stocks I want to download
tickers = yf.Tickers('META AAPL AMZN NFLX GOOG')

# Get data
df = yf.download(['GOOG', 'META', 'AAPL', 'AMZN', 'NFLX'], period='5d', interval='1h')

# Current datetime
now = dt.datetime.now()

# Filename
filename = now.strftime("%Y%m%d-%H%M%S") + ".csv"

# Save to a CSV file with the current date and time as the filename
df.to_csv(filename)
