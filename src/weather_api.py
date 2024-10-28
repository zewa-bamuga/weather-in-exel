import requests
from config import BASE_URL, HEADERS


def get_weather_forecast(city):
    url = f"{BASE_URL}/forecast.json"
    params = {"q": city, "days": 3}
    response = requests.get(url, headers=HEADERS, params=params)
    return response.json()


def get_historical_weather(city, date):
    url = f"{BASE_URL}/history.json"
    params = {"q": city, "dt": date}
    response = requests.get(url, headers=HEADERS, params=params)
    return response.json()
