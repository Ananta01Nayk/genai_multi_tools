from langchain_core.tools import tool
import requests
import os
from dotenv import load_dotenv

load_dotenv()

@tool
def get_stock_price(symbol: str) -> dict:
    """
    Fetch the latest stock price for a given stock symbol.

    Uses the Alpha Vantage API to retrieve real-time stock data.
    Example symbols: AAPL, TSLA, MSFT.

    Returns stock price information or a readable error message.
    """
    # ✅ CORRECT: use ENV VARIABLE NAME
    api_key = os.getenv("ALPHAVANTAGE_API_KEY")

    if not api_key:
        return {"error": "ALPHAVANTAGE_API_KEY is not set"}

    try:
        url = (
            "https://www.alphavantage.co/query"
            f"?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
        )

        response = requests.get(url, timeout=10)
        data = response.json()

        if "Note" in data:
            return {"error": "API rate limit exceeded. Please try again later."}

        if "Global Quote" not in data or not data["Global Quote"]:
            return {"error": f"No data found for symbol '{symbol}'"}

        return data

    except Exception as e:
        return {"error": str(e)}
