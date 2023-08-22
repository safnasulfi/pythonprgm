w1 = input("enter word1 : ")
w2 = input("enter word2 : ")

#s_w1 = sorted(w1)
#s_w2 = sorted(w2)

# for i in w2:
#     for j in w1:
#         if i == j:
#             print(j,end=' ')


wc = {}

for c in w1:
    if c in wc:
        wc[c]+=1
    else:
        wc[c]=1

for w in w2:
    if w in wc and wc[w]>0:
        wc[w]-=1
    else:
        print("its not a kangaroo word")
        break
print(f"{w1} and {w2} is a kangaroo word")

