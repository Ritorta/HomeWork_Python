# Work №3 - Task №3

# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.

# Ввод:
# ноутбук
# Вывод:
# 12

# ------------
# Вариант №1
# ------------

# list_ru = {1 : 'АВЕИНОРСТ',   
#            2 : 'ДКЛМПУ',
#            3 : 'БГЁЬЯ',
#            4 : 'ЙЫ',
#            5 : 'ЖЗХЦЧ',
#            8 : 'ШЭЮ',
#            10 : 'ФЩЪ'}

# list_en = {1 : 'AEIOULNSTR',
#            2 : 'DG',
#            3 : 'BCMP',
#            4 : 'FHVWY',
#            5 : 'K',
#            8 : 'JX',
#            10 : 'QZ'}

# select = str(input('Select language, enter the "RUS" or "ENG": ')).upper()

# if select == 'ENG':

#     word = str(input('Enter the word: ')).upper()

#     if word.isalpha():
#         sum_en = 0
#         for i in list_en:
#             for j in word:
#                 if j in list_en[i]:
#                     sum_en += i
#         print(sum_en)
#     else:
#         print('Error, please enter the word.')      

# elif select == 'RUS':

#     word = str(input('Enter the word: ')).upper()
    
#     if word.isalpha():
#         sum_ru = 0
#         for i in word:
#             for j in list_ru:
#                 if i in list_ru[j]:
#                     sum_ru += j
#         print(sum_ru)
#     else:
#         print('Error, please enter the word.')    

# else:
#     print('Error, incorect command, please enter the "RUS" or "ENG".')

# ------------
# Вариант №2
# ------------

book = {'АВЕИНОРСТ' : 1,   
        'ДКЛМПУ' : 2,
        'БГЁЬЯ' : 3,
        'ЙЫ' : 4,
        'ЖЗХЦЧ' : 5,
        'ШЭЮ' : 8,
        'ФЩЪ' : 10,
        'AEIOULNSTR' : 1,
        'DG' : 2,
        'BCMP' : 3,
        'FHVWY' : 4,
        'K' : 5,
        'JX' : 8,
        'QZ' : 10}

words = str(input('Enter the words, Ru or En language: ')).upper()
sum = 0

if words.isalpha():
    for k, v in book.items():
        for i in words:
            if i in k:
                sum += v
    print(sum)    

else:
    print('Error, please enter the words.')    