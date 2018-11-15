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
    KEY = "ba27b5fd166c4ca6a538cbb26de45975"
    URL_STUB = "https://services.last10k.com/v1/company/MSFT/quote?Subscription-Key="
    URL = URL_STUB + KEY
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

    return render_template("index.html", name=data['Name'], symbol=data["Symbol"], s_exchange=data["StockExchange"], high=data["DailyHigh"], low=data["DailyLow"], change=data["Change"])

if __name__ == "__main__":
    app.debug = True
    app.run()
