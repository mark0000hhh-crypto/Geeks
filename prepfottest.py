# Задание 1: Условия
# Код должен проверить, совершеннолетний ли человек, но он выдает ошибку.
# age = int(input("Введите возраст:"))
# if age >= 18:
#     print("Доступ разрешен")
# else:
#     print("Доступ запрещен")


# Задание 2: Списки
# Нужно добавить новое имя "islam" в конец списка, но метод написан неверно или не работает так.
# names = ["mark", "aliar"]
# names.append("islam")
# print(names)


# Задание 3: Циклы и итерации
# Требуется вывести числа от 0 до 4 с помощью цикла for, но цикл написан с ошибкой.
# for i in range(1,5):
#     print(i)


# a = 15
# b = 4
# print(a//b)
# print(a/b)

# word = "programming"
# print(word[0:6])

# x = 10
# y= 25

# print(x < y and x != 0)


# score = int(input("Введите количество баллов:"))

# if score >= 90:
#     print("отлично выполненая работа")
# elif 70 <= score <= 89:
#     print("Хорошая работа")
# else:
#     print("подтяни немного ты сможешь я уверен")



# colors = ["red", "blue", "green"]
# colors.append("yellow")
# colors.insert(1,"black")
# colors.pop(0)
# print(colors)

# my_tuple = (10, 20, 30, 20, 40, 20)

# all_20ies = my_tuple.count(20)
# print(all_20ies)


# for i in range(10,21):
#     print(i)

# products = ["apple", "banana", "milk", "bread"]

# for names in products:
#     print(f"Название товара: {names}")


# a = 10
# b = 0
# try:
#     print(a/b)
# except ZeroDivisionError:
#     print("на ноль делить нельзя!")


# age = int(input("Введите возраст:"))

# if age < 12:
#     print("Вам положен детский билет")
# elif 12 <= age <= 17:
#     print("Вам положен подростковый билет")
# elif age >= 18:
#     print("Вам положен Взрослый билет")

# numbers = [5, 12, 3, 8]
# numbers.append(20)
# numbers.insert(1,10)
# numbers.sort()
# print(numbers)


# numbers = [10, 5, 0, 2]
# for a in numbers:
#     try:
#         print(100/a)
#     except ZeroDivisionError:
#         print("Прости но на ноль делить нельзя")

# x = 7
# y = 3

# print(x/y)
# print(x**y)


# text = "python"
# print(text[3:7])


# num = int(input("Введите число:"))

# if num % 2 ==0:
#     print("Число четное")   
# else:
#     print("Число нечетное")


# fruits = ["apple", "banana"]
# fruits.append("kiwi")
# fruits.pop(1)
# print(fruits)

# for num in range(30,55,5):
#     print(num)
    

word = input("Введите слово(Any):")

try:
    print(word + 5)
except TypeError:
    print("Ошибка типа данных")