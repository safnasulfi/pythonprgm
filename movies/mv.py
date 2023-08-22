from json import load
with open("C:\\Users\\safna\\PycharmProjects\\exam1\\movies\\mdb.json") as f:
    data=load(f)

#total number of movies

# print(len(data))

#print all movie names

# allmvnames = [u.get("title") for u in data]
# print(allmvnames)

#print movie with highest duration

# maxduration = max(data,key=lambda m:int(m.get("runtime")))
# print(maxduration.get("title"))

# print all genres

# all_genres = [g.get("genres") for g in data]
# print(all_genres)

# yearwise movie count {1988:5,1984:3}

# print movie name which contain  genres comedy

# movie_com = [d.get("title") for d in data if "Comedy" in d.get("genres")]
# print(movie_com)

# print movie name which contain  genres comedy or Fantasy

#movie_cf = [d.get("title") for d in data if ["Comedy","Fantasy"] in d.get("genres")]
movie_cf =
print(movie_cf)

