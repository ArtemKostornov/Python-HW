# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N.

print("Введите число: ")
num = int(input())
step = 2
if (num < step):
    print("число меньше 2йки")
else:
    if (num == 2):
        print(step)
    else:
        while(step < num):
            print(step)
            step *= 2