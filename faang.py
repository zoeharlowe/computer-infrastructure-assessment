# faang.py
# This program downloads FAANG stock data and plots closing prices. 
# The user can execute this script from the terminal
# Author: Zoe McNamara Harlowe

#!/usr/bin/env python3

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import datetime as dt

# Get data
def get_data():
    # Download the data
    df = yf.download(['META', 'AAPL', 'AMZN', 'NFLX', 'GOOG'],
                     period='5d', interval='1h')

    # Build folder and filename
    folder = Path().resolve() / "data"
    folder.mkdir(parents=True, exist_ok=True)

    filename = dt.datetime.now().strftime("%Y%m%d-%H%M%S") + ".csv"
    filepath = folder / filename

    # Save the file
    df.to_csv(filepath)

    return filepath

# Plot data
def plot_data():
    # Open latest file in data folder
    folder = Path().resolve() / "data"
    latest_file = max(folder.glob("*.csv"), key=lambda x: x.stat().st_mtime)
    df = pd.read_csv(latest_file, header=[0,1], index_col=0, parse_dates=True)
    # Plot closing prices
    df[('Close')].plot()
    # Add title and labels
    plt.title("FAANG Stock Prices")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    # Show legend
    plt.legend(title="Stocks")
    # Save figure to folder 'plots'
    folder = Path().resolve() / "plots"
    fig_filename = latest_file.stem + ".png"
    plt.savefig(folder / fig_filename)
    return folder / fig_filename

# Script 
def main():
    csv_path = get_data()
    print(f"Saved data to: {csv_path}")

    plot_path = plot_data()
    print(f"Saved plot to: {plot_path}")


# Ensure script runs when called directly
if __name__ == "__main__":
    main()
