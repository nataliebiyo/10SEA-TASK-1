# modules
import requests
import os
from time import sleep

api_key = "92a9583345190eb5de5047f027e13c67" # api key for open weather map
current_weather_endpoint = "https://api.openweathermap.org/data/2.5/weather" # api endpoint for current weather
forecast_endpoint = "http://api.openweathermap.org/data/2.5/forecast" # api endpoint for forecasted weather

def clear():
    os.system("cls")

def intro():
    print("\n--- NatalieWeather ---\n")
    enter = int(input("(1) for help / more info.\n(2) to continue\n\n---> "))
    while enter != 1 and enter != 2:
        enter = int(input("Please enter (1) or (2): "))
    if enter == 1:
        clear()
        print("\nWelcome to NatalieWeather!")
        sleep(2)
        print(" - NatalieWeather can find weather conditions and predicted forecasts from all over the world.\n")
        print("Here, you can find...\n - current temperature, conditions, what it feels like, humidity and a 5 day forecast.\n")
        sleep(3)
        print("You will be asked to choose a city and choose above options.\n - These results will be found and given to you!")
        sleep(3)
        read = input("\n\nPress ENTER to continue   ")

def access_data(endpoint, location): # accessing 
    weather_parameters = {
        "q": location,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(endpoint, params=weather_parameters)
    return response

def get_weather(response):
    if response.status_code == 200:
        data = response.json()
        return data

def give_forecast(): #retrieving all forecasted weather data
    print(f"FORECASTED WEATHER FOR THE NEXT 5 DAYS...")
    forecast_list = forecast_data["list"]
    day = 0
    while day < 5:
        print(f"Temperature: {forecast_list[day]['main']['temp']}°C\nConditions: {forecast_list[day]['weather'][0]['description']}\n")
        day += 1 # ends while loop when 5 rounds of forecasted weather is printed

intro() # calls intro menu 
clear() # clear screen
city_name = input("\nEnter city name: ") # user input for location
print()

current_weather_response = access_data(current_weather_endpoint, city_name)
forecast_response = access_data(forecast_endpoint, city_name)

while current_weather_response.status_code != 200 or forecast_response.status_code != 200: # handles error incase invalid request occurs
    print("City not in data")
    city_name = input("City not found! Enter city name: ")
    print()
    current_weather_response = access_data(current_weather_endpoint, city_name)
    forecast_response = access_data(forecast_endpoint, city_name)

current_weather_data = get_weather(current_weather_response)
forecast_data = get_weather(forecast_response)

# retrieving all current weather data
current_temp = current_weather_data["main"]["temp"]
current_conditions = current_weather_data["weather"][0]["description"]
feels_like = current_weather_data["main"]["feels_like"]
humidity = current_weather_data["main"]["humidity"]

# print all above variables showing current weather
print(f"CURRENTLY...\nCurrent Temperature: {current_temp}°C\nCurrent Conditions: {current_conditions}\nFeels Like: {feels_like}°C\nHumidity:{humidity}%\n")
give_forecast()