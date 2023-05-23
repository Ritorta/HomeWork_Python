# Work №7 - Task №1

# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. 
# число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да  
  
# **Вывод:** Парам пам-пам  


# ------------
# Вариант №1
# ------------

# song = str(input('Enter soung: '))

# def rif(song):
#     a = song.lower().split()
#     check_list = 'аеёиоуыэюя'
#     b = lambda x: sum(1 for i in x if i in check_list)
#     c = b(a[0])
#     if all([b(i) == c for i in a]):
#         return 'Парам пам-пам'
#     else:
#         return 'Пам парам'

# print(rif(song))

# ------------
# Вариант №2
# ------------

song = str(input('Enter soung: '))

def rit(song):
    a = song.split()
    array = []
    check_list = 'аеёиоуыэюя'
    for i in a:
        count = 0
        for j in i:
            if j in check_list:
                count += 1
        array.append(count)
    return len(array) == array.count(array[0])        

if rit(song):
    print('Парам пам-пам')
else:
    print('Пам парам')


