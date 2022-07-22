from flask import Flask, render_template, request, flash, Blueprint
import requests



views = Blueprint("views", __name__)

@views.route("/", methods=["POST", "GET"])
def home():
    API_KEY = "207aa44bccceada5026035fbc69941e4"
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    if request.method == "POST":
        city = ""
        weather = ""
        temp = 0
        city = request.form.get("city")
        request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
        response = requests.get(request_url)

        if response.status_code == 200:
            data = response.json()
            weather = data["weather"][0]["description"]
            temp = round(data["main"]["temp"] - 273.15, 2)
        else:
            flash("The city " + city + "is not supported, please try another one.")
    return render_template("home.html", weather = weather,temp = temp, city = city)