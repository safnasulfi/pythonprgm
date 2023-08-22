#java var_name rule

#starts with alphabets
#special characters $ _
#length limit 1-10

from re import *
rule = "[a-zA-Z][a-zA-Z0-9$_]{0,10}"
var_name ="s"
matcher =fullmatch(rule,var_name)
if matcher == None:
    print("invalid")
else:
    print("valid")