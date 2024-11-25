import requests
import pandas as pd
from datetime import datetime

API_KEY = "1720969d247faec50cd966e8ac0f922e"
CITY = "London"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

def fetch_weather_data():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        weather_data = []
        for entry in data["list"]:
            weather_data.append({
                "Temperature": entry["main"]["temp"],
                "Humidity": entry["main"]["humidity"],
                "Wind Speed": entry["wind"]["speed"],
                "Weather Condition": entry["weather"][0]["description"],
                "Date": entry["dt_txt"].split(" ")[0],
                "Time": entry["dt_txt"].split(" ")[1]
            })
        return weather_data
    else:
        print("Failed to fetch data.")
        return []

def save_data_to_csv(data, filename="raw_data.csv"):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    weather_data = fetch_weather_data()
    save_data_to_csv(weather_data)
    print("Weather data collected and saved.")
