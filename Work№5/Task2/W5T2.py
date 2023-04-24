# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
# 4 


# ------------
# Вариант №1
# ------------

# def degree(a, b):

#     if count == 1:
#         return a + b
    
#     return abs(degree(count))
    
# a = abs(int(input('a: ')))
# b = abs(int(input('b: ')))
# count = 1
    
# print(degree(a, b))

# ------------
# Вариант №2
# ------------

def degree(a, b):

    if b == 0:
        return a
    
    return degree(a + 1, b - 1)
    

a = abs(int(input('a: ')))
b = abs(int(input('b: ')))

    
print(degree(a, b))


