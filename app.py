from fastapi import FastAPI
from agent import analyze_stock
from tools import get_stock_price,get_fundamentals,get_news

app=FastAPI(
    title="Stock Research Agent",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message":"Stock Agent API is running.."}

@app.get("/analyze/{symbol}")
def analyze(symbol : str):
    return{
        "price":get_stock_price.invoke({"symbol":symbol}),
        "fundamentals":get_fundamentals.invoke({"symbol":symbol}),
        "news":get_news.invoke({"symbol":symbol}),
        "analysis":analyze_stock(symbol)
    }
