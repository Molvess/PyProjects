import webbrowser
import os
import pyautogui
from random import randint
import time
import urllib.request

sec = int(input("\nKur seçecenği için 1'e basınız\nTerse döndür seçecenği için 2'e basınız\nFFYH seçeneği için 3'e basınız\nArama seçeneği için 4'e basınız\nHava durumu için 5'e basınız\nÇeviri için 6'ya basınız\nOyun için 7'ye kadar\nSaatkaç komudu için 8'e basınız\nNFT komudu için 9'a basınız\nResimçek komduu için 10'a basınız\nBAĞIR komudu için 11'e basınız\nHSP komudu için 12'e basınız\n"))

def Arama ():
        rgow = input("Aramak istediğiniz kelimeyi yazınız : ")
        url = f"https://tr.wikipedia.org/wiki/{rgow}"
        url2 = f"https://www.google.com/search?q={rgow}"
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url)
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url2)
def HavaDurumu ():
        istn = input("Hava durumuna bakmak istediğiniz şehri yazınız : ")
        url = f"https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il={istn}"
        url2 = f"https://www.google.com.tr/search?q={istn}+hava+durumu&sxsrf=APq-WBs9IyUxZ_TxodB0-dypUFu1Nmi0vA%3A1645219369087&ei=KQ4QYufpBO-Vxc8P0Zap4Ag&ved=0ahUKEwinosngl4r2AhXvSvEDHVFLCowQ4dUDCA4&uact=5&oq=Ayd%C4%B1n+hava+durumu&gs_lcp=Cgdnd3Mtd2l6EAMyBwgjELADECcyBwgAEEcQsAMyCggAEEcQsAMQyQMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAELADEENKBAhBGABKBAhGGABQAFgAYLkEaAFwAXgAgAEAiAEAkgEAmAEAyAEKwAEB&sclient=gws-wiz"
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url)
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url2)
def Çeviri():
        istn = input("Çevrilmesini istediğiniz kelimeyi yazınız : ")
        url = f"https://www.google.com/search?q={istn}+%C3%A7eviri&sxsrf=APq-WBtDo8bEWqOLXS5qkXwqdnSn6smooA%3A1647873911425&ei=d484Ysi-GaiJxc8P5vq7YA&ved=0ahUKEwiI1v_YuNf2AhWoRPEDHWb9DgwQ4dUDCA4&uact=5&oq=died+%C3%A7eviri&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQDRAeMggIABAIEA0QHjoHCCMQsAMQJzoHCAAQRxCwAzoHCAAQsAMQQzoSCC4QxwEQ0QMQyAMQsAMQQxgBOg8ILhDUAhDIAxCwAxBDGAE6BwgjELECECdKBAhBGABKBAhGGAFQwwZY3wpg7QtoAXABeACAAZcBiAGvBJIBAzAuNJgBAKABAcgBEcABAdoBBggBEAEYCA&sclient=gws-wiz"
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url)
def Oyun ():
    al = ("Valorant için 1'e tıklayınız\nFIFA için 2'ye tıklayınız\nLol için 3'e tıklayınız\n")
    def valo():
        os.system("C:\\Users\\Abdullah\\Desktop\\oyunlar\\VALORANT.lnk")
    def fıfa():
        os.system("C:\\Users\\Abdullah\\Desktop\\oyunlar\\FIFAMobile.lnk")
    def lel():
        os.system("C:\\Users\\Abdullah\\Desktop\\oyunlar\\League Of Legends.lnk")

    if al == 1:
        valo()
    elif al == 2:
        fıfa()
    elif al == 3:
        lel()
    al = input("Hangi NFT türünü seçiceksiniz : \n Mozaik ise 1'i\nCPaint ise 2'ye basınız")
    def Mozaik ():
        url = "https://mondrianandme.com/"
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url)

        time.sleep(2)

        a = 1

        while a < 100:
            a += 1
            x = randint(1,1920)
            y = randint(1,1080)
            pyautogui.moveTo(x,y)
            pyautogui.click()
        time.sleep(2)
        pyautogui.rightClick()
        pyautogui.press('down')
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.press("enter")
    def CPaint ():
        url = "https://jacksonpollock.org/"
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url)

        time.sleep(2)

        a = 1

        while a < 100:
            a += 1
            x = randint(1,1920)
            y = randint(1,1080)
            pyautogui.moveTo(x,y,1)
            pyautogui.click()
        time.sleep(2)
        pyautogui.rightClick()
        pyautogui.press('down')
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.press("enter")

    if al == 1:
        Mozaik()
    elif al == 2:
        CPaint()


if sec == 4:
    Arama()
elif sec == 5:
    HavaDurumu()
elif sec == 6:
    Çeviri()
elif sec == 7:
    Oyun()
