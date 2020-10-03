# # Задание 1
# chislo = 5
# drobi = 1.2
# stroka = "Hello world"
# list = ['a', '2']
# kortezh = ('b', '3')
# slovar = {'rasberry': 'Lemon', 'pineapple': 'Bus'}
#
# biglist = [chislo, drobi, stroka, list, kortezh, slovar]
# for i in biglist:
#     print(f'{i} is {type(i)}')

# # Задание 2
# my_list = ['a', 'b', 'c', 'd', 'e']
# if len(my_list) % 2 == 0:
#     i = 0
#     while i < len(my_list):
#         el = my_list[i]
#         my_list[i] = my_list[i+1]
#         my_list[i+1] = el
#         i += 2
# else:
#     i = 0
#     while i < len(my_list) - 1:
#         el = my_list[i]
#         my_list[i] = my_list[i + 1]
#         my_list[i + 1] = el
#         i += 2
# print(my_list)

# Задание 3
# number = int(input("Введи номер месяца: "))
# if number <= 12 and number >= 1:
#     month_dict = {1: 'January',
#                   2: 'February',
#                   3: 'March',
#                   4: 'April',
#                   5: 'May',
#                   6: 'June',
#                   7: 'Jule',
#                   8: 'August',
#                   9: 'September',
#                   10: 'October',
#                   11: 'November',
#                   12: 'December'}
#     month_list = list(month_dict.values())
#     for i, el in enumerate(month_list):
#         if i == number-1:
#             print(f"Month from list is {month_list[i]}")
#             break
#     print(f"Month from dict is {month_dict[number]}")
# else:
#     print("Ты ввел неправильное число")

# Задание 4
# my_str = input("Введи слова через пробел: ")
# a = my_str.split(' ')
# for i, el in enumerate(a, 1):
#     if len(el) > 10:
#         el = el[0:10]
#     print(f"{i}. - {el}")
# Задание 5

# number = int(input("Введи число: "))
# my_list = [9, 6, 4, 1]
# c = my_list.count(number)
# for element in my_list:
#     if c > 0:
#         i = my_list.index(number)
#         my_list.insert(i+c, number)
#         break
#     else:
#         if number > element:
#             j = my_list.index(element)
#             my_list.insert(j, number)
#             break
#         elif number < my_list[len(my_list) - 1]:
#             my_list.append(number)
# print(my_list)
# Задание 6

goods = []
while input("Тебе нужно добавить продукт? Введи Да или Нет: ") == 'Да':
    number = int(input("Введи порядковый номер продукта: "))
    features = {}
    while input("Нужно ли добавить параметры продукта? Введи Да или Нет: ") == 'Да':
        feature_key = input("Введи название продукта: ")
        feature_value = input("Введи цену продукта: ")
        features[feature_key] = feature_value
    goods.append(tuple([number, features]))
print(goods)

analitics = {}
for good in goods:
    for feature_key, feature_value in good[1].items():
        if feature_key in analitics:
            analitics[feature_key].append(feature_value)
        else:
         analitics[feature_key] = [feature_value]
print(analitics)