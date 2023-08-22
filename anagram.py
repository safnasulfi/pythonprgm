word1 = input("enter a string: ")
word2 = input("enter another string: ")
# w =list(word1)
# i =list(word2)
#
# w1.sort()
# w2.sort()
# if w1 == w2:
#     print("anagram")
# else:
#     print("not anagram")


#another method

srt_word1 = sorted(word1)
srt_word2 = sorted(word2)

if srt_word1 == srt_word2:
    print("anagram")
else:
    print("not anagram")
