words = ["hello","hai","hello","hai","good","morning","evening"]
#word count

ws = {}
for word in words:
    if word in ws:
        ws[word] += 1
    else:
        ws[word] = 1
print(ws)

# st = {"run","run","toy","car","toy"}



