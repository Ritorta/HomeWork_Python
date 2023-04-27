# Work №6 - Task №1

# Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# an = a1 + (n - 1) * d
# an = 7 + (5 - 1) * 2
 
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

# ------------
# Вариант №1
# ------------

# number = abs(int(input("Enter to start number: ")))
# steep = abs(int(input('Enter the number step: ')))
# count = abs(int(input('Enter count number: ')))

# array = []
# an = 0

# if count > 0:
#     for i in range(count + 1):
#         if i > 0:
#             an = number + (i - 1) * steep
#             array.append(an)

#     print(array)

# else:
#     print('Error, count = 0, please enter the count > 0.')


# ------------
# Вариант №2
# ------------

number = abs(int(input("Enter to start number: ")))
steep = abs(int(input('Enter the number step: ')))
count = abs(int(input('Enter count number: ')))

array = []
an = 0

if count > 0:
    while 0 < count:
        an = number + (count - 1) * steep
        array.append(an)
        count -= 1
    print(list(reversed(array)))
else:
    print('Error, count = 0, please enter the count > 0.')

# ------------
# Вариант №3
# ------------