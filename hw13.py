#q1
text = "AABBCCCDE"
#PRINT MOST RECURSSIVE CHARACTER
wc={}
for t in text:
    if t in wc:
        wc[t]+=1
    else:
        wc[t]=1
print(wc)
lst = wc.values()
print(sorted(lst))

# for i in wc.values():
#     j = i + 1
#     for j in wc.values():
#         if  j>= i:
#             j+=1
#         else:
#             break
# print()

#q2
words = ["in","hello","pneumonoultra","good"]
print(min(words,key=lambda w:len(w)))



