from database import Database
from flask import Flask
from flask import render_template

app = Flask(__name__)

db = Database()


@app.route('/')
def get_weather():
    weather_data = db.get_weather_data()
    return render_template('weather.html', weather = weather_data)


if __name__ == '__main__':
    app.run(port=5000, debug=True)