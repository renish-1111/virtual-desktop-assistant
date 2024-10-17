import requests

API_KEY = "bd5e378503939ddaee76f12ad7a97608"
BASE_URL = "http://openweathermap.org/current"

def get_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather_description = data['weather'][0]['description']
        temperature = main['temp']
        return f"The weather in {city} is {weather_description} with a temperature of {temperature}°C."
    else:
        return "I couldn't fetch the weather information. Please try again later."
