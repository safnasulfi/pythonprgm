data = {"django":"framework",
        "react":"library",
        "fastapi":"framework",
        "vue":"framework",
        "ajax":"library"}

#o/p: {'framework': 3, 'library': 2}
values =data.values()
wc={}
for v in values:
    if v in wc:
        wc[v]+= 1
    else:
        wc[v] = 1
print(wc)

#o/p: {'framework': ['django', 'fastapi', 'vue'], 'library': ['react', 'ajax']}
wc = {}
for k,v in data.items():
    if v in wc:
        wc[v].append(k)
    else:
        wc[v] =[k]
print(wc)
