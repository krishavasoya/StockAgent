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
    model="openai/gpt-oss-120b",
    # api_key=os.getenv("GROQ_API_KEY")
    temperature=0
)
agent=create_agent(
    model=llm,
    tools=[get_stock_price,get_fundamentals,get_news],
    system_prompt="""
    you are a proffessional stock research analyst.

    use available tools whenever stock information is needed.

    provide:
    1.company overview
    2.Financial health
    3.Strengths and weaknesses
    4.Risks
    5.Overall opinion on the stock

    give whole report in easy language and short summary like 5 to 6 bullet points
"""
)

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
    
if __name__ == "__main__":
    symbol=input("Enter stock symbol: ")
    print(analyze_stock(symbol))

