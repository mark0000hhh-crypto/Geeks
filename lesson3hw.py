# for num in range(20,51): - цикл выполняет следующею функция осчитывает от 20 до 50
#     print(num)

# num = int(input("Введите число: ")) - запрашивает число от пользователя а далее предоставляет ему таблицу умножения этого числа с 1 до 10

# print(f"Таблицы умножения для числа: {num}")

# for i in range(1,11):
#     print(f"{num} x {i} = {num * i}")

# total = 0 - данная программа то есть цикл выполняет следующие вычисчитывает сумму всех чисел с 1 до 100

# for i in range(1,101):
#     total += i


# print(total)


# names = ["Aliar","Omur","Arruke","Oisha","Amir","Mark"] - данный цикл выдает имена в следующем ввиде имя ученика: итерация и так далее

# for name in names:
#     print("имя ученика:", name)

# numbers = [-5, 10, 3, 0, -2, 8, -7, 15] - данный цикл выделяет положительные числа и пишит их при помощи условия 
# for num in numbers:
#     if num > 0:
#         print(num)

# correct_password = "python123" - этот цикл запрашивате пароль если пользователь вводит верно то программа дает доступ и завершается а если нет то бесконечно повторяться пока пользователь не ведет правильный пароль

# while True:
#     password = input("Введите пароль: ")

#     if password == correct_password:
#         print("Доступ разрешен!")
#         break
    
#     print("Неверный пароль. Попробуйте еще раз.")


# target_number = 15 - этот цикл повторяться до того момента пока пользователь не угадает загаданное число
# attempt = 0

# while True:
#     user_guess = int(input("guess number from 5 to 20: "))
#     attempt += 1
    
#     if user_guess == target_number:
#         print(f"Поздравляю! Вы угадали число.")
#         print(f"Количество затраченных попыток: {attempt}")
#         break  # Выходим из цикла, игра закончена
    
#     print("Не верно! Продолжайте догадываться до числа XD")


# try: - здесь операторы исключения try and except - делают следующие try ловит ошибки при помощи пробы тоесть попыток а except - исключает выбранные ошибки и вместо них выдает предупреждение при помощи принта
#     num1 = int(input("Введите число:"))
#     num2 = int(input("Введите число:"))

#     result = num1/num2
#     print(f"результат деления: {result}")

# except ZeroDivisionError:
#     print("на ноль делить нельзя!")

# except ValueError:
#     print("Вводи числа иначе никак XD")


# prices = [150,400,750,1600,2100] - этот цикл просчитывает стоимость вссех продуктов
# total_cost = 0

# for price in prices:
#     total_cost += price


# print(f"summirized price of all products: {total_cost}")


# balance = 5000 - в данном случае испольщует while применяется для того чтобы программа перезапускалась пока ее не прервут при помощи написания числа 0 и также try для ловли ошибок и except чтобы исключать ошибки и давать текстовое предупреждение

# print(f"Money on your bank account: {balance}")
# print("Enter 0 for leave from programm")

# while True:
#     try:

#         windraw = float(input("Ввелите сумму для снятия:"))

#         if windraw == 0:
#             print("Программа завершена! до скорой встречи")
#             break
#         if windraw < 0:
#             print("Ошибка: сумма не может быть отрицательной ")
#             continue
#         if windraw <= balance:
#             balance -= windraw
#             print(f"Вывод средств успешен! Остаток на балансе: {balance}")
#         else:
#             print(f"Вывод не возможен не достаточно средств! На балансе всего: {balance}")
#     except ValueError:
#         print("Ошибка: Введите число пожалуйста")
 