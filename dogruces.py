import webbrowser
import tkinter as tk
from random import randint
import time

pencere=tk.Tk()
canvas1 = tk.Canvas(pencere, width = 500, height = 600)
pencere.title("Videos")
pencere.geometry("370x220")
pencere.resizable(width=False, height=False)
canvas1.pack()

def Doğruluk ():
    s1 = "Daha sonra hafızanı silebilecek olsaydın sevgilin/hoşlandığın kişiyle ne yapmak isterdin ?"
    s2 = "İkramiye sana vurdu paranın hepsi gidecek ve sen bir zırnık kullanamıcan verdiğin kişiyi ayda 1 görebilirsin o kim olurdu?"
    s3 = "Hiç ayak tırnaklaırını yedin mi ?"
    s4 = "En sonki +18 rüyan ?"
    s5 = "Cinsel organın kaç cm ?"
    s6 = "50 Bin TL lira verecez ama 1 yıl ömründen gidecek ?"
    s7 = "Çok istediğin halde şuanda yanında olmadaığı biri varmı ?"
    s8 = "Hiç öğretmenine aşık oldun mu ?"
    s9 = "1 Milyar dolar vericez ama en yakın arkadaşın tokat manyağı yapıcaz ?"
    s10 = "En cesurce yaptığın şey ?"
    s11 = "Arkadaşının eski sevgilisi ile çıkarmıydın ?"
    s12 = ""
    s13 = ""
    s14 = ""
    s15 = ""

    zar1 = randint(1,11)
    if zar1 == 1:
        print(s1)
    elif zar1 == 2:
        print(s2)
    elif zar1 == 3:
        print(s3)
    elif zar1 == 4:
        print(s4)
    elif zar1 == 5:
        print(s5)
    elif zar1 ==6:
        print(s6)
    elif zar1 == 7:
        print(s7)
    elif zar1 == 8:
        print(s8)
    elif zar1 == 9:
        print(s9)
    elif zar1 == 10:
        print(s10)
    elif zar1 == 11:
        print(s11)
    elif zar1 == 12:
        print(s12)
    else:
        print("")
def Cesaret ():
    c1 = "Tanımadığın insanlara gözlerini hiç ayırmadan uzunca bak"
    c2 = "1 Yemek kaşığı un veya lebelebi tozu ile şarkı söylemeye çalış"
    c3 = "Gargara yaparak şarkı söyle"
    c4 = "Pencere çık ve birisinin sana el sallamasını sağla"
    c5 = "Üç adet acı biber ye"
    c6 = "Tanımadğın birini seninle 12 saniye dans etmeye ikna et"
    c7 = "Bir sihirbazlık numarası yap"
    c8 = "30 saniye birini halaya davet et"
    c9 = "Etrafında en güzel/yakışıklı adamı söyle"
    c10 = "Çiğ patatese ketçap+mayoneza bandır misss gibi ye"
    c11 = "Rastgele numara salla ve" "siparişinizigetirdim lütfen kapıyı açarmısınız" "diye ara"
    c12 = "Bir kaşık mayonez ye"
    c13 = "Bunu sana yaptıran kişi bir kağıda istediğini yazıcak ve sen bu oyun bitesiye kadar bu kağıtla durcaksın"
    c14 = "Oyundaki herkesin elini öp"
    c15 = "Oyuncunun ayakkabısını kokla"

    zar1 = randint(1,15)
    if zar1 == 1:
        print(c1)
    elif zar1 == 2:
        print(c2)
    elif zar1 == 3:
        print(c3)
    elif zar1 == 4:
        print(c4)
    elif zar1 == 5:
        print(c5)
    elif zar1 == 6:
        print(c6)
    elif zar1 == 7:
        print(c7)
    elif zar1 == 8:
        print(c8)
    elif zar1 == 9:
        print(c9)
    elif zar1 == 10:
        print(c10)
    elif zar1 == 11:
        print(c11)
    elif zar1 == 12:
        print(c12)
    elif zar1 == 13:
        print(c13)
    elif zar1 == 14:
        print(c14)
    elif zar1 == 15:
        print(c15)
    else:
        print("")

xvdsbttn = tk.Button(text="Doğruluk",width=15, height=5,command=Doğruluk, bg='white',fg='black')
pnhbbttn = tk.Button(text="Cesaretlik",width=15, height=5,command=Cesaret, bg='white',fg='black')
dctexts = tk.Label(pencere,text="Doğruluk & Cesaretlik" ,fg="green",font=('helvetica', 25, 'bold'))
xvdsbttn.pack()
canvas1.create_window(270, 155, window=xvdsbttn)
canvas1.create_window(90, 155, window=pnhbbttn)
canvas1.create_window(180, 30, window=dctexts)
pencere.mainloop()