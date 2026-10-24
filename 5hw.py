# products = {"eggs": 120,"bread":30,"patatoes":60,"peaches":180,"mango":360 }


# user_product = input("Введите продукт:")

# if user_product in products:
#     print(f"Цена товара : {products[user_product]}")
# else: 
#     print("продукт не найден")


# students = {"Алексей": 85, "Мария": 92, "Иван": 78, "Айсулуу": 95, "Бектур": 88}

# Best_student = max(students, key=students.get)
# print(f"Студент с самым большим баллом: {Best_student}, ({students[Best_student]} баллов)")


# a = {1, 2, 3, 4, 5, 6}
# b = {4, 5, 6, 7, 8, 9}

# common_elements = a & b
# differences_of_a = a - b

# print("общие элементы множеств:", common_elements)
# print("уникальные элементы только для множевства А", differences_of_a)

# numbers = [5, 2, 7, 5, 3, 2, 8, 7, 1, 5]

# unique_num = set(numbers)
# count = len(unique_num)


# print("уникальные числа:", unique_num)
# print("Количество таких чисел", count)

cities = ["Ош", "Бишкек", "Ош", "Талас", "Бишкек", "Ош", "Нарын", "Талас"]


city_counts = {}
for city in cities:
  city_counts[city] = city_counts.get(city, 0) + 1

print("Словарь повторений:", city_counts)


unique_cities = set(cities)
print("Уникальные города:", unique_cities)
print("Количество уникальных городов:", len(unique_cities))