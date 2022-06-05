import requests, os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/weather')
def get_weather():
    print(os.getenv("LAT"))
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=metric&appid={}".format(os.getenv("LAT"), os.getenv("LON"), os.getenv("WEATHER_API_KEY")))
    return response.json()