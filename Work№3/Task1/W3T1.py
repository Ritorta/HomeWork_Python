# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X.

# 5
# 1 2 3 4 5
# 3
# -> 1


n = abs(int(input('Size array: ')))
a = []
count = 0
for i in range(0, n):
    a.append(int(input('Enter array number: ')))

x = int(input('Enter the number to found : '))

for i in range(0, n):
    if a[i] == x:
        count += 1
    
print(count)