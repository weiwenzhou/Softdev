# ZhouLu - Wei Wen Zhou, Jack Lu
#SoftDev1 pd8
#K# 10: Jinja Tuning 
#2018-09-23 

from flask import Flask, render_template
import random

app = Flask(__name__)


book = {}
# From ZhouDynasty work - #3
def pickOccupation():
    file = open("data/occupations.csv",'r')
    info = file.read().split("\n")
    file.close()
    
    info.pop(0) # Title line
    info.pop(len(info)-1) # Last line
    info.pop(len(info)-1) # again due to some issue with csv
    
    #print('info length:')
    #print(len(info))
    
    # Initialize dictionary
    for x in range(0,len(info)):
        if info[x].count(',') == 1:
            line = info[x].split(",")
            book[line[0]] = float(line[1])
        else: 
            # more than 1 comma
            lastC = info[x].rindex(',')
            book[info[x][0:lastC]] = float(info[x][lastC+1:len(info[x])])

    target = random.uniform(0, 99.8)
    current = 0

    for entry in book:
        current = current + book[entry]
        if current > target:
            return entry


@app.route('/')
def index():
    link = '<a href="./occupations">go here</a>'
    return link

@app.route('/occupations')
def occupy():
    return render_template(
            'template.html',
            job=pickOccupation(),
            collection=book)
            
if __name__ == "__main__":
    app.debug = True
    app.run()