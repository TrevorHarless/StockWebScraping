import requests
from bs4 import BeautifulSoup

"""
Creates the list for the tickers and asks the user how many tickers they are adding. Then, tickers are added into a list
which will be used to concatenate with the URLs. 
"""

symbols = []


# Some explanation
def get_symbols():
    n = int(input("Enter the number of tickers you are adding: "))
    for i in range(0, n):
        symbol_input = input("Enter ticker: ")
        symbols.append(symbol_input)


# Function for getting the page data for HTML parsing.
def get_page(url):
    response = requests.get(url)
    page_content = response.text
    soup = BeautifulSoup(page_content, 'html.parser')
    return soup


# Some explanation
def get_stock_price():
    for symbol in range(len(symbols)):
        the_url = "https://finance.yahoo.com/quote/" + symbols[symbol] + "?pe" + symbols[symbol] + "&.tsrc=fin-srch"
        soup = get_page(the_url)
        the_ticker = symbols[symbol]
        stock_price = soup.select_one(f'fin-streamer[data-symbol="{the_ticker}"]')['value']
        print(symbols[symbol] + ": " + stock_price)


get_symbols()
get_stock_price()
