print('вы лежали в кровати и спали как вдруг проснулись от страннного шума,вы посмотрели на время,на часах было 3 часа ночи.что вы выберете остатся в кровати(y)или пойти проверить источник шума (x)')
qfirst = input('введите вариант ответа')
if qfirst == 'y':
    print ('вы остались прятатся в кровати а шум превратился в страшные звуки которые постепенно приближались к вам,что вы решите делать прятяться(X) защиатся(Y)')
    qsec = input('введите вариант ответа')
    if qsec == 'y':
        print ('вы оглядели комнату и обнаружили телефон(x)ящик с оружием(y) и лопату(z)')
        qsrd =input('введите вариант ответа')
        if qsrd == 'x':
            print ('вы взяли свой телефон и спрятались под одеялом')
            print ('нечто зашло в комнату и оказалось что это был напившийся отчим который хочет использовать вас как закуску,он ходил по комнате в поисках вас и у вас осталось чуть больше минуты чтобы что нибудь предпренять,вы открывайте телефон открыть папку игры(x)позвонить спасателям (y)инстаграмм (z)')
            qfth =input('введите вариант ответа')
            if qfth == 'x':
                print('выберете игру бравл старс-x райз оф киндомс-y рэйд шэдоу легендс-z')
                qsth =input('введите вариант ответа')
                if qsth == 'x':
                    print('Вы вызывали отчима на дуэль на мортисах выбрать мортиса-x выбрать шелли-y')
                    qsix =input('введите вариант ответа')
                    if qsix == 'x':
                        print('вы пошли на честную дуэль но отчим оказался скиловее и он вынес вас и съел.Плохая концовка')
                    elif qsix == 'y':
                             print('вы были умнее отчима и пикнули шелли.вы попустли бота и закибербулили отчима.Хорошая концовка')
                elif qsth =='y':
                    print('только вы открыли райз оф кингдомс как отчим нашел вас Вы-СТОЙ НЕ ЕШЬ МЕНЯ Отчим-почему я не должен есть тебя?Вы У МЕНЯ ДЕСЯТЬ МИЛЛИОНОВ МОЩИ В РАЙЗ ОФ КИНГДОМС отчим-ЧТОООО НА КАК ТЫ ДОСТИХ ТАКОГО УСПЕХА ВЕДЬ ТЫ ТОЛЬКО НЕДАВНО НАЧАЛ ИГРААААТЬ????Вы-Я ВЫБРАЛ ВИКИНГОВ ВЕДЬ У НИХ ЕСТЬ 5 ПРОЦЕНТОВ БОНУСА АТАКИ А ТАК ЖЕ 15 ПРОЦЕНТОВ БОНУСА К СБОРУ НАГРАБЛЕННЫХ РЕСУРСОВ И КОНТРАТАААКЕЕ Отчим-Я ХОЧУ БЫТЬ ТВОИМ СЛУГООЙ О МОЙ ПАВЕЛИТИЛЬ.Отличная концовка ')
                elif qsth =='z':
                    print('Вы-СТОЙ НЕ ЕШЬ МЕНЯ Отчим-почему я не должен есть тебя? Вы-ведь есть афигенная игра рэйд шэдоу лэээдженс ЗАХВАТЫВАЮЩАЯ ИГРА В ЖАНРЕ ММО РПГ СРАЖАЙСЯ С СОТНЯМИ ГЕРОЕВ ИЗ БОЕЕ 14 ФРАКЦИЙ А СКАЧАВ ИГРУ ПО ССЫЛКЕ В ОПИСАНИИ ВЫ ПОЛУЧИТЕ 20 ТЫСЯЧ СЕРЕБРА 5 БЕСПЛАТНЫХ ПРИЗЫВОВ И ПРЕМИУМ НА НЕДЕЛЮЮЮЮЮ Отчим-ВААУ КАКАЯ ИНТЕРЕСНАЯ ИГРА ПОЙДУ СКАЧАЮ *ушел качать*а вы забрали кучу денег с рекламы и убежали.Хорошая концовка')                  
        elif qsrd == 'y':
           qeth=input('вы открыли ящик с оружием и нашли там дробовик(x)зонтик(y)и шарф(Z)')
           if qeth =='x':
               print('вы берете дробовик и первращайтесь в шелли говорите летс гоу блен блен и ультуйте в отчима разнося все на своем пути-хорошая концовкa') 
           elif qeth == 'y':
               print('вы взяли зонтик и стали пайпер ультуйтеи улетайте из дома раскидывая гранаты и взрывая пол хаты-поздравляем вы опять бездомный')
           elif qeth == 'z' :
               print('ты надеваеш шарф шарф и становишся zxc 1000-7 dead inside эдгаром и размазываешь отчима кагуне и люто крутишся с дизом но вас крысит булл-плохая концовка')
           
        elif qsrd == 'z':
            print('вы взяли лопату но она слишком большая чтобы прятатся в кровати поэтому вы спрятались в шкафу')
            print('когда отчим нагнулся чтобы поискать вас  под кроватью то вы выходите из шкафа и говорите НЮХАЙ БЕБРУ и выносите отчима бесконечной ультой мортиса ')
            print('хорошя концовка ')
    elif qsec == 'x':
        print('вы умерли ')







elif qfirst == 'x':
    print('вы умерли без обяснения причины')