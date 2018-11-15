'''
Wei Wen Zhou
SoftDev1 pd08
K25 -- Getting More REST
2018-11-14
'''

from urllib import request
import json

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def root():
    #KEY_NASA = "DEMO_KEY"
    KEY_NASA = "L1NmAHRWyqjuPbhLPAKh6b7R2MEaTqtiMKCLaLd0"
    URL_STUB = "https://api.nasa.gov/planetary/apod?api_key="
    URL = URL_STUB + KEY_NASA
    fd = request.urlopen(URL)
    data = fd.read()
    dict = json.loads(data)
    
    return render_template("index.html", url=dict['url'])

if __name__ == "__main__":
    app.debug = True
    app.run()
