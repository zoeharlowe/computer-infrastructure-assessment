# computer-infrastructure-assessment
by Zoe McNamara Harlowe

### Welcome to my submission for the assessment for the Computer Infrastructure module. This module is provided by ATU (Atlantic Technological University) as part of the HDip in Computing in Data Analytics.

---

## Table of Contents

1. [Prerequisites](#prerequisites)  
2. [Setup](#setup)
3. [Technologies](#technologies)
4. [Libraries](#libraries)
5. [Project Structure](#project-structure)    
6. [Problems](#problems)

---

## Prerequisites

- Python 3.7 or higher  
- Required packages (listed in `requirements.txt`):  
  ```bash
  numpy
  yfinance
  pandas
  pathlib
  matplotlib
  datetime

---

## Setup

**View the repository online using Github Codespaces:**
1. Sign up for a free Github account.
2. Go to the repository page in your browser.
3. Click the green 'Code' button.
4. Click the 'Codespaces' tab.
5. Click 'Create New Codespace' on main.


**Or you can clone the repository onto your own machine:**
1. In Commander, clone the repo and change directory:
```bash 
git clone <https://github.com/zoeharlowe/computer-infrastructure-assessment>
cd <computer-infrastructure-assessment>
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Launch the Jupyter Notebook problems.ipynb locally:
```bash
jupyter notebook problems.ipynb
```

--- 

## Technologies

- Python
- Git
- Github
- Codespaces
- Jupyter

---

## Libraries

- Numpy: https://numpy.org/doc/2.3/user/absolute_beginners.html
- Yfinance: https://ranaroussi.github.io/yfinance/
- Pandas: https://pandas.pydata.org/docs/user_guide/index.html
- Pathlib: https://docs.python.org/3/library/pathlib.html
- Matplotlib.pyplot: https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html
- Datetime: https://docs.python.org/3/library/datetime.html

--- 

## Project Structure

Computer Infrastructure Assessment:
- `.gitignore`
- `README.md`
- `faang.py` – executable script for downloading and plotting FAANG data
- `.github/workflows/faang.yml` – GitHub Actions workflow for automation
- `data/` – folder where CSV data files are saved
- `plots/` – folder where PNG plots are saved            
- `requirements.txt`  
- `problems.ipynb` (notebook with explanations and solutions)

    [Imports](problems.ipynb#imports)

    [Problem 1: Data from yfinance](problems.ipynb#problem-1-data-from-yfinance)

    [Problem 2: Plotting Data](problems.ipynb#problem-2-plotting-data)

    [Problem 3: Script](problems.ipynb#problem-3-script)

    [Problem 4: Automation](problems.ipynb#problem-4-automation)

---

## Problems

### Problem 1: Data from yfinance
In this problem I write the function `get_data()`, which downloads hourly data for the last five days for FAANG stocks (META, AAPL, AMZN, NFLX, GOOG). Data is saved in the `data/` folder as a timestamped CSV file.
**References:**
  - yfinance documentation: https://ranaroussi.github.io/yfinance/
  - Investopedia: FAANG Stocks: https://www.investopedia.com/terms/f/faang-stocks.asp
  - AlgoTrading101: yfinance guide: https://algotrading101.com/learn/yfinance-guide/
  - Ian McLoughlin, Video Lecture Week 5 (Saving Data): https://atlantictu-my.sharepoint.com/personal/ian_mcloughlin_atu_ie/_layouts/15/stream.aspx?id=%2Fpersonal%2Fian%5Fmcloughlin%5Fatu%5Fie%2FDocuments%2Fstudent%5Fshares%2Fcomputer%2Dinfrastructure%2F21%2Dsaving%2Ddata%2Emkv&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E71983e3b%2D2c6e%2D4ed7%2D8a29%2Db55be8918d26
  - date.strftime documentation: https://docs.python.org/3.6/library/datetime.html#datetime.date.strftime
  - Pandas to_csv() documentation: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html

### Problem 2: Plotting Data
In this problem I write the function `plot_data()`, which loads the latest CSV file from `data/` and plots the Close prices for all five stocks on one graph. Output is saved in the `plots/` folder as a timestamped PNG file.
**References:**
  - Copilot: Help with writing plotting function: https://copilot.microsoft.com/shares/9EGGcjhzuPrid1sVUni2k

### Problem 3: Script
In this problem, I created `faang.py`, an executable script containing both of the above functions. The script includes a shebang line and can be run with the command `./faang.py` - this will download the data and generate the plot automatically. 
**References:**
  - Medium.com: A Deeper View into the Shebang: https://medium.com/@jcroyoaun/a-deeper-view-into-the-shebang-for-linux-scripting-4a26395df49d
  - ChatGPT: Writing a sanity check for faang.py: https://chatgpt.com/share/692ef5f0-bdf0-800c-8570-4d2775819ff9
  
### Problem 4: Automation
In this section of the notebook, I explain my automation of the above process. A GitHub Actions workflow (`faang.yml`) is included in `.github/workflows/`. This workflow runs the script automatically every Saturday morning.
**References:**
  - Copilot: Help with workflow automation code and explanations: https://copilot.microsoft.com/shares/ZT4wuksEYTXXx4yMrqVid
  - GitHub Actions demo workflow: https://docs.github.com/en/actions/get-started/quickstart
  - Yahoo Finance Stocks: https://finance.yahoo.com/markets/stocks/most-active/