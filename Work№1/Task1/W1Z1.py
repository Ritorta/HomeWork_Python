# Work №1 - Task №1

# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

# ------------
# Вариант №1
# ------------

# n = input('Enter three-digit number: ')
# count = len(n)
# if count == 3:
#     n = int(n)
#     n1 = n % 10
#     n2 = n % 100 // 10
#     n3 = n // 100
#     sum = n1 + n2 + n3
#     print('Sum numbers', sum)
# else:
#     print('Error, enter the three-digit.')

# ------------
# Вариант №2
# ------------

# n = input('Enter three-digit number: ')

# count = len(n)
# if count == 3:
#     n1 = int(n[0])
#     n2 = int(n[1])
#     n3 = int(n[2])
#     sum = n1 + n2 + n3
#     print('Sum numbers:',sum)
# else:
#     print('Error, enter the three-digit.')

# ------------
# Вариант №3
# ------------

n = input('Enter three-digit number: ')

count = len(n)
if count == 3:
    n = int(n)
    d1 = n % 10
    n1 = n // 10
    d2 = n1 % 10
    n2 = n1 // 10
    sum = n2 + d1 + d2
    print(sum)
else:
    print('error')    