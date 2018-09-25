# ZhouLu - Wei Wen Zhou, Jack Lu
#SoftDev1 pd8
#K# 10: Jinja Tuning 
#2018-09-23 

from flask import Flask, render_template
import csv
import random

app = Flask(__name__)

# Builds dictionary of occupations and corresponding percentage of workforce.
def buildDict(filename):
    d = {}
    with open(filename, 'rt') as csvfile:
        reader = csv.reader(csvfile)
        first = reader.__next__() # Processes column labels Job Class, Percentage
        d[first[0]] = first[1]
        for i in reader:
            d[ i[0] ] = float( i[1])
    return d

# Choose random job based on percentage
def chooseRandom(dictionary):
    jobList = list(dictionary.keys()) # list of jobs
    chanceList = list(dictionary.values()) # list of percentages
    # Ignores first and last rows (heading and total)
    randJob = random.choices(jobList[1:-1], chanceList[1:-1])[0]
    return randJob

# Root directory with link to table of occupations.
@app.route('/')
def index():
    return '<a href="./occupations">click this</a>'

# Calls buildDict to return the dictionary
# Calls chooseRandom to choose Occupation based on relative percentage
@app.route('/occupations')
def render():
    dict = buildDict('./data/occupations.csv')
    return render_template(
            'template.html',
            title = 'ZhouLu Corporation',
            rand = chooseRandom(dict),
            occupations = dict
            )

if __name__ == "__main__":
    app.debug = True
    app.run()