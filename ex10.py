def caesar_cipher(s: str, shift: int) -> str:
    result = []
    for char in s:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            pos = ord(char) - base
            new_pop = (pos + shift) % 26
            new_char = chr(base + new_pop)
            result.append(new_char)
        else:
            result.append(char)
    
    return ''.join(result)

print(caesar_cipher("abc", 3))     
print(caesar_cipher("XYZ", 2))      
print(caesar_cipher("Hello, World!", 5)) 