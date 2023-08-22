f = open("C:\\Users\\safna\\PycharmProjects\\exam1\\users\\data.txt","r")
usr = {}
users = []

for line in f:
    text = line.rstrip("\n")
    name,followers,following = text.split(",")
    print(name,followers,following)
    usr["name"]["follower"] = name
print(usr)
