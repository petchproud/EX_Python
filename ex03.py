#สลับตัวพิมพ์
#วิธีที่ 1
def swap_case(s: str) -> str:
    return s.swapcase()

print(swap_case("Hello World"))


#วิธีที่ 2
def swap_case(s: str) -> str:
    result = ""
    for char in s:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char
    return result
print(swap_case("Hello World"))
# .swapcase() เป็นเมธอดของ string ที่จะ แปลงตัวพิมพ์ใหญ่ → พิมพ์เล็ก , แปลงตัวพิมพ์เล็ก → พิมพ์ใหญ่ ทีละตัว