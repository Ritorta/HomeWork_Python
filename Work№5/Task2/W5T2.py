# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 


def degree(a, b):

    if count < 0:
        return print(degree(a + b, count))
    else:
        degree(a + b, count)
    
# a = abs(int(input('a: ')))
# b = abs(int(input('b: ')))
count = 0
    
degree(1, 1)
