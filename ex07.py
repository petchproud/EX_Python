#ตวจสอบว่าเป็น anagram (คือคำที่มีตัวอักษรเหมือนกันทุกตัวแต่เรียงลำดับต่างกัน)
#วิธีที่ 1
def is_anagram(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)    #sorted() คือ ใช้เรียงลำดับข้อมูล

print(is_anagram("listen", "silent"))  
print(is_anagram("hello", "world"))  
print(is_anagram("race", "care"))     

#วิธีที่ 2
from collections import Counter
def is_anagram(s1: str, s2: str) -> bool:
    return Counter(s1) == Counter(s2)

print(is_anagram("listen", "silent"))  
print(is_anagram("hello", "world"))    
print(is_anagram("race", "care"))