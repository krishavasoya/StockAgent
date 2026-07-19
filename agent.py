#llm,tools,age
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from tools import get_stock_price,get_fundamentals,get_news
from langchain.agents import create_agent


from tools import(
    get_stock_price,
    get_fundamentals,   
    get_news
)
load_dotenv()  #load environment variables from .env file
llm=ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)
agent=create_agent(
    model=llm,
    tools=[get_stock_price,get_fundamentals,get_news],
    system_prompt="""
    you are a proffessional stock research analyst.

    use availab;e tools whenever stock information is needed.

    provide:
    1.company overview
    2.Financial health
    3.Strengths and weaknesses
    4.Risks
    5.Overall opinion on the stock

    give whole report in easy language and short summary like 5 to 6 bullet points
"""
)
# def analyze_stock(symbol):
#     price=get_stock_price(symbol)
#     fundamentals=get_fundamentals(symbol)
#     news=get_news(symbol)
    
    # prompt=f""" 
    # Analyze the stock symbol: {symbol}
    # Current price: {price}
    # Fundamentals: {fundamentals}
    # Recent News: {news}

    # Give:
    # 1.company overview
    # 2.Financial health
    # 3.Strengths and weaknesses
    # 4.Risks
    # 5.Overall opinion on the stock

    # Give a short summary in 6 to 7 bullet points with each point having 1-2 sentences and line breaks.
    # """

def analyze_stock(symbol):
    result=agent.invoke({
        "messages":[
            {
                "role":"user",
                "content": f"""
                Analyze stock {symbol}.

                Use the available tools to get:
                1. Current stock price
                2. Company fundamentals
                3. Latest news

                Then provide:
                - Company Overview
                - Financial Health
                - Strengths and Weaknesses
                - Risks
                - Overall Opinion
                """
            }
        ]
    })
    return result["messages"][-1].content
    

    
    # response=llm.invoke(prompt)
    # return response.content
if __name__ == "__main__":
    symbol=input("Enter stock symbol: ")
    print(analyze_stock(symbol))
