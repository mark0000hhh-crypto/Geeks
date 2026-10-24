# student = {"name":"Aliar", "age": 18, "group": "Backend", "grade": 4.4}
# print(student)
# print(student["name"])
# print(student["grade"])


# products = {"eggs":90, "bread":30, "apples":120, "juice": 130, "juliet": 150}
# p1 = int(products["eggs"])
# p2 = int(products["bread"])
# p3 = int(products["apples"])
# p4 = int(products["juice"])
# p5 = int(products["juliet"])

# prices = [p1,p2,p3,p4,p5]

# lowest_price = min(prices)
# highest_price = max(prices)
# average_price = sum(prices) / len(prices)

# print(f"Товар с самой большой ценой: {highest_price}")
# print(f"Товар с самой маленькой ценой: {lowest_price}")
# print(f"среднея цена за товар: {average_price}")

# uni_words = set()

# for i in range(5):
#     user_input = input(f"слово{i + 1}:")
#     uni_words.add(user_input)

# print("uni words:",{uni_words})
# print(f"uni words how many?:", len({uni_words}))

# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}
# print(a | b)
# print(f'Элемент который есть только в А:', a - b)
# print(f'Элемент который есть только в B:', b - a)


# students_grades = {"Алексей": [4, 5, 4],}

# for name, grades in students_grades.items():
#     average = sum(grades) / len(grades)
#     print(f"Студент: {name}, средняя оценка: {average}")


# user_input = input("Введите строку: ")
# symvols_count = {}

# for char in user_input:
#     if char in user_input:
#         symvols_count[char] = symvols_count.get(char, 0) + 1

# print("Количество букв:", letter_count)


# student1st_subjects = {"Математика", "Физика", "Информатика", "История"}
# student2nd_subjects = {"Физика", "Информатика", "Химия", "Литература"}

# common_subjects = student1st_subjects & student2nd_subjects
# print("Одинаковые предметы:", common_subjects)

# stud1 = student1st_subjects - student2nd_subjects
# print("Предметы только у первого студента:", stud1)


# stud2 = student2nd_subjects - student1st_subjects
# print("Предметы только у второго студента:", stud2)



# numbers = [2, 4, 6, 8]

# square = lambda x: x ** 2
# squared_numbers = list(map(square, numbers))

# print("Квадраты чисел:", squared_numbers)


# num = int(input("Введите число: "))

# print(f"Таблицы умножения для числа: {num}")

# for i in range(1,11):
#     print(f"{num} x {i} = {num * i}")

# students = ["Alex", "John", "Emma", "Michael", "Sophia"]

# with open("student.txt", "w", encoding="utf-8") as file:
#     for name in students:
#         file.write(name + "\n")











