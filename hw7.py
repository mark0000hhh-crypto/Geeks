# with open("students.txt", "w", encoding="utf-8") as file:
#   file.write("Алексей\nМария\nИван\nОльга\nДмитрий")


# with open("students.txt", "r", encoding="utf-8") as file:
#   content = file.read()
#   print("Содержимое файла students.txt:")
#   print(content)

# note = input("Введите заметки: ")

# with open("diary.txt", "a", encoding="utf-8") as file:
#   file.write(note + "\n")

# print("\nВся история дневника:")
# with open("diary.txt", "r", encoding="utf-8") as file:
#   print(file.read())


# with open("text.txt", "w", encoding="utf-8") as file:
#   file.write("Сегодня отличная погода.\nМы изучаем язык программирования Python.\nРабота с файлами в Python — это очень удобно.\n")

# search_word = input("Введите слово для поиска: ").strip()

# with open("text.txt", "r", encoding="utf-8") as file:
#   text = file.read()
#   if search_word in text:
#     print(f"Слово '{search_word}' найдено в тексте!")
#   else:
#     print(f"Слово '{search_word}' не найдено в тексте.")