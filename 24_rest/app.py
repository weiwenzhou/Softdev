from flask import Flask, render_template
from urllib import request
import json

app = Flask(__name__)

fd = urllib.request.urlopen("https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=DEMO_KEY")

@app.route("/")
def root():
    return render_template("index.html", )

if __name__ == "__main__":
    app.debug = True
    app.run()
