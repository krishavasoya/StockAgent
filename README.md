# 📈 Stock Research Agent

An AI-powered Stock Research Agent built using LangChain, Groq LLM, Streamlit, and FastAPI.

## Features

- Get real-time stock prices
- Fetch company fundamentals
- Fetch latest stock news
- AI-generated stock analysis
- Streamlit web interface
- FastAPI backend support

## Tech Stack

- Python
- LangChain
- Groq LLM
- Yahoo Finance (yfinance)
- Finnhub API
- Streamlit
- FastAPI

## Project Structure

stock_agent/
│
├── tools.py
├── agent.py
├── streamlit_app.py
├── app.py
├── requirements.txt
└── README.md

## Installation

Clone the repository:

```bash
git clone <your-github-repo-url>
cd stock_agent
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate virtual environment:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
FINNHUB_API_KEY=your_finnhub_api_key
```

## Run Streamlit App

```bash
streamlit run streamlit_app.py
```

## Run FastAPI

```bash
uvicorn app:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

## Future Improvements

- Stock charts
- PDF report generation
- Buy/Hold/Sell recommendations
- Multi-stock comparison
- LangGraph workflow

## Author

Krisha Vasoya
