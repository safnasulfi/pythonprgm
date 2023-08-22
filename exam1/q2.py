txt = "pycharm is an ide"
vowel_count = 0
consents_count = 0
num_of_characters = len(txt)
print("number of characters :",num_of_characters)
for c in txt:
    if (c == 'a' or c == 'e' or c == 'i' or
        c == 'o' or c == 'u' or c == 'A' or
        c == 'E' or c == 'I' or c == 'O' or
        c == 'U'):
        vowel_count += 1
    else:
        consents_count += 1
print("total number of vowels are :",vowel_count)
print("total num of consents are :",consents_count)

