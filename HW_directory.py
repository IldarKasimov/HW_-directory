def work_with_phonebook():
    stop_all = 'No'
    choice = show_menu(stop_all)
    phone_book = read_csv('my_phonebook.csv')
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']

    while choice != 7:
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            choice_menu_2 = show_menu_2()
            if choice_menu_2 == 1:
                search_value = input('Введите Фамилию: ')
                key_d = 'Фамилия'
                print(*(find_by_key_d(phone_book, search_value, key_d)), sep = ',''\n')
            elif choice_menu_2 == 2:
                search_value = input('Введите Имя: ')
                key_d = 'Имя'
                print(*(find_by_key_d(phone_book, search_value, key_d)), sep = ',''\n')
            elif choice_menu_2 == 3:
                search_value = input('Введите Телефон: ')
                key_d = 'Телефон'
                print(*(find_by_key_d(phone_book, search_value, key_d)), sep = ',''\n')
            elif choice_menu_2 == 4:
                search_value = input('Введите Описание: ')
                key_d = 'Описание'
                print(*(find_by_key_d(phone_book, search_value, key_d)), sep = ',''\n')
        elif choice == 3:
            lst =[]
            lst.append(input('Введидте Фамилию: '))
            lst.append(input('Введидте Имя: '))
            lst.append(input('Введидте Телефон: '))
            lst.append(input('Введидте Описание: '))
            print(*(add_subscriber(phone_book, fields, lst)))
        elif choice == 4:
            last_name_del = input('Введите Фамилию удаляемого абонента: ')
            name_del = input('Введите Имя удаляемого абонента: ')
            print(*(del_subscriber(phone_book, last_name_del, name_del)), sep = '')
        elif choice == 5:
            print(write_csv('my_phonebook.csv', phone_book))
        elif choice == 6:
            stop_menu_6 = 0
            while stop_menu_6 != 1:
                choice_3 = input('Сохранить изменения? (Да/Нет): ').lower()
                if choice_3 == 'да':
                    print(write_csv('my_phonebook.csv', phone_book))
                    stop_menu_6 = 1
                    stop_all = 'Yes'
                    print('Всего доброго!')
                elif choice_3 == 'нет':
                    stop_menu_6 = 1
                    stop_all = 'Yes'
                    print('Всего доброго!')
                else:
                    print('Введите либо "Да", либо "Нет"')
        choice = show_menu(stop_all)


def show_menu(stop_all):
    if stop_all == 'Yes':
        return 7
    else:
        print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента\n"
          "3. Добавить абонента в справочник\n"
          "4. Удалить абонента из справочника по фамилии и имени\n"
          "5. Сохранить справочник в csv\n"
          "6. Закончить работу\n")
    choice = int(input())
    return choice


def show_menu_2():
    print("\n1. По фамилии\n"
         "2. По имени\n"
         "3. По телефону\n"
         "4. По описанию\n")
    choice_menu_2 = int(input())
    return choice_menu_2


def read_csv(my_phonebook):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open('my_phonebook.csv','r',encoding='utf-8') as phb:
        for line in phb:
           record = dict(zip(fields, line.rstrip('\n').split(',')))
           phone_book.append(record)
    return phone_book 


def print_result(phone_book):
    return print(*phone_book, sep = ',''\n')


def find_by_key_d(phone_book, search_value, key_d):
    # return [phone_book[i] for i in range(len(phone_book)) if phone_book[i]['key_d'] == search_value] # сократим код до 1 строчки вместо 3х,
    # но не вернем сообщение, если значения поиска нет в справочнике
    list_search_value = []
    for i in range(len(phone_book)):
        if phone_book[i][key_d].lower() == search_value.lower():
            list_search_value.append(phone_book[i])
    if len(list_search_value) > 0:
        return list_search_value
    return key_d, search_value, 'отстутсвует в справочнике'

    
def add_subscriber(phone_book, fields, lst):
    phone_book.append(dict(zip(fields, lst)))
    return 'Добавили абонента:', lst[:-2]


def del_subscriber(phone_book, last_name_del, name_del):
    flag = True
    for i in range(len(phone_book)):
        lst_del = []
        if flag:
            for v in phone_book[i].values():
                if v.lower() == last_name_del.lower():
                    lst_del.append(v.lower())
                elif v.lower() == name_del.lower():
                    lst_del.append(v.lower())
            if last_name_del.lower() in lst_del and name_del.lower() in lst_del:
                phone_book.pop(i)
                flag = False
                return 'Удалили абонента: ', last_name_del, ' ', name_del
    return 'Абонент: ', last_name_del, ' ', name_del, ' отсутствует в справочнике'


def write_csv(my_phonebook, phone_book):
        with open('my_phonebook.csv', 'w' ,encoding='utf-8') as subscriber:
            for i in range(len(phone_book)):
                s='' 
                for v in phone_book[i].values():
                    s+=v+','
                subscriber.write(f'{s[:-1]}\n')
        return 'Справочник сохранен!'


work_with_phonebook()