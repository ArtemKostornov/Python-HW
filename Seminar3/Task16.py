# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.
import random

n = int(input('Введите размер массива N: '))
x = int(input('Введите число X: '))
n_array = []
for i in range(n):
    n_array.append(random.randint(0, n//2))

num = 0
for i in range(len(n_array)-1):
    if n_array[i] == x:
        num += 1
print(num)