import pyautogui
import keyboard
import time
pole = [['o','o','o','o','o','o','o','o','o','o'],
        ['o','o','o','o','o','o','o','o','o','o'],
        ['o','o','o','o','o','o','o','o','o','o'],
        ['o','o','o','o','o','o','o','o','o','o'],
        ['o','o','o','o','o','o','o','o','o','o'],
        ['o','o','o','o','o','o','o','o','o','o'],
        ['o','o','o','o','o','o','o','o','o','o'],
        ['o','o','o','o','o','o','o','o','o','o'],
        ['o','o','o','o','o','o','o','o','o','o'],
        ['o','o','o','o','o','o','o','o','o','o']]
x=0
y=0
pole[y][x]='X'

for stroka in pole:
	for kletka in stroka:
		print(kletka,end='')
	print()
print()

while 'true':    
    if keyboard.is_pressed('right') == True:
        pole[y][x]='o'
        x=x+1
        pole[y][x]='X'
        for stroka in pole:
            for kletka in stroka:
                print(kletka,end='')
            print()
        print()
        time.sleep(0.1)
        

    if keyboard.is_pressed('left') == True:
        pole[y][x]='o'
        x=x-1
        pole[y][x]='X'
        for stroka in pole:
            for kletka in stroka:
                print(kletka,end='')
            print()
        print()
        time.sleep(0.1)     

        
    
    if keyboard.is_pressed('down') == True:
        pole[y][x]='o'
        y=y+1
        pole[y][x]='X'
        for stroka in pole:
            for kletka in stroka:
                print(kletka,end='')
            print()
        print()
        time.sleep(0.1)       

       
  
    if keyboard.is_pressed('up') == True:
        pole[y][x]='o'
        y=y-1
        pole[y][x]='X'
        for stroka in pole:
            for kletka in stroka:
                print(kletka,end='')
            print()
        print()
        time.sleep(0.1)      

        
print(stroka)