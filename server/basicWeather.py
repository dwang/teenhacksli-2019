import requests
import json
api_key = "708ca3f25f4dfda3c791b09ef4f990aa"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name
city_name = "Long Island"

# complete_url variable to store
# complete url address


def getWeather():


    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        return "City = " + city_name + "</br>"+  " Temperature = " + str(round(current_temperature + -273.15, 2)) + " Celsius</br> atmospheric pressure = " + str(current_pressure) + " hPa</br> humidity = " + str(current_humidiy) + "%</br> description = " + str(weather_description)

    else:
        return " City Not Found "
