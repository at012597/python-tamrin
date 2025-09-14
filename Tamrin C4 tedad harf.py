word = input("یک کلمه وارد کنید: ")
letter_count = {}
for letter in word:
    letter_count[letter] = letter_count.get(letter, 0) + 1
print(letter_count)
