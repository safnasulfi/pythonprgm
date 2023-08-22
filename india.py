from re import *
rule = "[A-Z]{2}[-][0-9]{2}[-][A-Z]{2}[-][0-9]{4}"
var_name ="TN-17-BN-2423"
matcher =fullmatch(rule,var_name)
if matcher == None:
    print("invalid")
else:
    print("valid")
