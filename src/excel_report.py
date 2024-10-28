from openpyxl import Workbook
import os


def save_to_excel(recommendations, avg_temps):
    wb = Workbook()
    ws = wb.active
    ws.title = "Погода и рекомендации"

    ws.append(["Город", "Температура сегодня", "Условия", "Рекомендация"])
    for rec in recommendations:
        ws.append([rec["Город"], rec["Температура сегодня"], rec["Условия"], rec["Рекомендация"]])

    ws2 = wb.create_sheet("Средние температуры")
    ws2.append(["Город", "Средняя температура за неделю", "Средняя температура на следующие 3 дня"])
    for avg in avg_temps:
        ws2.append([avg["Город"], avg["Средняя температура за неделю"], avg["Средняя температура на следующие 3 дня"]])

    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(parent_dir, "weather_report.xlsx")

    wb.save(file_path)
    print(f"Файл сохранён: {file_path}")
