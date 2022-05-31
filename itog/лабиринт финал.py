import keyboard
import pyautogui
import time

print('''Привет это игра лабиринт))
В этой игре вы должны дойти до финиша(!)
Не натыкаясь на стены (#)''')
play = True
while play == True:
    ckin = input('''Какой скин вы хотите?
Вы можете можете выбрать его сами!!
(напишите 1 букву или символ и он станет вашим скином кроме знака "#" и ".") ''')
    yroven = input('''В этой игре есть 3 сложности,
Если вы хотите играть в очень лёгкую версию напишите "легко",
Если вы хотите играть в сложную версию напишите "сложно" ''')
    if yroven == "легко":
        pole =[[".", "#", "!", ".", ".", "#", "#"],
                [".", "#", "#", "#", ".", ".", "."],
                [".", ".", ".", "#", "#", "#", "."],
                ["#", "#", ".", "#", "#", "#", "."],
                [".", ".", ".", "#", ".", ".", "."],
                [".", "#", "#", "#", ".", "#", "#"],
                [".", ".", ".", ".", ".", "#", "#"]]
        stroka = 0
        stolb = 0
        pole [0][0] = ckin
        game = True
        def vivod ():
            for stroka in pole:
                for kletka in stroka:
                    print (kletka, end = "")
                print()
        vivod()
        otvet=''
        while game == True:
            otvet=input('чтобы двигатся пишите w a s или d ижмите enter')






            if otvet == "d":
                if stolb == 6:
                    otvet = input ("Вы дошли до края: ")
                else:
                    time.sleep(0.1) 
                    pole [stroka] [stolb] = "."
                    stolb = stolb + 1
                    if pole [stroka][stolb] == "#":
                        stolb = 0
                        pole [0] [0] = ckin
                    else:
                        pole [stroka] [stolb] = ckin
                vivod()
            if otvet == "a":
                if stolb == 0:
                    otvet = input ("Вы дошли до края: ")
                else:
                    time.sleep(0.1) 
                    pole [stroka] [stolb] = "."
                    stolb = stolb - 1
                    if pole [stroka][stolb] == "#":
                        stolb = 0
                        pole [0] [0] = ckin
                    else:
                        pole [stroka] [stolb] = ckin
                vivod()
            if otvet == "w":
                if stroka == 0:
                    otvet = input ("Вы дошли до края: ")
                else:
                    time.sleep(0.1) 
                    pole [stroka] [stolb] = "."
                    stroka = stroka - 1
                    if pole [stroka][stolb] == "#":
                        stroka = 0
                        pole [0] [0] = ckin
                    else:
                        pole [stroka] [stolb] = ckin
                vivod()
            if otvet == "s":
                time.sleep(0.1) 
                if stroka == 6:
                    otvet = input ("Вы дошли до края: ")
                else:
                    time.sleep(0.1) 
                    pole [stroka] [stolb] = "."
                    stroka = stroka + 1
                    if pole [stroka][stolb] == "#":
                        stroka = 0
                        pole [0] [0] = ckin
                    else:
                        pole [stroka] [stolb] = ckin
                vivod()
            if pole[0][2] == ckin:
                print('''Урааа вы выйграли!!!!!
Давайте сыграем заново на этой же сложности или на другой;) ''')
                game = False
    if yroven == "сложно":
        pole = [[".", ".", ".", ".", "#", ".", ".", ".", ".", "!"],
                ["#", "#", "#", ".", "#", ".", "#", "#", "#", "#"],
                [".", ".", "#", ".", "#", ".", "#", "#", ".", "#"],
                [".", "#", "#", ".", "#", ".", ".", "#", ".", "#"],
                [".", "#", ".", ".", "#", ".", "#", "#", ".", "#"],
                [".", ".", ".", ".", "#", ".", "#", ".", ".", "#"],
                [".", "#", "#", "#", "#", ".", "#", ".", ".", "."],
                [".", "#", ".", ".", ".", ".", ".", ".", "#", "."],
                [".", "#", "#", "#", "#", ".", "#", ".", "#", "."],
                [".", ".", ".", ".", ".", ".", "#", ".", ".", "."]]
        stroka = 0
        stolb = 0
        pole [0][0] = ckin
        game = True
        def vivod ():
            for stroka in pole:
                for kletka in stroka:
                    print (kletka, end = "")
                print()
        vivod()
        while game == True:
            otvet =  input("""
Напишите w, a, s или d: """)
            if otvet == "d":
                if stolb == 9:
                    otvet = input ("Вы дошли до края: ")
                else:
                    pole [stroka] [stolb] = "."
                    stolb = stolb + 1
                    if pole [stroka][stolb] == "#":
                        stolb = 0
                        pole [0] [0] = ckin
                    else:
                        pole [stroka] [stolb] = ckin
                vivod()
            if otvet == "a":
                if stolb == 0:
                    otvet = input ("Вы дошли до края: ")
                else:
                    pole [stroka] [stolb] = "."
                    stolb = stolb - 1
                    if pole [stroka][stolb] == "#":
                        stolb = 0
                        pole [0] [0] = ckin
                    else:
                        pole [stroka] [stolb] = ckin
                vivod()
            if otvet == "w":
                if stroka == 1:
                    otvet = input ("Вы дошли до края: ")
                else:
                    pole [stroka] [stolb] = "."
                    stroka = stroka - 0
                    if pole [stroka][stolb] == "#":
                        stroka = 0
                        pole [0] [0] = ckin
                    else:
                        pole [stroka] [stolb] = ckin
                vivod()
            if otvet == "s":
                if stroka == 9:
                    otvet = input ("Вы дошли до края: ")
                else:
                    pole [stroka] [stolb] = "."
                    stroka = stroka + 1
                    if pole [stroka][stolb] == "#":
                        stroka = 0
                        pole [0] [0] = ckin
                    else:
                        pole [stroka] [stolb] = ckin
                vivod()
            if pole[0][9] == ckin:
                print('''Урааа вы выйграли!!!!!
Давайте сыграем заново на этой же сложности или на другой;) ''')
                