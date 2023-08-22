movies=[
    {"language":"malayalam","name":"2018","rating":5,"year":2023,"genres":["mystery"]},
    {"language":"malayalam","name":"aadujeevitahm","rating":5,"year":2023,"genres":["fiction","drama"]},
    {"language":"malayalam","name":"neymar","rating":4,"year":2023,"genres":["action","comedy","romance"]},
    {"language":"malayalam","name":"sunny","rating":4,"year":2022,"genres":["drama","thriller"]},
    {"language":"malayalam","name":"12th man","rating":3,"year":2022,"genres":["drama","thriller"]},
    {"language":"thamil","name":"vikram","rating":5,"year":2022,"genres":["action","thriller"]},
    {"language":"thamil","name":"jai bhim","rating":5,"year":2021,"genres":["mystery","crime"]},
    {"language":"hindi","name":"pathaan","rating":5,"year":2023,"genres":["action","thriller"]},
    {"language":"telungu","name":"kgf","rating":15,"year":2018,"genres":["action","romance","thriller"]}

]

#q1 print all movie name

#q2 print filter movies with genre = mystery

#q3 top rated movie names

#q4 print malayalam movie names

#q5 movie names released in 2023

#q6 order movies with rating order by desc

#q1
# for mov in movies:
#     print(mov.get("name"))


# movies_name = [m.get("name") for m in movies]
# print(movies_name)

#q2
# for mov in movies:
#         if "mystery" in mov.get("genres"):
#             print(mov.get("name"))


# movie_mys = [mov.get("name") for mov in movies if "mystery" in  mov.get("genres")]
# print(movie_mys)

#q3
# top_rated_movies =  max(movies,key=lambda m:m.get("rating"))
# print(top_rated_movies)

#q4
# malayalam_movie_names = [m.get("name")for m in movies if m.get("language")=="malayalam"]
# print(malayalam_movie_names)

#q5
# year_filter =[m.get("name")for m in movies if m.get("year")==2023]
# print(year_filter)

#q6
#movie_sort = sorted(movies,reverse=True,key=lambda m:m.get("rating"))
# print(movie_sort)



