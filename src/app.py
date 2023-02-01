from flask import Flask, render_template, request
from controller import Controller

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html') 

@app.route('/weather', methods=['GET', 'POST'])
def weather():
	location = request.form['location']
	access_key = request.form['access_key']
	wr = Controller()
	weather_data = wr.getWeatherData(location, access_key)
	return render_template('weather.html', weather=weather_data)

if __name__ == '__main__':
	app.run(debug=True)
