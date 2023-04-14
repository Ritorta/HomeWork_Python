# Task №3

# Задача 3: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.

# 10 -> 1 2 4 8

# ------------
# Вариант №1
# ------------

# n = int(input('Enter the nubmer: '))

# degree = 0
# result= 0

# while degree < n:
#     result = 2 ** degree
#     if result < n:
#         print(result)
#     degree = degree + 1


# ------------
# Вариант №2
# ------------

# n = int(input('Enter number: '))

# degree = 0

# for i in range(n):
#         degree = 2 ** i
#         if degree < n:
#             print(degree)            
 
    
# ------------
# Вариант №3
# ------------

n = int(input('Enter the number: '))

degree = 1

while degree < n:
    print(degree)
    degree = degree * 2
    