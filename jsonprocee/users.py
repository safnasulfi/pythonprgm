from json import load

with open("C:\\Users\\safna\\PycharmProjects\\exam1\\jsonprocee\\data.json","r") as f:
    data = load(f)

names = [u.get("name") for u in data]
print(names)


#student with highest mark
#lst=[10,30,40]

candidate = max(data,key=lambda s:s.get("total"))
print(candidate)

#sort all students with tal order by desc

# out = sorted(data.reverse=True,key=lambda s:s.get("total"))
# print(out)


#print bca student names
bca_students = [u.get("name") for u in data if u.get("course")=="bca"]
print(bca_students)


