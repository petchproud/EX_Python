def sorted_vowel_words(word_list):
    vowels = "aeiouAEIOU"
    vowel_words = [word for word in word_list if word.lower().startswith(tuple(vowels))]
    return sorted(vowel_words, key=len, reverse=True)

words = ["apple", "elephant", "umbrella", "orange", "owl", "ice"]
print(sorted_vowel_words(words))

'''เป็น list comprehension ที่ทำหน้าที่:
วนลูปแต่ละ word ใน word_list
แปลง word เป็นตัวพิมพ์เล็กด้วย .lower()
เช็คว่าเริ่มต้นด้วยสระ (startswith(tuple(vowels)))
ถ้าใช่ → ใส่ใน list vowel_words
ตัวอย่าง:
ถ้า word_list = ["apple", "banana", "orange"] → vowel_words = ["apple", "orange"]
'''