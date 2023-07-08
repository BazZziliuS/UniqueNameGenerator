import random

word = "BazZziliuS"
words_count = 100
words = set()

while len(words) < words_count:
    new_word = ""
    for char in word:
        if char.isalpha():
            if random.random() < 0.5:
                new_word += char.upper()
                if random.random() < 0.5:
                    new_word += str(random.randint(0, 9))
            else:
                new_word += char.lower()
        else:
            new_word += str(random.randint(0, 9))  # замена буквы на случайную цифру
    if new_word not in words:
        words.add(new_word)

print(words)
