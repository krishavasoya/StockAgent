from langchain_core.tools import tool
import yfinance as yf    #import yfinance library to get stock data
import requests  #import requests library to get news data used to call api
import os  #import os library to read variables of .env file
from dotenv import load_dotenv  #import load_dotenv to load environment variables from .env

load_dotenv()  #load environment variables from .env file
FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")  #get FINNHUB_API_KEY from environment variables

@tool
def get_stock_price(symbol: str):  #function for getting stock price of a given symbol
    """get current stock price"""  #helps sgent to understand when to use this tool
    stock=yf.Ticker(symbol)  #make a stock object using the symbol provided
    current_price=stock.fast_info.get("lastPrice")  #get current price of the stock
    
    if current_price is None:  #check if current price is None
        return{"error":"Invalid symbol or no data available"}
    

    return{
        "symbol": symbol,
        "current price":float(current_price)
    }

@tool
def get_fundamentals(symbol: str):  #function for getting fundamentals of a given symbol

    """Get company fundamental data such as revenue, net income, EPS,
      debt, profit margin, market cap, and P/E ratio."""
    stock=yf.Ticker(symbol)  #make a stock object using the symbol provided
    financials=stock.financials  #get financials of the stock
    balance_sheet=stock.balance_sheet  #get balance sheet of the stock

    revenue=financials.loc["Total Revenue"].iloc[0]  #get total revenue from financials
    net_income=financials.loc["Net Income"].iloc[0]  #get net income from financials
    eps=financials.loc["Diluted EPS"].iloc[0]  #get diluted EPS from financials
    total_debt=balance_sheet.loc["Total Debt"].iloc[0]  #get total debt from balance sheet
    profit_margin=(net_income/revenue)*100  #calculate profit margin
    market_cap=stock.fast_info['marketCap'] #get market cap from stock info

    current_price = stock.fast_info.get("lastPrice")
    PE_ratio = current_price / eps  
    

    return{
        "revenue":float(revenue),
        "net income":float(net_income),
        "eps":float(eps),
        "total debt":float(total_debt),
        "profit margin":float(profit_margin),
        "market cap":float(market_cap),
        "P/E ratio":float(PE_ratio)
      

    }
@tool
def get_news(symbol: str):  #function for getting news of a given symbol
    """Get the latest news headlines for a given stock symbol."""
    url = (
        f"https://finnhub.io/api/v1/company-news"
        f"?symbol={symbol.upper()}"
        f"&from=2026-01-01"
        f"&to=2026-12-31"
        f"&token={FINNHUB_API_KEY}"
    )
    response = requests.get(url)  #make a get request to the url
    news=response.json()  #get json response from the request
    # print("Total articles:", len(news))

    headlines=[]  #create an empty list to store headlines
    for article in news[:5]:  #loop through the news articles
        headlines.append(article['headline'])  #append the headline of each article to the list

    return headlines  #return the list of headlines

