# Work №4 - Task №1

# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

# Ввод:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18

# Вывод:
# 6 12

# ------------
# Вариант №1
# ------------

# a = int(input('Enter the size first array: '))
# array1 = set()

# b = int(input('Enter the size second array: ')) 
# array2 = set()

# for i in range(a):
#     array1.add(int(input('Enter the number for first array: ')))

# print(array1)    
# for j in range(b): 
#     array2.add(int(input('Enter the number for second array: ')))

# print(array2)

# z = array1.intersection(array2)

# print('The intersection array:', z)

# ------------
# Вариант №2
# ------------

# a = int(input('Enter the size first array: '))

# array1 = set()

# for i in range(a):
#     array1.add(int(input('Enter the number for first array: ')))

# b = int(input('Enter the size second array: '))

# array2 = set()

# for j in range(b):
#     array2.add(int(input('Enter the number for second array: ')))

# array3 = set()

# for z in array1:
#     if z in array2:
#             array3.add(z)

# print('The intersection array:', array3)


# ------------
# Вариант №3
# ------------

a = int(input('Enter the size first array: '))
array1 = set(int(input('Enter the number for first array: ')) for i in range(a))

b = int(input('Enter the size second array: ')) 
array2 = set(int(input('Enter the number for second array: ')) for j in range(b))

array3 = array1.intersection(array2)

print(array3)