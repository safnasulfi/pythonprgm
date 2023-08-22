f = open("C:\\Users\\safna\\PycharmProjects\\exam1\\fwrite\\data.txt","w")

# f.write("python programming")
# print("process finished")

languages = [
    "python","java","c","c++"
]

for l in languages:
    f.write(l+"\n")
print("finished")