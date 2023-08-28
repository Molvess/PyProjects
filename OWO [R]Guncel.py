import pyautogui
import time
from random import randint

al = input("Açmak için gerekli olan kodu yaz : ")

time.sleep(2)
if al == "Himalaya":
    while True:
        owocek = randint(100,1500)
        pyautogui.typewrite(f'owo cf {owocek}',interval=2.75)
        pyautogui.press("enter")