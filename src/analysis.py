import sqlite3
from config import cities
from database import get_avg_temp


def generate_recommendation(condition):
    if "rain" in condition.lower() or "drizzle" in condition.lower():
        return "Возьмите зонт"
    elif "snow" in condition.lower():
        return "Оденьте шапку и теплую одежду"
    elif "clear" in condition.lower():
        return "Хорошая погода, можно гулять"
    else:
        return "Одевайтесь по погоде"


def generate_recommendations(today):
    conn = sqlite3.connect("weather_data.db")
    cursor = conn.cursor()
    recommendations = []

    for city in cities:
        cursor.execute("SELECT temp_c, condition FROM weather WHERE city = ? AND date = ? AND is_forecast = 1",
                       (city, today.strftime("%Y-%m-%d")))
        temp, condition = cursor.fetchone()
        recommendations.append({
            "Город": city,
            "Температура сегодня": temp,
            "Условия": condition,
            "Рекомендация": generate_recommendation(condition)
        })
    conn.close()
    return recommendations
