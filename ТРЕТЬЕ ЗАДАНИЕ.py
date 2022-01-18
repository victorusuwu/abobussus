log = input('ТЕПЕРЬ ВВЕДИ ЛОГИН БОТ')
pas = input('введите пароль')
ent = log+pas

while ent != 'баблквас' :
    if log == 'бабл':
        print ('пароль не верен')
    else:
        print('логин не верен')
    
    log = input ('логин')
    pas = input ('пароль')
    ent = log+pas
print ('вход успешен')

   