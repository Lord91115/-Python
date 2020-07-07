import string
#Создать сет ( 'буквы алфавита' Заглавные + прописные + числа )
set1 = set(string.ascii_letters + string.digits[2:8] + string.digits[:5])
set2 = set(string.ascii_letters + string.digits[2:8] + string.digits[6:])
print(set1)
print(set2)
#Пересечение 1 и 2 сета
tpl_intersection = tuple(set1.intersection(set2))
print(tpl_intersection)
#Разности 1 и 2 сета
tpl_difference = tuple(set1.difference(set2))
print(tpl_difference)
print(tpl_intersection[:4])
#Вывести только числа
print(set(string.digits).intersection(set2))
#Вывести  только буквы
print(set(string.ascii_letters).intersection(set2))
#
print(tpl_intersection[::-1])
#Конвентировать в список
print(list(tpl_intersection),list(tpl_difference))