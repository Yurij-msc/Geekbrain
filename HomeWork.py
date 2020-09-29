# Задание 1
a = 10
b = 20
print(a, b)
a = int(input("Введи число A!"))
b = input("Введи слово!")
print(a, b)

# Задание 2
user_Time = int(input("Введите время в секундах!"))
def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)
print(convert(user_Time))

# Задание 3
a = int(input("Введите число : "))
temp = str(a)
t1 = temp + temp
t2 = temp + temp + temp
comp = a + int(t1) + int(t2)
print("Результат равен:", comp)

#Задание 4
print (max([int(s) for s in input("Введи число!")]))

#Задание 5
