import pyautogui
import webbrowser
import tkinter as tk 

kullanıcıadı = "molvess"
password = str('NutakU')
akullanıcıadı = input("KULLANICI ADI GİRİNİZ : ")
apassword = input("ŞİFRENİZİ GİRİNİZ : ")

if (kullanıcıadı == akullanıcıadı) + (password == apassword):
    pencere=tk.Tk()
    canvas1 = tk.Canvas(pencere, width = 300, height = 600)
    pencere.title("NUTAKU")
    pencere.geometry("350x170")
    pencere.resizable(width=False, height=False)
    canvas1.pack()
    def NutakuAç ():
        url = "https://www.nutaku.net/home/"
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url)
        pyautogui.moveTo(1167, 54,2)
        pyautogui.leftClick()
        pyautogui.moveTo(1132, 467,5)
        pyautogui.leftClick()
        pyautogui.press("F5")
    def Nutakukapat ():
        url = "http://www.ismycomputeron.com/"
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url)
        pyautogui.moveTo(1167, 54,2)
        pyautogui.leftClick()
        pyautogui.moveTo(1132, 467,2)
        pyautogui.leftClick()
        pyautogui.moveTo(1259, 5,1)
        pyautogui.leftClick()

    buton = tk.Button(text="NUTAKU KAPAT",width=15, height=3,command=Nutakukapat, bg='white',fg='black')
    buton1 = tk.Button(text="NUTAKU AÇ",width=15, height=3,command=NutakuAç, bg='white',fg='black')
    buton.pack()
    canvas1.create_window(250, 80, window=buton)
    canvas1.create_window(70, 80, window=buton1)
    pencere.mainloop()
