from config import cities
from weather_api import get_historical_weather, get_weather_forecast
from database import create_db, insert_weather_data, get_avg_temp
from analysis import generate_recommendations
from excel_report import save_to_excel
from datetime import datetime, timedelta

create_db()

today = datetime.today()
for city in cities:
    for days_ago in range(1, 8):
        date = (today - timedelta(days=days_ago)).strftime("%Y-%m-%d")
        data = get_historical_weather(city, date)
        temp = data["forecast"]["forecastday"][0]["day"]["avgtemp_c"]
        condition = data["forecast"]["forecastday"][0]["day"]["condition"]["text"]
        insert_weather_data(city, date, temp, condition, is_forecast=0)

    forecast_data = get_weather_forecast(city)
    for day in forecast_data["forecast"]["forecastday"]:
        date = day["date"]
        temp = day["day"]["avgtemp_c"]
        condition = day["day"]["condition"]["text"]
        insert_weather_data(city, date, temp, condition, is_forecast=1)

recommendations = generate_recommendations(today)

avg_temps = get_avg_temp(cities, today)
save_to_excel(recommendations, avg_temps)
