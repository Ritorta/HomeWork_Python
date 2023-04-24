# Work №3 - Task №2

# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X.

# 5
# 1 2 3 4 5
# 6
# -> 5

# ------------
# Вариант №1
# ------------

# n = abs(int(input('Enter the size array: ')))

# a = []

# for i in range(n):
#     a.append(abs(int(input('Enter the number: '))))

# x = abs(int(input('Enter the key number: ')))

# dif = abs(a[0] - x)
# result = a[0]

# for i in a:
#     if abs(i - x) < dif:
#         dif = abs(i - x)
#         result = i

# print(result)

# ------------
# Вариант №2
# ------------

# n = abs(int(input('Enter size array: ')))

# a =[]

# for i in range(n):
#     a.append(abs(int(input('Enter the number: '))))

# x = abs(int(input('Enter the key number: ')))

# result_min = x - 1
# result_max = result_min + 2

# print(result_min)
# print(result_max)

# ------------
# Вариант №3
# ------------

# n = abs(int(input('Enter size array: ')))

# a =[]

# for i in range(n):
#     a.append(abs(int(input('Enter the number: '))))

# x = abs(int(input('Enter the key number: ')))

# dif_min = abs(a[0] - x)

# result_min = a[0]
# result_max = a[-1]

# for i in a:
#     if abs(i - x) < dif_min:
#         dif_min = abs(i - x)
#         result_min = i
#     dif_max = abs(result_min + 2)
#     result_max = dif_max

#     if i == x:
#         result_min = result_min - 1
#         result_max = result_min + 2
                
# print(result_min)
# print(result_max)


# ------------
# Вариант №4
# ------------

n = abs(int(input('Enter size array: ')))

a =[]

for i in range(n):
    a.append(abs(int(input('Enter the number: '))))

x = abs(int(input('Enter the key number: ')))

dif_min = abs(a[0] - x)
dif_max = 0

result_min = a[0]
result_max = a[-1]


for i in a:
    if abs(i - x) < dif_min:
        dif_min = abs(i - x)
        result_min = i
        for j in range(len(a)):
            if result_min == a[-1]:
                dif_max = abs(result_min + 2)
                result_max = dif_max

            else:
                dif_max = a[result_min]
                result_max = dif_max

    if i == x:
        result_min = result_min - 1
        result_max = result_min + 2
                
print(result_min)
print(result_max)



# a = [5,3,2]
# for i in range(len(a)):
#     print(a[i], i)#a[i] - значение, i - индекс (i идет по индексам от 0 до len(a))

# a = [5,3,2]
# for i in a:
#     print(i)#значение(i идет по элементам списка a)

