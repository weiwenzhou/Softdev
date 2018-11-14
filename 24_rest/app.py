from flask import Flask, render_template
import urllib.request, urllib.parse
import json

app = Flask(__name__)

@app.route("/")
def root():
    fd = urllib.request.urlopen("https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=DEMO_KEY")
    data = fd.read()
    dict = json.loads(data)
    
    return render_template("index.html", url=dict['url'])

if __name__ == "__main__":
    app.debug = True
    app.run()
