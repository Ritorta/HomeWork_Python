# Work №4 - Task №2

# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

# Ввод:
# 4 -> 1 2 3 4

# Вывод:
# 9

# ------------
# Вариант №1
# ------------

# n = abs(int(input('Enter the number of bushes: ')))
# if n > 2:

#     bushes = []
#     sum = []

#     for i in range(n):
#         bushes.append(abs(int(input(f'Bushes number {i + 1}, enter to the number berriers: '))))

#     for j in range(len(bushes) - 1):
#             sum.append(bushes[j] + bushes[j - 1] + bushes[j + 1])
#     sum.append(bushes[-1] + bushes[-2] + bushes[0]) 
    
#     max_value = max(sum)
#     max_index = sum.index(max_value) + 1



#     print('Sum berriers:', sum)
#     print(f'Maximum number of berries per bush is equal to: {max_value}, maximum berriers in bushes number: {max_index}.')
# else:
#     print('Error, need thee an more bushes.')         


# ------------
# Вариант №2
# ------------

n = abs(int(input('Enter the number of bushes: ')))

bushes = []
sum = 0

for i in range(n):
    bushes.append(abs(int(input(f'Bushes number {i + 1}, enter to the number berriers: '))))

bushes += bushes[:2]

for j in range(n):
    sum = max(sum, bushes[j] + bushes[j + 1] + bushes[j + 2])


print('Maximum berries:', sum)


