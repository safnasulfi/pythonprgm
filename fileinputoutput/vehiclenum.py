f1 = open("C:\\Users\\safna\\PycharmProjects\\exam1\\fileinputoutput\\vehicle.txt")
from re import *
kvalid = set()
tvalid = set()
krule = "[K][L][-][0-9]{2}[-][A-Z]{1,2}[-][0-9]{4}"
trule = "[T][N][-][0-9]{2}[-][A-Z]{1,2}[-][0-9]{4}"
for line in f1:
    num = line.rstrip("\n")
    matcher = fullmatch(krule,num)
    if matcher != None:
        kvalid.add(num)
    matcher = fullmatch(trule,num)
    if matcher != None:
        tvalid.add(num)
print(kvalid)
print(tvalid)

