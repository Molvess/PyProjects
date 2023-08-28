import pyautogui
from random import randint
import time

time.sleep(2)
a = 1

while a < 100:
    a += 1
    x = randint(1,1280)
    y = randint(1,1024)
    pyautogui.moveTo(x,y)
    pyautogui.click()
time.sleep(1)
pyautogui.rightClick()
pyautogui.press('down')
pyautogui.press("enter")
time.sleep(0.75)
pyautogui.press("enter")