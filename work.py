teacher = {"id":10,"name":"sindhu","subject":"computer","class":10,"salary":25000}
if "subject" in teacher:
    print(teacher["subject"])
else:
    print("no such key present")

# print all key value pairs

for key in teacher:
    print(key,":",teacher[key])

# add a key  value pair

teacher["gender"] = "female"
print(teacher)

# salary decrement

teacher["salary"] -= 1000
print(teacher["salary"])



