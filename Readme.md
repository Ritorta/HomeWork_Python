Этот репозиторий будет содержать все домашние работы по семинарам по Python.
--------
Work №1:
--------

Task №1

Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) 

Task №2

Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

Task №3

Задача 6: Вы пользуетесь общественным транспортом? 
Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*
385916 -> yes
123456 -> no

--------
Work №2:
--------

Task №1

Задача 1: На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.

*Пример:*
5 -> 1 0 1 1 0
2

Task №2

Задача 2: Петя и Катя – брат и сестра. Петя – студент, а Катя –
школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.

*Пример:*
4 4 -> 2 2
5 6 -> 2 3

Task №3

Задача 3: Требуется вывести все целые степени двойки (т.е. числа
вида 2k), не превосходящие числа N.

*Пример:*
10 -> 1 2 4 8

--------
Work №3:
--------

Task №1

Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai. Последняя строка содержит число X.

*Пример:*
5
1 2 3 4 5
3
-> 1

Task №2

Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai. Последняя строка
содержит число X.

*Пример:*
5
1 2 3 4 5
6
-> 5

Task №3

В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
ценность. В случае с английским алфавитом очки распределяются так:
● A, E, I, O, U, L, N, S, T, R – 1 очко;
● D, G – 2 очка;
● B, C, M, P – 3 очка;
● F, H, V, W, Y – 4 очка;
● K – 5 очков;
● J, X – 8 очков;
● Q, Z – 10 очков.
А русские буквы оцениваются так:
● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
● Д, К, Л, М, П, У – 2 очка;
● Б, Г, Ё, Ь, Я – 3 очка;
● Й, Ы – 4 очка;
● Ж, З, Х, Ц, Ч – 5 очков;
● Ш, Э, Ю – 8 очков;
● Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо только
английские, либо только русские буквы.

*Пример:*
Ввод:
ноутбук
Вывод:
12

--------
Work №4:
--------

Task №1

Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.

*Пример:*
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12

Task №2

В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
круглой грядке, причем кусты высажены только по окружности. Таким образом, у
каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.

*Пример:*
4 -> 1 2 3 4

9

--------
Work №5:
--------

Task №1

Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

*Пример:*
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8 

Task №2

Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

*Пример:*
2 2
4 

--------
Work №6:
--------

Task №1

Заполните массив элементами арифметической
прогрессии. Её первый элемент, разность и количество
элементов нужно ввести с клавиатуры. Формула для
получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.

*Пример:*
an = a1 + (n - 1) * d
an = 7 + (5 - 1) * 2
 
Ввод: 7 2 5
Вывод: 7 9 11 13 15

Task №2

Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного
максимума)

*Пример:*
Ввод: [-5, 9, 0, 3, -1, -2, 1,
4, -2, 10, 2, 0, -9, 8, 10, -9,
0, -5, -5, 7]
Интервал: [7, 11]

Вывод: [1, 9, 13, 14, 19]

--------
Work №7:
--------

Task №1

Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. 
число гласных букв) в каждой фразе стихотворения одинаковое. 
Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.

*Пример:*

Ввод: пара-ра-рам рам-пам-папам па-ра-па-да  
  
Вывод: Парам пам-пам  

Task №2

Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, 
у которой ровно два аргумента, как, например, у операции умножения.

*Пример:*

Ввод: `print_operation_table(lambda x, y: x * y) ` 
Вывод:

1 2  3  4  5  6
2 4  6  8  10 12
3 6  9  12 15 18
4 8  12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36

--------
Work №8:
--------
Task №1

Дополнить созаднный телефонный справочник или создать новый с возможностью изменения и удаления данных. 
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.

--------
Work №9:
--------

Task №1

Работать с файлом california_housing_train.csv, 
который находится в папке sample_data. 
Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).

Task №2

Работать с файлом california_housing_train.csv, 
который находится в папке sample_data. 
Узнать какая максимальная households в зоне минимального значения population.

P.s Должно быть сделано в Colaboratory.

--------
Work №10:
--------

Task №1

В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI'lst})
data.head()

Task №2

Напишите класс Dragon (Дракон), экземпляр которого при инициализации принимaет аргументы:
рост, огнеопасность, цвет.

Класс обеспечивает выполнение методов (dr — экземпляр класса)
экземпляры можно сравнивать: сначала по росту. затем по огнеопасности, затем по цвету по алфавиту

экземпляры класса можно складывать: dr2 =dr + dr1. при этом возвращается новый экземпляр со значениями атрибутов:

цвет меньший по алфавиту;
рост - среднее арифметическое из двух округлённое до целого вниз,
огнеопасность - большее из двух;

из экземпляра класса можно вычесть число: dr -= number, из роста вычитается целая честь от деления роста на число, к
огнеопасности прибавляется остаток от деления огнеопасности на число;

Экземпляр можно вызвать с аргументом-строкой - возвращается строка-аргумент, повторенная количество раз, равное
значению атрибута огнеопасность;

change_color() - вызывается c аргументом - цветом, на который нужно поменять имеющийся цвет

str- возвращает строку:
Dragon with height «рост», danger <огнеопасность> and color «цвет».

repr- возвращaет строку:
Dragon(‹рост>, <огнеопасность>, <цвет>) 

Пример

dr = Dragon(69, 5, “brown™)
dr1 = Dragon(69, 5, “gray")
print (dr > dr1, dr != dr1, dr <= dr1)
print(dr, dr1, sep="\n")
print()

dr.change_color("white")
dr -= 23
dr1 -= 2
dr2 = dr+dr1
print(dr, dr1, dr2, sep="\n")

print(dr("Welcome")

Вывод

False True True
Dragon with height 69, danger 5 and color brown.
Dragon with height 69, danger 5 and color gray.

Dragon with height 66, danger 10 and color white.
Dragon with height 35, danger 6 and color gray.
Dragon with height 50, danger 10 and color brown.
WelcomeWelcomeWelcomeWelcomeWelcome