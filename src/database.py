import sqlite3


def create_db():
    conn = sqlite3.connect("weather_data.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS weather (
        city TEXT,
        date TEXT,
        temp_c REAL,
        condition TEXT,
        is_forecast INTEGER
    )
    """)
    conn.commit()
    conn.close()


def insert_weather_data(city, date, temp, condition, is_forecast):
    conn = sqlite3.connect("weather_data.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO weather (city, date, temp_c, condition, is_forecast) VALUES (?, ?, ?, ?, ?)",
                   (city, date, temp, condition, is_forecast))
    conn.commit()
    conn.close()


def get_avg_temp(cities, today):
    conn = sqlite3.connect("weather_data.db")
    cursor = conn.cursor()
    avg_temps = []
    for city in cities:
        cursor.execute("SELECT AVG(temp_c) FROM weather WHERE city = ? AND is_forecast = 0", (city,))
        avg_week_temp = cursor.fetchone()[0]

        cursor.execute("SELECT AVG(temp_c) FROM weather WHERE city = ? AND is_forecast = 1 AND date > ?",
                       (city, today.strftime("%Y-%m-%d")))
        avg_forecast_temp = cursor.fetchone()[0]

        avg_temps.append({
            "Город": city,
            "Средняя температура за неделю": avg_week_temp,
            "Средняя температура на следующие 3 дня": avg_forecast_temp
        })
    conn.close()
    return avg_temps
