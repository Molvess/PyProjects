import tkinter as tk
import time

root = tk.Tk()
root.title("Telepone")
root.resizable(width=False, height=False)
canvas1 = tk.Canvas(root, width = 300, height = 600)
canvas1.pack()

def whatsapp ():
    whatsac = tk.Label(root,text="WHATSAPP AÇILIYOR!.",fg="green",font=('helvetica', 25, 'bold'))
    canvas1.create_window(150, 100, window=whatsac)
def aç ():
    açılıyoryazısı = tk.Label(root,text="AÇILIYORRR...",fg="green",font=('helvetica', 24, 'bold'))
    canvas1.create_window(150, 100, window=açılıyoryazısı)
    button1.destroy()
    açılıyoryazısı.destroy()
    boşluk = tk.Entry(width=10)
    canvas1.create_window(150, 130, window=boşluk)
    def parola ():
        prl = boşluk.get()
        şifragir.destroy()
        grş.destroy()
        boşluk.destroy()
        if prl == "2008":
            doruyzsı = tk.Label(root,text="ŞİFRE DOĞRU!.",fg="green",font=('helvetica', 24, 'bold'))
            canvas1.create_window(150, 100, window=doruyzsı)
            doruyzsı.destroy()
            whatsappbtn = tk.Button(text='W',width=10, height=3,command=whatsapp,bg='green',fg='white')
            canvas1.create_window(50, 100, window=whatsappbtn)               
        else:
            ynlşyazısı = tk.Label(root,text="ŞİFRE YANLIŞ!.",fg="red",font=('helvetica', 24, 'bold'))
            canvas1.create_window(150, 100, window=ynlşyazısı)
            ynlşyazısı.destroy()
            root.destroy()
        

    şifragir=tk.Label(text="Şifrenizi Yazınız",font="Arial 14 bold")
    canvas1.create_window(150, 100, window=şifragir)
    grş = tk.Button(text='GİRİŞ',width=15, height=2,command=parola,bg='brown',fg='white')
    canvas1.create_window(150, 170, window=grş)

    
button1 = tk.Button(text='AÇ',width=15, height=2,command=aç,bg='brown',fg='white')
buton = tk.Button(text="⚡",width=5, height=2,command=root.destroy, bg='red',fg='green')
buton.pack()
canvas1.create_window(150, 300, window=button1)
canvas1.create_window(280, 30, window=buton)


root.protocol('WM_DELETE_WINDOW', buton)


root.mainloop()