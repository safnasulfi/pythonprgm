from re import *
text = "luminar techno lab luminar techno hub"
matcher = finditer("luminar",text)
count = 0
for m in matcher:
    print(m.start())#position aryan
    count+=1
print(count)