# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

print("Введите размер 1й стороны шоколадки: ")
n = int(input())
print("Введите размер 2й стороны шоколадки: ")
m = int(input())
print("Введите сколько хотите съесть долек шоколадки: ")
k = int(input())
if(k == (m*n)):
    print("Это и есть вся шоколадка, забирай")
else:
    if(k > (m*n)):
        print("Это больше чем у меня есть, извини =(")
    else:
        if(k <= 0):
            print("Жаль что ты на диете")
        else:
            if(k == 1):
                print("Нет, это испортит вид моей шоколадки")
            else:
                if((m*n)%k == 1):
                    print("Нет, это испортит вид моей шоколадки")
                else:
                    print("Да, конечно! Я поделюсь)")