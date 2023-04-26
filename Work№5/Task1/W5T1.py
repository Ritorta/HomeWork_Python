# Work №5 - Task №1

# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 

# ------------
# Вариант №1
# ------------

# def degree(num, deg):
#     if deg == 1:
#         return num
    
#     return degree(num * count, deg - 1)
    
# num = abs(int(input('Enter fist number: ')))
# deg = abs(int(input('Enter second number: ')))
# count = num
    
# print('Degree =', degree(num, deg))

# ------------
# Вариант №2
# ------------


# def degree(num, deg):
#     if deg == 1:
#         return num
    
#     return num * degree(num, deg - 1)
    
# num = abs(int(input('Enter fist number: ')))
# deg = abs(int(input('Enter second number: ')))
    
# print('Degree =', degree(num, deg)) 

# ------------
# Вариант №3
# ------------

def degree(a, b):

    if count == 1:
        return a ** b
    
    return abs(degree(count - 1))
    
a = abs(int(input('Enter fist number: ')))
b = abs(int(input('Enter second number: ')))
count = 1
    
print('Degree =', degree(a, b))