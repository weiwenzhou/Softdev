'''
Wei Wen Zhou
SoftDev1 pd08
K26 -- Getting More REST
2018-11-16
'''

from urllib import request
import json

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def root():
    URL = "https://ghibliapi.herokuapp.com/films/58611129-2dbc-4a81-a72f-77ddfc1b1b49"
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
    
    URL0 = data["species"][2]
    print("---------------")
    print("URL0:")
    print(URL0)
    print("---------------")
    u0 = request.urlopen(URL0)
    response0 = u0.read()
    print("---------------")
    print("response0:")
    print(response0)
    print("---------------")
    data0 = json.loads(response0)
    
    URL1 = "https://catfact.ninja/fact"
    print("---------------")
    print("URL1:")
    print(URL1)
    print("---------------")
    u1 = request.urlopen(URL1)
    response1 = u1.read()
    print("---------------")
    print("response1:")
    print(response1)
    print("---------------")
    data1 = json.loads(response1)
    
    URL2 = "https://http.cat/100"
    '''
    print("---------------")
    print("URL2:")
    print(URL2)
    print("---------------")
    u2 = request.urlopen(URL2)
    response2 = u2.read()
    print("---------------")
    print("response2:")
    print(response2)
    print("---------------")
    data2 = json.loads(response2)
    '''
    return render_template("index.html", title=data['title'], name=data0["name"], classtype=data0["classification"], fact=data1["fact"], url=URL2)

if __name__ == "__main__":
    app.debug = True
    app.run()
