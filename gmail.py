import re
gmail=input("enter your gamil: ")
g=re.search("@gmail.com$",gmail)
if(g):
    print("it is valid......")
else:
    print("not valid....")