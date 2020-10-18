# # Задание 1
#
# my_list = []
# while True:
#     line = input("Введи что-нибудь: ")
#     if line == '':
#         print(my_list)
#         exit()
#     else:
#         newline = line + "\n"
#         my_list.append(newline)
#
#     with open("test_1.txt", "w") as file_obj:
#         file_obj.writelines(my_list)

# Задание 2
#
# my_list = ['Привет\n', 'Гики\n', 'как дела?\n']
# with open("test_2.txt", 'w+') as file_obj:
#     file_obj.writelines(my_list)
# with open("test_2.txt") as file_obj:
#     lines = 0
#     letters = 0
#     for line in file_obj:
#         lines += line.count("\n")
#         letters = len(line)-1
#         print(f"{letters} letters in line")
#     print(f"String count is {lines}")

# Задание 3
# firm = {'Иванов': 170, 'Петров': 210, 'Сидоров': 190, 'Ротшильд': 1500}
# try:
#     file_obj = open("test_3.txt", 'w')
#     for last_name, salary in firm.items():
#         file_obj.write(last_name + ':' + str(salary) + "\n")
# except IOError:
#     print("Произошла ошибка ввода-вывода!")
# finally:
#     file_obj.close()
# summa = 0
# count = 0
# persons = []
# with open("test_3.txt", "r") as file_obj:
#     for line in file_obj:
#         print(line, end="")
#         tokens = line.split(':')
#         if int(tokens[1]) <= 200:
#             persons.append(tokens[0])
#         summa += int(tokens[1])
#         count += 1
# result = summa / count
# print(f"persons: {persons}")
# print(f"averate: {result}")

# Задание 3.1
translater = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре'}
my_list = []
result = []
try:
    file_obj = open("test_4_output.txt", 'r')
    for line in file_obj:
        tokens = line.split(" - ")
        print(tokens)
        if tokens[0] in translater:
            word = translater[tokens[0]]
            result.append(word +' - '+ tokens[1])
    print(result)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_obj.close()

try:
    file_input = open("test_4_input.txt", "w")
    file_input.writelines(result)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_input.close()