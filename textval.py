# import re
# text1 = "abababab"
# text2 = "aaaabbbbbccc"
# t1 = re.search("[a]{4}",text1)
# t2 = re.search("[a]{4}",text2)
# print(t1)
# print(t2)

# import re
# text3 = "abcd1234"
# check = re.search("[a-z]{4}",text3)
# print(check)

#mobile number verifiction +91 other 10 positions digits?
import re
stri = "3457abDARG5643"
s = re.search("[a-z]{2}[A-Z]{4}",stri)
print(s)

