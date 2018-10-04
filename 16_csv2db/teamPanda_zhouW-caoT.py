#team Panda - Wei Wen Zhou, Tania Cao
#SoftDev1 pd8
#K #16: No Trouble
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect("foo.db") #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

command = "CREATE TABLE courses (name TEXT, mark INTEGER, id INTEGER);"


with open('courses.csv') as file:
    courses = csv.DictReader(file)
    for row in courses:
        command += "INSERT INTO courses values {" + row['code'] + "," + row['
        print(row['code'], row['mark'])
        
c.execute(command)    #run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database


