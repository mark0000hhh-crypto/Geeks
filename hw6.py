# def result(a, b, operation):
#     if operation == "+":
#         return a + b
#     elif operation == "-":
#         return a - b
#     elif operation == "*":
#         return a * b 
#     elif operation == "/":
#         if b == 0:
#             return "Ошибка:деление на ноль невозможно"
        
# print(result(2,4,"-"))
# print(result(2,4,"+"))
# print(result(2,4,"*"))
# print(result(2,0,"/"))

# num1 = int(input("Введи число:"))
# num2 = int(input("Введи число:"))
# num3 = int(input("Введи число:"))

# max_num = lambda num1, num2, num3: max(num1, num2, num3)

# result = max_num(num1, num2, num3)
# print("Наибольшие число:", result)

# Costs = [1200, 2500, 800, 3500, 1500, 4200.]
# discount = 0.15
# result =  list(map(lambda Costs: Costs * (1- discount) , Costs))
# print(result)

# age = [12, 18, 25, 16, 30, 14, 21, 17, 45, 19.]
# filter_ = list(filter(lambda age: 18 <= age <= 30 , age ))
# print(filter_)