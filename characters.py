import re
from re import *
text = "aabdXYZ$#098"

# [ab] either a or b


matcher = re.finditer("[^a-bA-B0-9]",text)
print(matcher)
for m in matcher:
    print(m.group())


# a-z == /w  [^a-z] ==/W
# 0-9 == /d  [^0-9] == /D
# space == /s
