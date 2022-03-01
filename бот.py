import pyautogui
import keyboard
import time
while True:
    command = input('введите нужную комманду')
    if command == 'поиск':
        ask = input('введите свой запрос')
        pyautogui.moveTo(280, 750)
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(1)
        pyautogui.press('ctrl')
        time.sleep(0.5)
        pyautogui.moveTo(1000, 55)
        pyautogui.click()
        pyautogui.press('del')
        time.sleep(1)
        pyautogui.click()
        keyboard.write(ask)
        pyautogui.press('enter')
    if command == 'текст':
        pyautogui.hotkey('win', 'r')
        keyboard.write('notepad')
        pyautogui.press('enter')

    if command == 'выход':
        keyboard.write('exit()')
        keyboard.write('типа все закрылось')
    if command == 'займ':
        print('ЗДРАВСТВУЙТЕ вас приветствует  компания zaim bez skama228')
        name = input('Как вас зовут?')
        s = int(input('на какую сумму вы хотите взять займ? '+(name)))
        n = int(input('сколько лет вы хотите  выплачивать проценты'+'введите число'))
        p = int(input('под какой процент вы хотите взять займ? '+(name)+' введите число'))
        r = p/100
        print (r)
        m = (s * r*(1 + r)*n) / (12 * ((1+r)*n-1))

        print('каждый месяц вы должны платить'+str(m) )
    if command == 'калькулятор':
        num1 = input("введите с какое знак действия которое  вы хотите совершить")
        first = input("введите первое число")
        seck = input("введите второе число")
        num2 =int(first)
        num3 =int(seck)
        if num1 == ("+"):
            answer = num2 + num3
            print(answer)
        elif num1 == ("-"):
            answer = num2 - num3
            print(answer)
        elif num1 == ("/"):
            answer =  num2 / num3
            print(answer)
        elif num1 ==("*"):
            answer = num2 * num3
            print(answer)
        else:
            print ("неверный знак")
    if command == 'факториал':
        n = input('введите число')
        n = int(n)
        fact = 1
        for step in range(1, n+1 ): 
            fact = fact * step
        print(fact)
    if command == 'автокликер':
        pyautogui
        import time
        time.sleep(30)
        a = (pyautogui.position())
        pyautogui.moveTo(a)
        while True:
            pyautogui.click()

    else:
        print('НЕВЕРНАЯ КОМАНДААААА') 

