import sqlite3

con = sqlite3.connect('lab9.db')
cursor = con.cursor()

cursor.execute(
    '''Create table if not exists _group(
    id integer primary key autoincrement,
    name text,
    balance integer)''')

cursor.execute(
    '''Create table if not exists user(
    id integer primary key autoincrement,
    name text,
    email text,
    member_since text,
    avatar text)''')

cursor.execute(
    '''Create table if not exists group_user(
    id integer primary key autoincrement,
    id_group integer references _group(id),
    id_user integer references user(id),
    balance integer)''')

cursor.execute(
    '''Create table if not exists bill(
    id integer primary key autoincrement,
    id_group integer references _group(id),
    title integer,
    amount integer,
    date text,
    created_by integer)''')

cursor.execute(
    '''Create table if not exists bill_user_owes(
    id integer primary key autoincrement,
    id_bill integer references bill(id),
    id_user integer references user(id),
    owes integer)''')

cursor.execute(
    '''Create table if not exists bill_user_paid(
    id integer primary key autoincrement,
    id_bill integer references bill(id),
    id_user integer references user(id),
    paid integer)''')

cursor.execute(
    '''Create table if not exists note(
    id integer primary key autoincrement,
    id_bill integer references bill(id),
    id_user integer references user(id),
    massage text,
    created text)''')

print('1 - добавление данных; 2 - вывод таблиц')
choice = int(input())

if choice == 1:
    print('1 - group; 2 - bill; 3 - group_user; 4 - bill_user_owes; 5 - bill_user_paid; 6 - note; 7 - user;')
    table_choice = int(input())
    if table_choice == 1:
        name = input('Введите имя: ')
        balance = input('Введите баланс: ')
        cursor.execute('''insert into _group(name, balance) values(?, ?);''', (name, balance))
    elif table_choice == 2:
        id_group = input('Введите id группы: ')
        title = input('Введите название: ')
        amount = input('Введите сумму: ')
        date = input('Введите дату: ')
        created_by = input('Введите создателя: ')
        cursor.execute('''insert into bill(id_group, title, amount, date, created_by) values(?, ?, ?, ?, ?);''',
                       (id_group, title, amount, date, created_by))
    elif table_choice == 3:
        id_group = input('Введите id группы: ')
        id_user = input('Введите id пользователя: ')
        balance = input('Введите баланс: ')
        cursor.execute('''insert into group_user(id_group, id_user, balance) values(?, ?, ?);''', (id_group, id_user, balance))
    elif table_choice == 4:
        id_bill = input('Введите id счета: ')
        id_user = input('Введите id пользователя: ')
        owes = input('Сумма должна: ')
        cursor.execute('''insert into bill_user_owes(id_bill, id_user, owes) values(?, ?, ?);''', (id_bill, id_user, owes))
    elif table_choice == 5:
        id_bill = input('Введите id счета: ')
        id_user = input('Введите id пользователя: ')
        paid = input('Оплачено: ')
        cursor.execute('''insert into bill_user_paid(id_bill, id_user, paid) values(?, ?, ?);''', (id_bill, id_user, paid))
    elif table_choice == 6:
        id_bill = input('Введите id счета: ')
        id_user = input('Введите id пользователя: ')
        message = input('Введите сообщение: ')
        created = input('Дата создания: ')
        cursor.execute('''insert into note(id_bill, id_user, message, created) values(?, ?, ?, ?);''', (id_bill, id_user, message, created))
    elif table_choice == 7:
        name = input('Введите имя: ')
        email = input('Введите почту: ')
        member_since = input('Дата регистрации: ')
        avatar = input('URL аватара: ')
        cursor.execute('''insert into user(name, email, member_since, avatar) values(?, ?, ?, ?);''', (name, email, member_since, avatar))
    else:
        print('Неверный выбор.')

    con.commit()

elif choice == 2:
    print('1 - group; 2 - bill; 3 - group_user; 4 - bill_user_owes; 5 - bill_user_paid; 6 - note; 7 - user;')
    table_choice = int(input())

    if table_choice == 1:
        cursor.execute('''select * from _group''')
    elif table_choice == 2:
        cursor.execute('''select * from bill''')
    elif table_choice == 3:
        cursor.execute('''select * from group_user''')
    elif table_choice == 4:
        cursor.execute('''select * from bill_user_owes''')
    elif table_choice == 5:
        cursor.execute('''select * from bill_user_paid''')
    elif table_choice == 6:
        cursor.execute('''select * from note''')
    elif table_choice == 7:
        cursor.execute('''select * from user''')
    else:
        print('Неверный выбор.')

    data = cursor.fetchall()
    for row in data:
        print(row)

con.close()
