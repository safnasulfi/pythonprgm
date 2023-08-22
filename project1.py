#sum of natural numbers

# n = int(input("enter the number: "))
# i = 1
# s = 0
# while i <= n:
#     s = s + i
#     i+= 1
# print("the sum of natural numbers upto",n,"is",s)

#print pattern

"""
pattern

        *
      *   *
    *   *   *
  *   *   *   *
*   *   *   *   *

"""
# n = int(input("enter the number of rows: "))
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(' ',end=' ')
#     for k in range(i):
#         print('*  ',end=' ')
#     print()

#print even and odd numbers of a list

# list1 = [1,2,3,4,5,6]
# even = []
# odd = []
# for i in list1:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("even numbers are: ",even)
# print("even numbers are: ",odd)

#print the reverse of a number 567

# n = 567
# reverse = 0
# a = n
# while a > 0:
#     n = a%10
#     reverse = reverse * 10 +n
#     a = a // 10
# print("reverse of",n,"is: ",reverse)

#find the least positive integer from the given list
# list = [2,3,4,6]
# for i in range(0,len(list)):
#     e1 = list[i]
#     e2 = list[i+1]
#     if e2 - e1 != 1:
#         print(e1+1,"is missing")
#         break

# lst = [2,3,4,5,6]
# for i in lst:
#     if i % 2 != 0:
#         print(i)

#listcomprehension

# lst = [2,3,4,5,6]
#
# odds = [num for num in lst if num % 2 != 0]
# print(odds)

# cubes = [num*3 for num in lst]
# print(cubes)

# divisibleby3 = [num for num in lst if num % 3 == 0 ]
# print(divisibleby3)

#nested list

# lst = [
#     [1,2],
#     [4,50],
#     [50,45]
# ]

# for ls in lst:
#     for num in ls:
#         print(num)

# for ls in lst:
#     for num in ls:
#         if num > 5:
#            print(num)

# gt5 = [num for ls in lst for num in ls if num > 5]
# print(gt5)

# mobiles=[
#     [100,"redminote12",23000,"5g"],
#     [101,"oneplusnord",32000,"5g"],
#     [102,"iphnoe14",123000,"5g"],
#     [103,"s23ultra",133000,"5g"],
#     [104,"pexel12",43000,"5g"],
#     [105,"nothing",13000,"4g"],
#     [106,"galaxya52",23000,"5g"]

#]

# print(len(mobiles))

# for mob in mobiles:
#     print(mob[1])

# mobilenames =[mob[1]  for mob in mobiles]
# print(mobilenames)

#print only 4g mobiles
# mobilenames = [mob[1] for mob in mobiles if mob[3] =="4g"]
# print(mobilenames)

#print mobiles <30000
# mobilenames = [mob[1] for mob in mobiles if mob[2] < 30000]
# print(mobilenames)

#print mobile in range of 30000 to 50000
# mobilenames = [mob[1] for mob in mobiles if mob[2] in range(30000,50000)]
# mobilenames = [mob[1] for mob in mobiles if mob[2] > 30000 and mob[2] < 50000]
# print(mobilenames)

#print all 5g mobiles under 25000
# mobilenames = [mob[1] for mob in mobiles if mob[3] == "5g" and mob[2] < 25000]
# print(mobilenames)

# items=[
#     [1,"potatto",45,"veg",10],
#     [2,"tomatto",40,"veg",20],
#     [3,"onion",35,"veg",0],
#     [4,"brinjal",50,"veg",0],
#     [5,"fish",145,"nonveg",10],
#     [6,"chicken",145,"nonveg",10],
#     [7,"egg",6,"nonveg",100]
#
# ]

# total number products
# print in stock product names
# print out of stock product names
# print veg category product names
# product available in range of 50-100
# veg products available in range of 40-80

# print(len(items))

# instock = [it[1] for it in items if it[4] != 0]
# print(instock)

# outofstock = [it[1] for it in items if it[4] == 0]
# print(outofstock)

# vegproduct = [it[1] for it in items if it[3] == "veg"]
# print(vegproduct)

# rangefltr = [it[1] for it in items if it[2] in range(50,100)]
# print(rangefltr)

# rangefltr = [it[1] for it in items if it[2] in range(40,80) and it[3] == "veg"]
# print(rangefltr)

