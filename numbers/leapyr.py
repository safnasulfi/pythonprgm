fread = open("C:\\Users\\safna\\PycharmProjects\\exam1\\numbers\\data.txt","r")

fwrite = open("C:\\Users\\safna\\PycharmProjects\\exam1\\numbers\\lyear.txt","w")

for y in fread:
     year =int(y.rstrip("\n"))
     if(year%100==0) and (year%400==0):
         fwrite.write(str(year)+"\n")
     elif(year%100!=0) and (year%4==0):
         fwrite.write(str(year)+"\n")
print("process finished")

