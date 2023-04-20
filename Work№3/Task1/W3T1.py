# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X.

# 5
# 1 2 3 4 5
# 3
# -> 1

# ------------
# Вариант №1
# ------------

# n = abs(int(input('Size array: ')))
# a = []
# count = 0
# for i in range(0, n):
#     a.append(int(input('Enter array number: ')))

# x = int(input('Enter the number to found : '))

# for i in range(0, n):
#     if a[i] == x:
#         count += 1
    
# print(count)

# ------------
# Вариант №2
# ------------

# n = abs(int(input('Enter the size array: ')))

# a = []

# for i in range(0, n):
#     a.append(int(input('Enter the number: ')))

# x = abs(int(input('Enter the number to found: ')))

# print(a.count(x))

# ------------
# Вариант №3
# ------------

# n = input('Enter the number: ').split(' ')

# for i in range(len(n)):
#     n[i] = int(n[i])

# x = int(input('Enter the number to found: '))

# count = 0

# for i in n:
#     if i == x:
#         count += 1

# print(count)

# ------------
# Вариант №4
# ------------

n = input('Enter the number: ').split(' ')

for i in range(len(n)):
    n[i] = int(n[i])

x = int(input('Enter the number to found: '))

print(n.count(x))