import random
print('Привет это игра камень ножницы бумага 1-камень 2-ножницы 3-бумага')
bot=random.randint(1,3)
schet = 0
bot = 0
schet=int(schet)
bot=int(bot)    

while bot <3 and schet <3:
    
    ti =input('камень ножницы бумага')
    ti = int(ti)
    schet = 0
    bot = 0
    schet=int(schet)
    bot=int(bot)
    bot=random.randint(1,3)
    if ti == bot:
        print('одинаково переигрываем')
        
        
    elif bot == 1 and ti == 3:
        print('Бот выбрал камень,Вы победили')
        schet+1  
    elif bot == 2 and ti == 3:
        print('Бот выбрал ножницы Вы проиграли')
        bot+1
    elif bot == 3 and ti == 2:
        print('бот выбрал бумагу Вы победили ')
        schet+1
    elif bot == 1 and ti == 2:
        print('бот выбрал камень Вы проиграли')
        bot+1
    elif bot == 2 and ti == 1:
        print('бот выбрал ножницы Вы победили')
        schet+1
    elif bot == 3 and ti == 1:
        print('бот выбрал бумагу Вы проиграли')
        bot+1
if bot>schet:
    print('робот победил')
elif bot<schet:
    print('вы победили')
