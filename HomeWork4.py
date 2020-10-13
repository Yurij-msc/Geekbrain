# Задание 1
# from sys import argv
#
# file_name, worked_hour, rate, benefit = argv
#
# calculation = (int(worked_hour) * int(rate)) + int(benefit)
# print(f"Ты получишь плату равную {calculation}")

#Задание 2
#
# """
# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# """
# '''Вариант с генератором'''
# my_list = [3, 20, 9, 5, 1, 8, 11, 6, 15]
# new = [el for el in my_list if el > my_list[my_list.index(el)-1]]
# print(new)
#
# ''' Вариант с циклом
# i = 0
# new= []
# for el in my_list:
#     if el > my_list[i-1]:
#         new.append(el)
#     i+=1
# print(new)
# '''
# Задание 3

# numbers = range(20, 241)
# new_list = [el for el in numbers if el%20==0 or el%21==0]
# print(new_list)

#Задание 4
#from itertools import permutations, repeat, combinations
# my_list = [1, 2, 2, 3, 4, 1, 2]
# new = [el for el in my_list if my_list.count(el)==1]
# print(new)

#Задание 5
# from functools import reduce
# my_list = [el for el in range(100, 1001) if el % 2 == 0]
# def my_func(prev_el, el):
#     return prev_el * el
#
# print(reduce(my_func, my_list))

#Задание 6
def fibo_gen(number):
    count = 1
    while count <= number:
        yield count
        count += 1
i = 1
my_fifteen = []
for el in fibo_gen(5):
    if i > 15:
        break
    else:
        my_fifteen.append(el)
        i += 1
print(my_fifteen)