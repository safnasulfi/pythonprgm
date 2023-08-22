f = open("C:\\Users\\safna\\PycharmProjects\\exam1\\leapyr\\data.txt","w")
years = [
    2000,2024,1991,1200,1400,1234
]

# century yr divicible by 100 and 400
# non century yr %100 !=0 and divisible by 4
for y in years:
    if(y%100==0) and (y%400==0): #century?
        f.write(str(y)+"\n")
    elif(y%100!=0) and (y%4==0):
        f.write(str(y)+"\n")
print("finished")