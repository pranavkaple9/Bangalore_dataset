import requests
import pandas as pd
import os
from datetime import datetime

API_KEY = os.getenv("API_KEY")
CITY = "Bangalore"

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

r = requests.get(url)
data = r.json()

row = {
"date": datetime.now().strftime("%Y-%m-%d"),
"temperature": data["main"]["temp"],
"humidity": data["main"]["humidity"],
"pressure": data["main"]["pressure"],
"wind_speed": data["wind"]["speed"],
"weather": data["weather"][0]["main"]
}

file = "weather_data.csv"

if os.path.exists(file):
    df = pd.read_csv(file)
    df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
else:
    df = pd.DataFrame([row])

df.to_csv(file, index=False)
print("Saved weather data")
