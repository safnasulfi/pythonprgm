#method inside dict
#list =(append,pop,insert,extend clear)
#SET =(add,union,difference,intersection)
#tuple(count,)
# all utility classes and functions are defined in builtins.py

student={"rollno":1234,"name":"hari","age":21,"course":"mca"}
print(student.values())
print(student.keys())
print(student.items()) #print keys ansd values

for k,v in student.items():
    print(k,v)

#get(key) fetching value with key
#print(student["name"])
print(student.get("name"))

# pop(key)
student.pop("course")
print(student)

