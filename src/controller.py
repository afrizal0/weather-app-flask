from models import WeatherReport
import requests

class Controller():
	def getWeatherData(self, location, access_key):
		weather_data = requests.get(f"http://api.weatherstack.com/current?access_key={access_key}&query={location}")
		data = weather_data.json()
		country = data["location"]["country"
		temperature = data["current"]["temperature"]
		time = data["current"]["observation_time"]
		icon = data["current"]["weather_icons"]
		
		report = WeatherReport(location, country, time, temperature, icon)
		return report 


