#แทนที่คำใน string
def replace_word(s: str, old: str, new: str) -> str:
    return s.replace(old,new)
print(replace_word("I love Java", "Java", "Python"))