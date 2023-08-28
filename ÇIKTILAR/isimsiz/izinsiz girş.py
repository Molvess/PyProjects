import webbrowser
import tkinter as tk 
kullanici_adi = "fearless"
passwürd = "öşeg07"
akullanıcıadı = input("KULLANICI ADI GİRİNİZ : ")
apassword = input("ŞİFRENİZİ GİRİNİZ : ")

if (kullanici_adi == akullanıcıadı) + (passwürd == apassword):
    pencere=tk.Tk()
    canvas1 = tk.Canvas(pencere, width = 500, height = 600)
    pencere.title("Videos")
    pencere.geometry("370x190")
    pencere.resizable(width=False, height=False)
    canvas1.pack()
    def Xvds ():
        url = "https://www.xvideos.com/"
        chrome_path = "C:\\Users\\Abdullah\\AppData\\Local\\Programs\\Opera GX\\launcher.exe"
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url)
    def pnhb ():    
        url = "https://www.pornhub.com/"
        chrome_p = "C:\\Users\\Abdullah\\AppData\\Local\\Programs\\Opera GX\\launcher.exe"
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_p))
        webbrowser.get('chrome').open_new_tab(url)
    xvdsbttn = tk.Button(text="XVideos",width=15, height=5,command=Xvds, bg='white',fg='black')
    pnhbbttn = tk.Button(text="PornHub",width=15, height=5,command=pnhb, bg='white',fg='black')
    xvdsbttn.pack()
    canvas1.create_window(270, 90, window=xvdsbttn)
    canvas1.create_window(90, 90, window=pnhbbttn)
    pencere.mainloop()









