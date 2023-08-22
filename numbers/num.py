f =open("C:\\Users\\safna\\PycharmProjects\\exam1\\numbers\\data.txt","w")

for num in range(1890,3001):
    f.write(str(num)+"\n")
print("process finished")
