def  count_char(s: str, char: str) -> int:
    count = 0
    for i in s:
        if i.lower() == char.lower():
            count += 1
    return count

result = count_char("pppnnnefu","n")
print("จำนวนตัว 'n' ที่พบในข้อความ", result)