#ask user for stock symbol and return the stock price, fundamentals, and news.
# run agent and print report

from agent import analyze_stock
from tools import get_stock_price, get_fundamentals,get_news


symbol = input("Enter stock symbol: ")
print(analyze_stock(symbol))
# price_data=(get_stock_price(symbol))
# for key, value in price_data.items():
#     print(f"{key}: {value}")

# fundamentals=(get_fundamentals(symbol))
# for key, value in fundamentals.items():
#     print(f"{key}: {value}")

# news=(get_news(symbol))
# print("\nLatest News Headlines:")
# for headline in news:
#     print(f"- {headline}")
