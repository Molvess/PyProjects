import pyautogui
import pyperclip
import time
from random import randint

al = input("Açmak için gerekli olan kodu yaz : ")
time.sleep(2)
if al == "Himalaya":
    while True:
        pyautogui.hotkey('ctrl', 'v', interval=0)
        pyautogui.typewrite('Rifatt',interval=0)
        pyautogui.press("enter")
        pyautogui.press("enter")