# Work №6 - Task №2

# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

# ------------
# Вариант №1
# ------------

m = int(input('Enter the size array: '))

array = []

for i in range(m):
    array.append(int(input(f'Enter number array {i + 1}: ')))

# interval = int(input('Enter the number size interval: '))

array_i = []
z = []

for j in range(1, 3):
    array_i.append(int(input(f'Enter the number interval {j + 1}: ')))

for i1 in range(len(array)):
    for j1 in array_i:
        if array_i <= array and array_i >= array:
            z.append(i1)


print(array)
print(array_i)
