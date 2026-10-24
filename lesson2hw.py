cost = float(input("Введите сумму покупки:"))

if cost < 1000: 
    discount = 0
elif 1000 <= cost <= 5000: 
    discount = 0.05
elif cost > 5000: 
    discount = 0.10

total_cost = cost * (1-discount)
print(f"Итоговая сумма к оплате: {total_cost}")


user = input("Введите свой логин:")
age = int(input("Введите возраст:"))

if user == "admin" and age >= 18: 
    print("Доступ получен")
else:
    print("Доступ закрыт")

products = ["eggs","butter","milk","bread","sausages"]

products.append("apples")
products.insert(3,"chesee")
products.remove("apples")
products.sort()
print(products)


students = ["Aziret","Oisha","Aliar","Guliroza","Omur"]
students.pop(0)
students.append("Muhamed Ali")
students.append("Denis")
print(students)


grades = (5, 4, 3, 5, 4, 5, 3, 5)

all_five = grades.count(5)
first_three_index = grades.index(3)

print(F"количевство 5ок: {all_five} ")
print(F"индекс первой тройки равен: {first_three_index}")