#vehicle number plate

#starts with KL
#-
#2 digits
#-
#alphabet 2
# -
#number 4

from re import *
rule = "[K][L][-][0-9]{2}[-][A-Z]{2}[-][0-9]{4}"
var_name ="KL-17-BN-2423"
matcher =fullmatch(rule,var_name)
if matcher == None:
    print("invalid")
else:
    print("valid")
