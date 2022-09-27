import requests
from bs4 import BeautifulSoup

symbols = []


# Obtains the number of symbols the user wants to add and then compiles those symbols into a list.
def get_symbols():
    n = int(input("Enter the number of stocks you are adding: "))
    for i in range(0, n):
        symbol_input = input("Enter symbol: ")
        symbols.append(symbol_input)


# Function for getting the page data for HTML parsing.
def get_page(url):
    response = requests.get(url)
    page_content = response.text
    soup = BeautifulSoup(page_content, 'html.parser')
    return soup


# Iterates through the symbols list and obtains the stock price of each symbol through concatenating each symbol with the
# yahoo URL. BeautifulSoup is then used to find the value of the stock in the HTML code.
def get_stock_price():
    for symbol in range(len(symbols)):
        the_url = "https://finance.yahoo.com/quote/" + symbols[symbol] + "?pe" + symbols[symbol] + "&.tsrc=fin-srch"
        soup = get_page(the_url)
        the_symbol = symbols[symbol]
        stock_price = soup.select_one(f'fin-streamer[data-symbol="{the_symbol}"]')['value']
        print(symbols[symbol] + ": " + stock_price)


get_symbols()
get_stock_price()
