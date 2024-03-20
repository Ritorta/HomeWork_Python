
# Добавление в базу данных контакта
def add_base(dat):
    with open('BASE.txt', 'a', encoding='utf-8') as file:
        file.write(dat)
    print('Запись добавлена.')

# Поиск контакта по базе данных
def searh_base(dat):
    with open('BASE.txt', 'r', encoding='utf-8') as file:
        sear = file.readlines()
        flag = False
        for i in sear:
            if dat in i:
                flag = True
                print(i)
        if flag == False:
            print('Записи не существует.\n')
    input("Нажмите клавижшу для продолжения: ")

# Сортировака базы данных по имени контакта
def sort_base_name():
    with open('BASE.txt', 'r', encoding='utf-8') as file:
        sorts = file.readlines()
        sorts.sort(key=lambda x: x.split('; ')[0].split(': ')[1].lower())

    with open('BASE.txt', 'w', encoding='utf-8') as file:
        file.writelines(sorts)
        print('Сортировка завершина.')
    input("Нажмите клавижшу для продолжения: ")

# Сортировка базы данных по дате рождения контакта
def sort_base_date():
    with open('BASE.txt', 'r', encoding='utf-8') as file:
        sort_date = file.readlines()
        j = [i.split("; ") for i in sort_date]
        j.sort(key=lambda x: x[3].split(': ')[1])

    with open('BASE.txt', 'w', encoding='utf-8') as file:
        file.write("".join('; '.join(line) for line in j))
        print('Сортировка завершина.')
    input("Нажмите клавижшу для продолжения: ")

# Показать список имён контактов
def show_base_name():
    with open('BASE.txt', 'r', encoding='utf-8') as file:
        wi = file.readlines()
        for i in wi:
            print(i.split(';')[0])
        input("Нажмите клавижшу для продолжения: ")

# Вспомогательная функция для метода изменения и удаления контакта
def select_number(dat):
    lst_edit = []
    count = 1
    with open('BASE.txt', 'r', encoding='utf-8') as file:
        edit = file.readlines()
        for i in edit:
            if dat in i:
                print(f"{count}) {i.strip()}")
                count += 1
                lst_edit.append(i)
    return lst_edit

# Изменить контакт
def change_base(old_str, new_str):
    with open('BASE.txt', 'r', encoding='utf-8') as file:
        lst_delete = file.readlines()

    with open('BASE.txt', 'w', encoding='utf-8') as file:
        for i in lst_delete:
            if i == old_str:
                file.write(new_str)
                continue
            file.write(i)
    print('Запись изменена.')
    input("Нажмите клавижшу для продолжения: ")

# Удалить контакт
def delete_name_base(dat):
    with open('BASE.txt', 'r', encoding='utf-8') as file:
        lst_delete = file.readlines()

    with open('BASE.txt', 'w', encoding='utf-8') as file:
        for i in lst_delete:
            if dat == i:
                continue
            file.write(i)
    print('Запись удалена!')
    input("Нажмите клавижшу для продолжения: ")

# Показать список контактов
def show_base():
    with open('BASE.txt', 'r', encoding='utf-8') as file:
        wi = file.read()
        print(wi)
        input("Нажмите клавижшу для продолжения: ")
