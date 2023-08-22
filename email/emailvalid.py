from re import *
f = open("C:\\Users\\safna\\PycharmProjects\\exam1\\email\\data.txt")
valid_email = set()
rule = "[a-zA-Z0-9][a-zA-Z0-9_$#]*[@]gmail[.]com"
for id in f:
    id = id.rstrip("\n")
    matcher = fullmatch(rule,id)
    if matcher != None:
        valid_email.add(id)
print(valid_email)

