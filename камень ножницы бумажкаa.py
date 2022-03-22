import random
print('Привет это игра камень ножницы бумага 1-камень 2-ножницы 3-бумага')
bot=random.randint(1,3)
ti =input('камень ножницы бумага')
ti = int(ti)
if ti == bot:
    print('одинаково переигрываем')
    bot=random.randint(1,3)
    ti =input('камень ножницы бумага')
elif bot == 1 and ti == 3:
    print('Вы победили')
elif bot == 2 and ti == 3:
    print('Вы проиграли')
elif bot == 3 and ti == 2:
    print('Вы победили ')
elif bot == 1 and ti == 2:
    print('Вы проиграли')
elif bot == 2 and ti == 1:
    print('Вы победили')
elif bot == 3 and ti == 1:
    print('Вы проиграли')
