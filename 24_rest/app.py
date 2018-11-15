'''
Wei Wen Zhou
SoftDev1 pd08
K24 -- A RESTful Journey Skyward
2018-11-13
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
    print("---------------")
	print("URL:")
	print(URL)
	print("---------------")
	u = request.urlopen(URL)
	response = u.read()
    print("---------------")
	print("response:")
	print(response)
	print("---------------")
	data = json.loads(response)
    
    return render_template("index.html", url=dict['url'])

if __name__ == "__main__":
    app.debug = True
    app.run()
