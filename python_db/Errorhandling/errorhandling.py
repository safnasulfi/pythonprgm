num1 = int(input("enter value of num1: "))
num2 = int(input("enter value of num2: "))

try:
    res=num1/num2
    print("result",res)
except Exception as e:
    print("exception occured")

print("db commit1")
print("db commit2")