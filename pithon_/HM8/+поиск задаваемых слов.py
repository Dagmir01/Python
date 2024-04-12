def find_word(text, word):
    words = text.split()
    for index, w in enumerate(words):
        if w == word:
            print(f"Слово '{word}' найдено в тексте на позиции {index + 1}")
            return
    print(f"Слово '{word}' не найдено в тексте")

# Получаем текст от пользователя
text = input("Введите текст: ")
word = input("Введите слово для поиска: ")

find_word(text, word)