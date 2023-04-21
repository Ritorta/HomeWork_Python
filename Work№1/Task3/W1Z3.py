# Work №1 - Task №3

# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

# ------------
# Вариант №1
# ------------

# n = input('Enter six-digit number ticket: ')

# list1 = int(n[0]) + int(n[1]) + int(n[2])
# list2 = int(n[3]) + int(n[4]) + int(n[5])
# count = len(n)
# if count == 6:
#     if list1 == list2:
#         print('Yes, thes lucky ticket')
#     else:
#         print('Oh no, thes ticket losers')
# else:
#     print('Error, enter six-digit number!')

# ------------
# Вариант №2
# ------------

n = input('Enter six-digit number tiket: ')

firstn = int(0)
secondn = int(0)
count = len(n)

if count == 6:
    n = int(n)
    for i in range(6):
        if i < 3:
            firstn = firstn + n // 10 ** i % 10
        else:
            secondn = secondn + n // 10 ** i % 10
    if firstn == secondn:
        print('Yes, thes lucky ticket')         
    else:
        print('Oh no, thes ticket losers')
else:
    print('Error, enter six-digit number!')




