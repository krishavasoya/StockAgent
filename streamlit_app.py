import streamlit as st
from agent import analyze_stock
from tools import get_stock_price,get_fundamentals,get_news
st.title("📈 Stock Research Agent")

st.set_page_config(
    page_title="Stock Research Agent",
    page_icon="📈",
    layout="wide"
)

# symbol = st.text_input(
#     "Enter Stock Symbol",
#     placeholder="Enter Stock symbol"
# )
companies={
    "Apple":"AAPL",
    "Microsoft":"MSFT",
    "Google":"GOOGL",
    "Amazon":"AMZN",
    "Tesla":"TSLA",
    "Meta":"META",
    "Nvidia":"NVDA",
    "JPMorgan Chase":"JPM",
    "Bank of America":"BAC",
    "Netflix":"NFLX",
    "Intel":"INTC",
    "Oracle":"ORCL",
    "Mastercard":"MA",
    "Walmart":"WMT",
    "Coca-Cola":"KO",
    "McDonald's":"MCD",
    "Disney":"DIS",
    "Nike":"NKE",
}
company=st.selectbox(
    "select a company",
    companies.keys(),
)
symbol=companies[company]
if st.button("Analyze"):
    price = get_stock_price.invoke({"symbol": symbol})
    fundamentals = get_fundamentals.invoke({"symbol": symbol})
    news = get_news.invoke({"symbol": symbol})

    st.subheader("Current Price:")
    st.json(price)

    st.subheader("Fundamentals:")
    st.json(fundamentals)

    st.subheader("Recent News:")
    st.json(news)
    for headline in news:
        st.write("•",headline)

    st.subheader("Analysis:")
    analysis = analyze_stock(symbol)

    st.write(analysis)