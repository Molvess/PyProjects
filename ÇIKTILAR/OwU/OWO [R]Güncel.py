import pyautogui
import time
from random import randint

al = input("Açmak için gerekli olan kodu yaz : ")

time.sleep(2)
if al == "Himalaya":
    time.sleep(2)
    while True:
        owoçek = randint(5,1000)
        pyautogui.typewrite(f"owo wh {owoçek}",interval=2.75)
        pyautogui.press("enter")
        time.sleep(3)
        pyautogui.typewrite(f"owo wb {owoçek}",interval=2.75)
        pyautogui.press("enter")
