lst = [10,11,10,11,12,13]
wc = {}
duplicate = set()
for num in lst:
    if num in wc:
        wc[num] += 1
        duplicate.add(num)
    else:
        wc[num] = 1
print(wc)
print("the duplicate numbers are :")
print(duplicate)