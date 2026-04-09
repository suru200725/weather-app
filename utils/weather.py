import requests
from config import API_KEY, BASE_URL
from datetime import datetime


def get_weather(city):

    url = f"{BASE_URL}/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # 👉 PUT YOUR WEATHER DICTIONARY HERE
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind": data["wind"]["speed"],
            "icon": data["weather"][0]["icon"]
        }

        return weather

def get_forecast(city):

    url = f"{BASE_URL}/forecast?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        forecast_data = []

        for i in range(0, 40, 8):  # 5 days
            item = data["list"][i]

            date_obj = datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S")

            forecast_data.append({
                "date": date_obj.strftime("%A"),
                "temp": item["main"]["temp"],
                "description": item["weather"][0]["description"],
                "icon": item["weather"][0]["icon"]
            })

        return forecast_data

    else:
        print("Error fetching forecast")
        return None
    
    # else:
    #     print("Error fetching weather data")
    #     return None