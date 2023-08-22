import re
mob = input("enter the mobile number with country code")
x = re.search("^[+]91",mob)
if (x):
    print("number is indian")
else:
    print("number is not indian")