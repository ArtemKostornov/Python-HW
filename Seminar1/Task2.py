# Задача 2: Найдите сумму цифр трехзначного числа.

while True:
 print("Введтите трёхзначное число: ")
 num = int(input())
 if ( 100 > num or num > 999):
  print("неверное число")
 else:
  break
sum = (num//100) +((num//10)%10) + (num % 10)
print("сумма цифр числа", num, " = ",sum)