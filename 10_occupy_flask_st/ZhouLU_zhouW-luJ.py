# ZhouLu - Wei Wen Zhou, Jack Lu
#SoftDev1 pd8
#K# 10: Jinja Tuning 
#2018-09-23 

from flask import Flask, render_template
from util import occupy


app = Flask(__name__)

# Root directory with link to table of occupations.
@app.route('/')
def index():
    return '<a href="./occupations">click this</a>'

# Calls buildDict to return the dictionary
# Calls chooseRandom to choose Occupation based on relative percentage
@app.route('/occupations')
def render():
    dict = occupy.buildDict('./data/occupations.csv')
    return render_template(
            'template.html',
            title = 'ZhouLu Corporation',
            rand = occupy.chooseRandom(dict),
            occupations = dict
            )

if __name__ == "__main__":
    app.debug = True
    app.run()