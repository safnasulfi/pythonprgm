from re import *
f = open("C:\\Users\\safna\\PycharmProjects\\exam1\\users\\data.txt","r")
valid_tyres = set()
rule = "[0-9]{3}[/][0-9]{2}[/][R][0-9]{2}[/][0-9]{2}[K,L,M,N,P,Q,R,S,T,U,H,V,W,Y]"
for id in f:
    id=id.rstrip("\n")
    matcher = fullmatch(rule,id)
    if matcher != None:
        valid_tyres.add(id)
print(valid_tyres)
