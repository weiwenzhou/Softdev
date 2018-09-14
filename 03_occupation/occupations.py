# Wei Wen Zhou
# SoftDev1 pd8
# K#06: StI/O: Divine your Destiny!
# 2018-09-13

file = open("occupations.csv",'r')

info = file.read().split("\n")

file.close()
# Title line
info.pop(0)
# Last line : blank plus total
info.pop(len(info)-1)
info.pop(len(info)-1)


book = {}
for x in range(0,len(info)):
    if info[x].count(',') == 1:
        line = info[x].split(",")
        book[line[0]] = float(line[1])
    else: 
    # more than 1 comma
        lastC = info[x].rindex(',')
        book[info[x][0:lastC]] = float(info[x][lastC+1:len(info[x])-1])
#print (book)