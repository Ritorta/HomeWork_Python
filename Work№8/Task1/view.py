def user_input():
    ask = int(input('Действие с телефонной книгой:\n'
                    '1 - Внести контакт\n'
                    '2 - Поиск контакта\n'
                    '3 - Сортировать по имени контакта\n'
                    '4 - Сортировать по дате контакта\n'
                    '5 - Список контактов\n'
                    '6 - Список имён\n'
                    '7 - Изменить контакт\n'
                    '8 - Удалить контакт\n'
                    '9 - Выйти из меню\n'))
    return ask

# Добавление пользователя в базу данных.
def input_1():

    name = input('Введите имя: ')
    family = input('Введите Фамилию: ')
    father = input('Введите Отчество: ')
    date = input('Введите дату рождения: ')
    telephone = input('Введите номер телефона: ')
    data = (f"Имя: {name}; Фамилия: {family}; Отчество: {father}; Дата Рождения: {date}; Телефон: {telephone} \n")
    return data.lower()

def input_2():
    in_sea = input('Поиск по телефонной книге: ')
    return in_sea.lower()

def input_7():
    number = int(input('Введите номер для изменения: '))
    return number

def input_8():
    number = int(input('Введите номер для удаления: '))
    return number