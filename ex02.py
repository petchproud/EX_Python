def is_palindrome(s: str) -> bool:
    clear = s.replace(" ","").lower()
    return clear == clear [::-1]
print(is_palindrome("pop"))