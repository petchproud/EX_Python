from collections import Counter
def duplicate_chars(s: str) -> dict:
    counts = Counter(s)

    return {char: count for char, count in counts.items() if count > 1}

print(duplicate_chars("programming")) 
print(duplicate_chars("hello world"))   
print(duplicate_chars("abc")) 