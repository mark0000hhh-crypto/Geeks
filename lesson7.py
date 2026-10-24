# Работа с файлами 
# 1) без with
# 2) с with

# 1) без with
# r - чтение файла
# w -  записать/перезаписать что то в файл
# Метод read - читает то что находится внутри файла
# read = open("test.txt", "r", encoding="utf-8")
# result = read.read()
# print(read.read())
# read.close()

# метод write открывает если есть или создает файл если нет и пишет то что нужно написать :3
# write_file = open("test1.txt", "w", encoding="utf-8")
# write_file.write("привет мир")
# write_file.close()


# add = open("test1.txt", "a", encoding="utf-8")
# add.write("\nкак дела мабой")
# add.close()

# 2) с with

# with open("test.txt", "r", encoding="utf-8") as with_read:
#     result = with_read()
#     print(result)

# with open("geekspro.txt" , "w", encoding="utf-8") as my_bio:
#      me = my_bio.write("Name: Mark \nSurname:Mamytov\nWork experience:4 years\nsubject of work: python")
#      print(me)