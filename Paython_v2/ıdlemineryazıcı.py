import pyautogui
import time

def deneme():
    for sayi in sayilar:
        pyautogui.typewrite(str(sayi))
        pyautogui.press("enter")
        #time.sleep(0.50)

dosya = open(r"C:\Users\Bekirx00\Desktop\Paython\ıdleminercode.txt", "r")
sayilar = []
for satir in dosya:
    satir = satir.strip()
    if satir.isdigit() and int(satir) not in sayilar:
        sayilar.append(int(satir))
dosya.close()

al = input("Şifre;")
al = al.upper()
if al == "BAŞLA":
    time.sleep(3)
    deneme()
else:
    exit()

