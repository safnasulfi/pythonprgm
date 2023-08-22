
tweets="What a game , hats off to both teams . Well done @benstokes38 @patcummins30 you have bought test cricket back to life. Love test cricket  @TheBarmyArmy @CricketAus @ECB_cricket"
words = tweets.split()
from  re import *
rule = "[@][a-z0-9]+"
for w in words:
    matcher =finditer(rule,w)
    if matcher != None:
        print(w)

