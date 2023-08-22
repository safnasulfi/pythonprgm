f1 = open("C:\\Users\\safna\\PycharmProjects\\exam1\\fileinputoutput\\atten.txt")
f2 = open("C:\\Users\\safna\\PycharmProjects\\exam1\\fileinputoutput\\presnt.txt")

total = set()
present = set()
for line in f1:
    total.add(line.rstrip("\n"))
print(total)

for line in f2:
    present.add(line.rstrip("\n"))
print(present)

absent = total-present
print(absent)
