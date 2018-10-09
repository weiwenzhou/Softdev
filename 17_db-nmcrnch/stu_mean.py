#Jiggumbob - Wei Wen Zhou, Soojin Choi 
#SoftDev1 pd8
#K #17: Average
#2018-10-05

# Jiggumbob - a thingamabob; a gadget; a whatsit; a gewgaw 

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect("foo.db") #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

#Look up each student’s grades
def gradeLookup(id):
    command = "SELECT courses.name, mark FROM peeps, courses WHERE peeps.id = {0} AND courses.id = {0}".format(id)
    c.execute(command)
    grades = "Grades of {0}\n".format(id)
    for each in c:
        grades += "{0}, {1}\n".format(each[0], each[1])
    return grades
    
print(gradeLookup(2))

#Compute each student’s average
def getAverage(id):
    command = "SELECT mark FROM peeps, courses WHERE peeps.id = {0} AND courses.id = {0}".format(id)
    c.execute(command)
    total = 0.0
    count = 0
    for each in c:
        total += each[0]
        count += 1
    return total/count

print(getAverage(2))
    
#Display each student’s name, id, and average
def display():
    command = "SELECT * FROM peeps"
    c.execute(command)
    table = "Name, id, average\n"
    for each in c:
        table += "{0}, {1}, {2}\n".format(each[0], each[2], getAverage(each[2]))
        command = "SELECT * FROM peeps"
        c.execute(command)
    return table

print(display())
    
#Create a table of IDs and associated averages, named "peeps_avg"
def createTable():
    command = "CREATE TABLE peeps_avg (id INTEGER, avg INTEGER);"
    

#Facilitate adding rows to the courses table



#==========================================================

db.commit() #save changes
db.close()  #close database