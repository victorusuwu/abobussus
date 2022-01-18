log = input('ТЕПЕРЬ ВВЕДИ ЛОГИН БОТ')
pas = input('введите пароль')
ent = log+pas

while ent != 'баблквас' :
    print('логин или пароль неверен)
    log = input('логин ')
    pas = input('ПАРОЛЬ ВВОДИ')
    ent = log+pas
print('Вот теперь ВЕРНО!')
