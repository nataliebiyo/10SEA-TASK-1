# modules
import requests
import os
from time import sleep
from yachalk import chalk

api_key = "92a9583345190eb5de5047f027e13c67" # api key for open weather map
current_weather_endpoint = "https://api.openweathermap.org/data/2.5/weather" # api endpoint for current weather
forecast_endpoint = "http://api.openweathermap.org/data/2.5/forecast" # api endpoint for forecasted weather
user_history = []
app = True

def clear(): # clears page
    os.system("clear") # "cls" for windows

def line(): # divides sections for user readability
    print("\n-----------------------------------------------------\n") 

def intro():
    clear()
    print(chalk.cyan.bold("\n--- NatalieWeather ---\n"))
    enter = int(input(chalk.blue("(1)") + " for help / more info\n" + chalk.blue("(2)") + " to continue\n\n---> "))
    
    while enter != 1 and enter != 2:
        enter = int(input(chalk.red.bold("\n\n (!)  ") + ("Please enter") + chalk.blue(" (1) ") + "or" + chalk.blue(" (2)") + "\n\n---> "))
    
    if enter == 1:
        clear()
        print("\nWelcome to NatalieWeather!")
        sleep(2)
        print(" - NatalieWeather can find weather conditions and predicted forecasts from all over the world.\n")
        print("Here, you can find...\n - current temperature, conditions, what it feels like, humidity and a 5 day forecast.\n")
        sleep(3)
        print("You will be asked to choose a city and choose from forecast and conditions.\n - These results will be found and given to you!")
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

def give_forecast(location): #retrieving all forecasted weather data
    line()  
    print(f"FORECASTED WEATHER FOR THE NEXT 5 DAYS IN {location}...")
    forecast_list = forecast_data["list"]
    day = 0

    while day < 5:
        print(f" Temperature: {forecast_list[day]['main']['temp']}°C\n Conditions: {forecast_list[day]['weather'][0]['description']}")
        day += 1 # ends while loop when 5 rounds of forecasted weather is printed

def give_weather(location): # retrieving all current weather data
    line()
    list = []

    current_temp = current_weather_data["main"]["temp"]
    current_conditions = current_weather_data["weather"][0]["description"]
    feels_like = current_weather_data["main"]["feels_like"]
    humidity = current_weather_data["main"]["humidity"]

    # print all above variables showing current weather
    print(f"CURRENTLY IN {location}...\n Current Temperature: {current_temp}°C\nCurrent Conditions: {current_conditions}\n Feels Like: {feels_like}°C\n Humidity: {humidity}%")

def continue_options():
    global app
    line()
    print("Look at another city? \n (1) Continue \n (2) Exit \n (0) User History")
    cont = int(input(" ---> "))

    while cont != 1 and cont != 2 and cont != 0:
        line()
        print(chalk.red.bold("(!)  ") + "\Sorry! Please choose from (1) , (2) or (0)")
        cont = int(input("  ---> "))
    clear()
    line()

    if cont == 1:
        #clear()
        pass
    elif cont == 2:
        app = False
        #clear()
        line()
        print("Thank you for choosing NatalieWeather!")
        line()
    elif cont == 0:
        #clear()
        print("User History This Session:")
        print(user_history)
        continue_options()

intro() # calls intro menu 
clear() # clear screen
line()

while app == True:
    city_name = input("\nEnter city name: ") # user input for location
    location = city_name.upper()
    user_history.append(location)
    line()
    current_weather_response = access_data(current_weather_endpoint, city_name)
    forecast_response = access_data(forecast_endpoint, city_name)

    while current_weather_response.status_code != 200 or forecast_response.status_code != 200: # handles error incase invalid request occurs
        city_name = input("City not found! Enter city name: ")
        print()
        current_weather_response = access_data(current_weather_endpoint, city_name)
        forecast_response = access_data(forecast_endpoint, city_name)
    
    print(chalk.gray("Choose from (1) , (2) or (0)\n\n") + "To find --\n  Weather: press (1) and ENTER\n  Forecast: press (2) and ENTER\n  Weather and Forecast: press (0) and ENTER")
    users_request = int(input("\nPlease enter (1) , (2) or (0):  "))

    while users_request != 1 and users_request != 2 and users_request != 0:
        line()
        print(chalk.red.bold("(!)  ") + "Sorry! Please choose from (1) , (2) or (0)")
        users_request = int(input("  ---> "))

    current_weather_data = get_weather(current_weather_response)
    forecast_data = get_weather(forecast_response)
    clear()

    if users_request == 1:
        give_weather(location=location)
    elif users_request == 2:
        give_forecast(location=location)
    else:
        give_weather(location=location)
        give_forecast(location=location)
    continue_options()

# DO USER HISTORY 