# modules
import requests

api_key = "92a9583345190eb5de5047f027e13c67" # api key for open weather map
current_weather_endpoint = "https://api.openweathermap.org/data/2.5/weather" # api endpoint for current weather
forecast_endpoint = "http://api.openweathermap.org/data/2.5/forecast" # api endpoint for forecasted weather

city_name = input("\nENTER CITY NAME: ") # user input for location
print()

def access_data(endpoint, location): # accessing 
    weather_parameters = {
        "q": location,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(endpoint, params=weather_parameters)
    return response
current_weather_response = access_data(current_weather_endpoint, city_name)
forecast_response = access_data(forecast_endpoint, city_name)

while current_weather_response.status_code != 200 or forecast_response.status_code != 200: # handles error incase invalid request occurs
    print("ERROR - INVALID REQUEST")
    city_name = input("\nENTER CITY NAME: ")
    print()
    current_weather_response = access_data(current_weather_endpoint, city_name)
    forecast_response = access_data(forecast_endpoint, city_name)

def get_weather(response):
    if response.status_code == 200:
        data = response.json()
        return data
current_weather_data = get_weather(current_weather_response)
forecast_data = get_weather(forecast_response)

# retrieving all current weather data
current_temp = current_weather_data["main"]["temp"]
current_conditions = current_weather_data["weather"][0]["description"]
feels_like = current_weather_data["main"]["feels_like"]
humidity = current_weather_data["main"]["humidity"]

# print all above variables showing current weather
print(f"CURRENTLY...\nCurrent Temperature: {current_temp}°C\nCurrent Conditions: {current_conditions}\nFeels Like: {feels_like}°C\nHumidity:{humidity}%\n")

#retrieving all forecasted weather data
print(f"FORECASTED WEATHER FOR THE NEXT 5 DAYS...")
forecast_list = forecast_data["list"]
count = 0
while count < 5:
    print(f"Temperature: {forecast_list[count]['main']['temp']}°C\nConditions: {forecast_list[count]['weather'][0]['description']}\n")
    count += 1 # ends while loop when 5 rounds of forecasted weather is printed