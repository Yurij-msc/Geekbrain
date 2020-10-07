# # Задание 1
# a = int(input("Введи первое число.."))
# b = int(input("Введи второе число.."))
#
#
# def multiplication(a, b):
#     if (b == 0):
#         print("На ноль делить нельзя")
#     else:
#         return (a / b)
#
# print("Результат деления чисел равен..", multiplication(a, b))

# Задание 2
#
# def input_user(name, surname, birthsday, sity, e_mail, tel)
#     print(name, surname, birthsday, sity, e_mail, tel)
# input_user(name='Yurij', surname='Rom', birthsday='26.10.82', sity='Msc', e_mail='E-mail', tel='Samsung')
# Задание 3
#
# def my_func(x, y, z):
#     sequence = [x, y, z]
#     total = [] # создаем пустой список
#     max_1 = max(sequence) #выбираем максимальное число из 3-х
#     total.append(max_1) # добавляем в пустой список первое максимальное число
#     sequence.remove(max_1) #удаляем выбранное мах число для продолжения отбора
#     max_2 = max(sequence) #ищем второе мах число
#     total.append(max_2) #добавляем в список 2-е число
#     print(sum(total)) # выводим сумму мах чисел в списке
#
# my_func(10, 20, 30) # присваиваем значения переменным

# # Задание 4 без второго способа
# def my_func(x, y):
#     return 1 / x ** abs(y)
# print(my_func(4, -5))
# Второй способ
x = int(input("Введи положительное число"))
y = int(input("Введи число степени"))
stepen = 1
total = x
while (stepen < y):
    if y == 0:
        print("Любое число в степени 0 равно 1")
    elif y < 0: #Почему-то не распознает знак минус и не идет по этому пути
        total = total * x
        stepen += 1
        print(1 / total)
    else:
        total = total * x
        stepen += 1
        print(total)

# # Задание 5
# import sys
#
# result = 0
# while True:
#     line = input("Введи число или спец знак q для выхода: ")
#     tokens = line.split(" ")
#     for token in tokens:
#         try:
#             number = float(token)
#             result += number
#         except:
#             if token == 'q':
#                 print(f"You sum is {result}. Работа программы прервана")
#                 exit(0)
#             else:
#                 print(f"You sum is {result}. Input error", file=sys.stderr)
#                 exit(1)
#
# # Задание 6
#
#
# # 1 Вариант
# def func(a):
#         return a.title()
# print(func("abca dsd"))'''
#
# # 2 Вариант
# def my_func(a):
#     separate_word = a.split(' ')
#     total = []
#     for i in separate_word:
#         string_element = str(i)
#         first_letter = string_element[:1].upper()
#         word = first_letter + string_element[1:]
#         total.append(word)
#     return total
# print(my_func("hello world"))
# # Второй вариант
