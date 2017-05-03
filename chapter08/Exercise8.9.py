def is_palindrome(word):
    if word[::-1].find(word) ==-1:
        return False
    else:
        return True
print(is_palindrome("noooob"))
