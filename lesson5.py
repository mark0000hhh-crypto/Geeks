# dictinary - dict - словари - {}
# changeable type of data
# indexes doest work here

# dict_st = {"name":"Nurbolot","age":18} словарь ключ - значение
# print(dict_st)
# dict_st["hobby"] = "footbal" добавляет ключ и его значение
# print(dict_st)
# dict_st["age"] = "21" изменение данных заложенных в ключе Age
# print(dict_st)
# dict_st.pop("hobby") убирает ключ и значение 
# print(dict_st)
# print(dict_st.values()) выдает значения без ключей
# print(dict_st.keys()) выдает ключи только без значении
# print(dict_st.items()) выдает и ключ и значения парами 


# множество - variables - set - frozenset - {}
# data is unique
# doesnt have any sequance
# indexes doesnt work

# set - {}
# changeable type of data
# student = {"Beksultan","Nurbolot","Aibek","Beksultan"}
# print(student)
# student.add("Askar")
# print(student)
# student.remove("Aibek")
# print(student)
# student.discard("Aibek1")

# frozenset
# unchangeable type of data


# stud = frozenset(["Beksultan","Nurbolot","Aibek","Beksultan"])
# print(stud)



# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}
# print(a&b)
# print(a|b)

# group1 = ["Азамат", "Алия", "Нурбек", "Руслан"]
# group2 = ["Алия", "Руслан", "Айдана", "Эльдар"]

# comm = set(group1) & set(group2)
# print(comm)

# text = input("Введите предложение:")
# words = text.lower().split()
# unique_cost = len(set(words))
# print("количество уникальных слов:" , {unique_cost})