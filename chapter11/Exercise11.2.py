txt = "Load up on guns Bring your friends"
def count_letter(str):
    dic = {}
    for letter in txt:
        dic[letter] = 1 + dic.get(letter,0)
    return dic
print(count_letter(txt))
