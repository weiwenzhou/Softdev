# Wei Wen Zhou
# SoftDev1 pd8
# K#06: StI/O: Divine your Destiny!
# 2018-09-13

file = open("occupation.csv",r)

info = file.read().split("\n")

file.close()
# Title line
info.pop(0)
# Last line
info.pop(len(info-1))


book = {}
for x in range(0,len(info)):
    line = info[x].split(",")
    book[line[0]] = line[1]

print book;