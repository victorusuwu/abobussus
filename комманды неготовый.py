import pyautogui
import keyboard
import time
command = input('введите нужную комманду')
if command == 'поиск':
    ask = input('введите свой запрос')
    pyautogui.moveTo(280, 750)
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

