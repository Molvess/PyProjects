import tkinter as tk

pencere=tk.Tk()
pencere.title("Buton İşlemleri")
pencere.geometry("500x500")

def butonBas():

    #entry den bilgileri alma
    adsoyad=ent1.get()
    print(adsoyad)

e1=tk.Label(text="Adı Soyadı",font="Arial 12 bold")
e1.pack()
ent1=tk.Entry(width=30)
ent1.pack()
b1=tk.Button(text="GİRİŞ",bg="black",fg="white",font="Arial 20 bold",command=butonBas)
b1.pack()

pencere.mainloop()


#
