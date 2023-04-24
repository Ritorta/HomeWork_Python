# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 

# ------------
# Вариант №1
# ------------

def degree(num, deg):
    if deg == 1:
        return num
    
    return degree(num * count, deg - 1)
    
num = abs(int(input('a: ')))
deg = abs(int(input('b: ')))
count = num
    
print(degree(num, deg))

# ------------
# Вариант №2
# ------------


# def degree(num, deg):
#     if deg == 1:
#         return num
    
#     return num * degree(num, deg - 1)
    
# num = abs(int(input('a: ')))
# deg = abs(int(input('b: ')))
    
# print(degree(num, deg)) 