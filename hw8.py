with open("expenses.txt", "w", encoding="utf-8") as file:
  file.write("Потребности:\nпродукты - 1200 сом\nтранспорт - 300 сом\nинтернет - 800 сом\n кафе - 500")


with open("expenses.txt", "r", encoding="utf-8") as file:
  content = file.read()
  print("потребности дня")
  print(content)
