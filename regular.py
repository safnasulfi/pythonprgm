# sen = "joel is a very good student in may batch"
# words = sen.split(" ")

# print(sen.startswith("joel"))
# bol = sen.startswith("joel")
# print(bol)
# if bol == True:
#     print("the sentence is starting with 'joel'")
# if words[0] == "joel":
#     print("the sentence is starting with 'joel'")

# import packageName
import re
sen = "joel is a very good student in may batch"
x = re.search("^Joel",sen)
y = re.search("^joel",sen)
print(x)
print(y)