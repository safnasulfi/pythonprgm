
# st = set()
# print(st)

# st = {10,20,"hello","hai",True}
# for ele in st:
#     print(ele)

# print(dir(list))

# print(dir(set))

# st = {1,2,3,4,5}
# st.add(6)
# print(st)

#conversion of listt to set
# lst = [1,2,3,4,5,6]
# st = set(lst)
# print(st)

# st1 = {10,11,12,13}
# st2 = {10,12,25,30}

#union intersection difference

# union_set = st1.union(st2)
# print(union_set)

# intersection_set = st1.intersection(st2)
# print(intersection_set)

# diff_set = st1.difference(st2)
# print(diff_set)

# lst = [10,20,10,20,12,13,14]
# st = set(lst)
# lst1 = list(st)
# print(lst1)

#suggestions for dq

# allusers = ["mohanlal","fahad","dq","vijay","nivin","asif"]
# dq_friendslist = ["mohanlal","fahad","asif"]
# asif_friendslist = ["mohanlal","fahad","nivin","vijay"]
# st1 = set(allusers)
# st2 = set(dq_friendslist)
# st3 = st1.difference(st2)
# sugg = list(st3)
# sugg.remove("dq")
# print(sugg)


# dq => asif ? mutual friends

# st1 = set(asif_friendslist)
# st2 = set(dq_friendslist)
# st3 = st1.difference(st2)
# mutual = list(st1.intersection(st2))
# print(mutual)

# word = "pneumonoultramicroscopicsilicovolcanoconiosis"
# ccount = 0
# vcount = 0
# vowels = {'a','e','i','o','u','A','E','I','O','U'}
# for ch in word:
#     if ch in vowels:
#         vcount+=1
#     else:
#         ccount += 1
# print("total number of vowels: ",vcount)
# print("total number of consonants: ",ccount)
#set is immutable but can be updated using another set
# st1 = {10,20}
# st2 = {30,40}
# st1.update(st2)
# print(st1)
