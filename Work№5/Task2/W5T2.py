# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
# 4 


# ------------
# Вариант №1
# ------------

# def sum(a, b):

#     if count == 1:
#         return a + b
    
#     return abs(sum(count))
    
# a = abs(int(input('Enter fist number: '))
# b = abs(int(input('Enter second number: ')))
# count = 1
    
# print('Sum =', sum(a, b))

# ------------
# Вариант №2
# ------------

def sum(a, b):

    if b == 0:
        return a
    
    return sum(a + 1, b - 1)
    

a = abs(int(input('Enter fist number: ')))
b = abs(int(input('Enter second number: ')))

    
print('Sum =', sum(a, b))


