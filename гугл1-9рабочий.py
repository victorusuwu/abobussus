import pyautogui
import time
amount=input('Введите число от 1 до 9')
amount=int(amount)
pyautogui.moveTo(179, 744)
pyautogui.click()
time.sleep(2)

for step in range(amount+1):
     
    pyautogui.hotkey('ctrl', 't')
    time.sleep(0.1)
