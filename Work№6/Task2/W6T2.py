# Work №6 - Task №2

# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Интервал: [7, 11]

# Вывод: [1, 9, 13, 14, 19]

# ------------
# Вариант №1
# ------------

m = int(input('Enter the size array: '))

array = []

for i in range(m):
    array.append(int(input(f'Enter number array {i + 1}: ')))

array_i = []
index = [] 

for j in range(1, 3):
    array_i.append(int(input(f'Enter the number interval {j + 1}: ')))

for i1 in range(len(array)):
        if array_i[0] <= array[i1] <= array_i[1]:
            index.append(i1)

print(f'Index in interval from {array_i[0]} to {array_i[1]}: {index}')

# ------------
# Вариант №2
# ------------

# m = int(input('Enter the size array: '))

# array = []

# for i in range(m):
#     array.append(int(input(f'Enter number array {i + 1}: ')))

# interval_first = int(input('Enter the number size interval: '))
# interval_second = int(input('Enter the number size interval: '))

# array_i = []

# for i1 in range(len(array)):
#         if interval_first <= array[i1] <= interval_second:
#             array_i.append(i1)

# print(f'Index in interval from {interval_first} to {interval_second}: {array_i}')
