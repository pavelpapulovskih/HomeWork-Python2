# Задача 10: На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. 
# Определите минимальное число монеток, 
# которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('Введите кол-во монет: '))
orel = 0
reshka = 0
for i in range(n):
    x = int(input('Введите сторону орел = 0, а решка = 1: '))
    if x == 0:
        orel += 1
    else:
        reshka += 1
if reshka > orel:
    print(f'Кол-во минимальных переворотов {orel}')
else:
    print(f'Кол-во минимальных переворотов {reshka}')