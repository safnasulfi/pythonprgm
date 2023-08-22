f =open("C:\\Users\\safna\\PycharmProjects\\exam1\\fileinputoutput\\data.txt","r")

# for line in f:
#     print(line)
# words = []
# for line in f:
#     text = line.split(" ")
#     for w in text:
#         words.append(w)
# for w in words:
#      print(w)

words = set()
for line in f:
    text = line.split(" ")
    for w in text:
        words.add(w)
print(words)
