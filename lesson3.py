# циклы 
# for - если знаешь результат (итог)
# while - если не знаешь результат(итог)




# for i in range(10): - цикл выводит 10 раз фразу из принта
#     print("hello world")



# students = ["aliar", "islam", "jamal"] пишет имена согласно индексу
# print("name:" , students.index(0))
# print("name:" , students.index(1))
# print("name:" , students.index(2))

# for num in range(200,800,25): идет отсчет от 200 до 800 со шагом в 25 
#     print(num)

# students = ["aliar", "islam", "jamal"]
# for names in students: - выводит по формуле в принте
#     print("name:", names)




# while True: 
#     num1 = int(input("введите число:"))
#     num2 = int(input("введите второе число:"))

#     print(num1+num2)
#     print(num1-num2)
#     print(num1*num2)
#     print(num1/num2)
#     print(num1//num2)
#     print(num1%num2)
#     print(num1**num2)    

# операторы исключения
# Try - ловит ошибки путем попыток
# except - обрабатывает ошибку


num1 = 33
num2 = 00
try:
    print(num1 / num2)
except ZeroDivisionError:
    print("высшая математика тебе рано") 


