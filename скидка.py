num = int(input('введите вашу сумму заказа'))
price =num-(num/100*30)
if num > 1000:

    print('со скидкой 30 процентов ваш заказ составил'+ str(price) )

else:
    print('на васскидка не распространяется,стоимость заказа'+str(num))
