# Work №10 - Task №2

# Напишите класс Dragon (Дракон), экземпляр которого при инициализации принимaет аргументы:
# рост, огнеопасность, цвет.

# Класс обеспечивает выполнение методов (dr — экземпляр класса)
# экземпляры можно сравнивать: сначала по росту. затем по огнеопасности, затем по цвету по алфавиту

# экземпляры класса можно складывать: dr2 =dr + dr1. при этом возвращается новый экземпляр со значениями атрибутов:

# цвет меньший по алфавиту;
# рост - среднее арифметическое из двух округлённое до целого вниз,
# огнеопасность - большее из двух;

# из экземпляра класса можно вычесть число: dr -= number, из роста вычитается целая честь от деления роста на число, к
# огнеопасности прибавляется остаток от деления огнеопасности на число;

# Экземпляр можно вызвать с аргументом-строкой - возвращается строка-аргумент, повторенная количество раз, равное
# значению атрибута огнеопасность;

# change_color() - вызывается c аргументом - цветом, на который нужно поменять имеющийся цвет

# str- возвращает строку:
# Dragon with height «рост», danger <огнеопасность> and color «цвет».

# repr- возвращaет строку:
# Dragon(‹рост>, <огнеопасность>, <цвет>) 

# Пример

# dr = Dragon(69, 5, “brown™)
# dr1 = Dragon(69, 5, “gray")
# print (dr > dr1, dr != dr1, dr <= dr1)
# print(dr, dr1, sep="\n")
# print()

# dr.change_color("white")
# dr -= 23
# dr1 -= 2
# dr2 = dr+dr1
# print(dr, dr1, dr2, sep="\n")

# print(dr("Welcome")

# Вывод

# False True True
# Dragon with height 69, danger 5 and color brown.
# Dragon with height 69, danger 5 and color gray.

# Dragon with height 66, danger 10 and color white.
# Dragon with height 35, danger 6 and color gray.
# Dragon with height 50, danger 10 and color brown.
# WelcomeWelcomeWelcomeWelcomeWelcome


# ------------
# Вариант №1
# ------------

class Dragon:

    # Функция инициализация класса Dragon
    def __init__(self, height, danger, color):
        self.height = height
        self.danger = danger
        self.color = color

    # Функция сравнения
    def __lt__(self, other):
        if self.height != other.height:
            return self.height < other.height
        if self.danger != other.danger:
            return self.danger < other.danger
        return self.color < other.color

    # Функция сравнения
    def __eq__(self, other):
        return self.height == other.height and self.danger == other.danger and self.color == other.color

    # Функция сравнения
    def __le__(self, other):
        if self.height != other.height:
            return self.height <= other.height
        if self.danger != other.danger:
            return self.danger <= other.danger
        return self.color <= other.color

    # Функиция сложения Драконов
    def __add__(self, other):
        new_color = min(self.color, other.color)
        new_height = (self.height + other.height) // 2
        new_danger = max(self.danger, other.danger)
        return Dragon(new_height, new_danger, new_color)

    # Функция вычитания Драконов
    def __sub__(self, number):
        new_height = self.height // number
        new_danger = self.danger % number
        return Dragon(new_height, new_danger, self.color)

    # Функция вызова строки
    def __call__(self, string):
        return string * self.danger

    # Функция изменения цвета
    def change_color(self, new_color):
        self.color = new_color

    # Функция возврата строкогого представления
    def __str__(self):
        return f"Dragon with height {self.height}, danger {self.danger} and color {self.color}."

    # Функция возврата возврата объекта в виде строки
    def __repr__(self):
        return f"Dragon({self.height}, {self.danger}, {self.color})"

dr = Dragon(69, 5, "brown")
dr1 = Dragon(69, 5, "gray")
print(dr > dr1, dr != dr1, dr <= dr1)
print(dr)
print(dr1)
print()

dr.change_color("white")
dr -= 23
dr1 -= 2
dr2 = dr + dr1
print(dr)
print(dr1)
print(dr2)
print(dr("Welcome"))
