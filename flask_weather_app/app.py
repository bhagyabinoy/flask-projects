from flask import Flask, request, render_template
import os, requests
from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)


@app.route('/', methods = ["GET", "POST"])
def index():
    if(request.method == 'GET'):
        return render_template("index.html")
    elif(request.method == 'POST'):
        user_zipcode = request.form.get("zip")
        user_country_code = request.form.get("country_code")
        openweather = requests.get("https://api.openweathermap.org/data/2.5/weather?zip={},{}&appid={}&units=imperial".format(user_zipcode, user_country_code, os.environ.get("API_KEY")))
        print(openweather,"###############")
        return render_template('weather.html', weather=openweather.json())

@app.route('/<zip>/<code>', methods = ["GET", "POST"])
def openweather_api():

    openweather = requests.get("https://api.openweathermap.org/data/2.5/weather?zip={},{}&appid={}".format(user_zipcode, user_country_code, os.environ.get("API_KEY")))
    print(openweather.json())

if __name__ == '__main__':
    app.run(debug=True)