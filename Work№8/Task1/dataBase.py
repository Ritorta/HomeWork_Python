
def add_base(dat):
    with open('BASE.txt', 'a', encoding='utf-8') as file:
        file.write(dat)
    print('Запись добавлена.')

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

def sort_base_name():
    with open('BASE.txt', 'r', encoding='utf-8') as file:
        sorts = file.readlines()
        sorts.sort()
    with open('BASE.txt', 'w', encoding='utf-8') as file:
        file.writelines(sorts)
        print('Сортировка завершина.')
    input("Нажмите клавижшу для продолжения: ")

def sort_base_date():
    with open('BASE.txt', 'r', encoding='utf-8') as file:
        sort_date = file.readlines()
        
        j = [i.split(":") for i in sort_date]
        
        print("Old = ", j)

        j.sort(key = lambda x: x[4])
        print("New = ", j)
    with open('BASE.txt', 'w', encoding='utf-8') as file:
        file.writelines(sort_date) # - сортировка по какойто причине сюда не предаётся...
        print('Сортировка завершина.')
    # input("Нажмите клавижшу для продолжения: ")

def show_base_name():
    with open('BASE.txt', 'r', encoding='utf-8') as file:
        wi = file.readlines()
        for i in wi:
            print(i.split(';')[0])
        input("Нажмите клавижшу для продолжения: ")

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


def show_base():
    with open('BASE.txt', 'r', encoding='utf-8') as file:
        wi = file.read()
        print(wi)
        input("Нажмите клавижшу для продолжения: ")