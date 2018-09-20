# Double Z Dyanasty - Wei Wen Zhou, Thomas Zhao
# SoftDev1 pd8
# K#06: StI/O: Divine your Destiny!
# 2018-09-13

import random

def pickOccupation():
    file = open("occupations.csv",'r')
    info = file.read().split("\n")
    file.close()
    
    info.pop(0) # Title line
    info.pop(len(info)-1) # Last line
    info.pop(len(info)-1) # again due to some issue with csv
    
    #print('info length:')
    #print(len(info))
    
    # Initialize dictionary
    book = {}
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

print(pickOccupation())
