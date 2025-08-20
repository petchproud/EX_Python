def longest_vowel_word(word_list):
    if not word_list:
        return None
    
    new_word = None
    vowel = "aeiouAEIOU"

    for i in word_list:
        if i.lower().startswith(tuple(vowel)):
            if new_word is None or len(i) > len(new_word):
                new_word = i
    return new_word

word_1 = ["apple","banana","cat","dog","elephant","umberlla"]
word_2 = longest_vowel_word(word_1)
print(word_2)