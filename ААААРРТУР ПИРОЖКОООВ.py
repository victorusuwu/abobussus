import pyautogui
import time
number = input('введите номер вкладки')
pyautogui.moveTo(280, 750)
pyautogui.click()
pyautogui.hotkey('ctrl',number)
pyautogui.moveTo(1000, 55)
pyautogui.click()
pyautogui.press('del')
time.sleep(1)
pyautogui.click()
pyautogui.write('Artur Pirozhkov')
pyautogui.press('enter')





