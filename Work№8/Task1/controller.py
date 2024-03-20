import view
import database

# Логика вызова функций через кнопки меню
def main():
    while True:
        try:
            num = view.user_input()
            if num == 1:
                dat = view.input_1()
                database.add_base(dat)
            elif num == 2:
                dat = view.input_2()
                database.searh_base(dat)
            elif num == 3:
                database.sort_base_name()
            elif num == 4:
                database.sort_base_date()
            elif num == 5:
                database.show_base()
            elif num == 6:
                database.show_base_name()
            elif num == 7:
                dat = view.input_2()
                select = database.select_number(dat)
                number = view.input_7()
                new_user = view.input_1()
                database.change_base(select[number - 1], new_user)
            elif num == 8:
                dat = view.input_2()
                select = database.select_number(dat)
                number = view.input_8()
                database.delete_name_base(select[number -1])
            elif num == 9:
                print('Программа завершена.')
                break
            else:
                print('Такого пункта меню не существует, выберите цифру согласно пункта меню.')
                input("Нажмите клавижшу для продолжения: ")
        except ValueError:
            print('Ошибка пожалуста для навигации по меню используйте цифры.')
            input("Нажмите клавижшу для продолжения: ")

main()
