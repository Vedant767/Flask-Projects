from flask import Flask, render_template, request
import urllib.request, json
from ..config import api_id
app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def weather():
    if request.method == "POST":
        cname = request.form.get("cname")
        url = f"https://api.openweathermap.org/data/2.5/weather?q={cname}&appid={api_id}"
        response = urllib.request.urlopen(url)
        data = response.read()
        dict = json.loads(data)
        return dict["weather"][0]["description"]
    return render_template("index.html")

if __name__=="__main__":
    app.run()