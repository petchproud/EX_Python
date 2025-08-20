#หาหลายคำที่มีความยาวเท่ากัน (และขึ้นต้นด้วยสระ)
def longest_vowel_words(word_list):
    vowels = "aeiouAEIOU"
    max_length = 0
    result = []

    for word in word_list:
        if word.lower().startswith(tuple(vowels)):
            if len(word) > max_length:
                result = [word]
                max_length = len(word)
            elif len(word) == max_length:
                result.append(word)

    return result if result else None

words = ["apple", "elephant", "umbrella", "orange", "owl"]
print(longest_vowel_words(words))