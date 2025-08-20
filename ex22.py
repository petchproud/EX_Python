#หาคำที่ "ขึ้นต้นด้วยพยัญชนะ" ที่ยาวที่สุด
def longest_consonant_word(word_list):
    if not word_list:
        return None
    
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    new_word = None

    for word in word_list:
        if word and word[0] in consonants: #word ต้องไม่ใช่ None หรือว่าง ("") ตัวอักษรตัวแรกของคำ (word[0]) อยู่ในพยัญชนะ
            if new_word is None or len(word) > len(new_word):
                new_word = word
    return new_word

#รับคำจากผู้ใช้ (คั่นด้วยช่องว่าง)
user_input = input("Enter words separted by spaces:")
words = user_input.split()

#เรียกใช้ฟังก์ชัน
result = longest_consonant_word(words)

#แสดงผล
if result:
    print("Longest consonant-starting word is:", result)
else:
    print("No word starts with a consonant.")