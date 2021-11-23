import pyautogui
import time
import keyboard
ask = input('какой запрос вы хотите узнать в браузере')

number = input('введите номер вкладки')
pyautogui.moveTo(280, 750)
pyautogui.click()
time.sleep(1)
pyautogui.press('ctrl')
time.sleep(0.05)


pyautogui.hotkey('ctrl','t')
time.sleep(0.05)
pyautogui.hotkey('ctrl','t')
time.sleep(0.05)

pyautogui.hotkey('ctrl','t')
time.sleep(0.05)

pyautogui.hotkey('ctrl','t')
time.sleep(0.05)

pyautogui.hotkey('ctrl','t')
time.sleep(0.05)

pyautogui.hotkey('ctrl','t')
time.sleep(0.05)

pyautogui.hotkey('ctrl','t')
time.sleep(0.05)

pyautogui.hotkey('ctrl','t')
time.sleep(0.05)

pyautogui.hotkey('ctrl','t')
time.sleep(0.05)
pyautogui.hotkey('ctrl',number)


pyautogui.moveTo(1000, 55)
pyautogui.click()
pyautogui.press('del')
time.sleep(1)
pyautogui.click()
keyboard.write(ask)
pyautogui.press('enter')