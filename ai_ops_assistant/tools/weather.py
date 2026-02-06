from langchain_core.tools import tool
import requests
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(dotenv_path=Path(__file__).resolve().parents[1] / ".env")

@tool
def get_weather(city: str) -> dict:
    """
    Fetch current weather information for a given city.

    Uses OpenWeatherMap API to return temperature and weather condition.
    """
    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        return {"error": "OPENWEATHER_API_KEY is not set"}

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&units=metric&appid={api_key}"
    )

    try:
        res = requests.get(url, timeout=10).json()

        if "main" not in res:
            return {"error": "Weather data not found"}

        return {
            "city": city,
            "temperature_c": res["main"]["temp"],
            "condition": res["weather"][0]["description"]
        }

    except Exception as e:
        return {"error": str(e)}
