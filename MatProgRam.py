import os
import time

grşisn = int(input("Yapmak istediğiniz işlemi seçiniz \nDiktörgen işlemleri için 1'e basınız\nKare işlemleri için 2'e basınız\nÜçgen işlemleri için 3'e basınız\nDaire işlemleri için 4'e basınız\nHesap makinesi işlemleri için 5'e basınız\nÖzel işlemler için 6'ya tıklayınız\n:"))
def Dikdörgen ():
    dktistnn = int(input("Dikdörtgenin çevresi için 1'e basınız\nDikdörtgenin alanı için 2'e basınız\n:"))

    def dkdrgnçvr ():
        sayı = int(input("Uzun kenar = "))
        sayı2 = int(input("Kısa kenar = "))
        print("Diktörgenin çevresi :" , (sayı + sayı2) * 2)

    def dkdrgnaln ():
        sayı = int(input("Uzun kenar = "))
        sayı2 = int(input("Kısa kenar = "))
        print("Diktörgenin alanı : " , sayı * sayı2)

    if dktistnn == 1:
        dkdrgnçvr()
    elif dktistnn == 2:
        dkdrgnaln()
def Kare ():

    kareisttn = int(input("Karenin çevresi için 1'e basınız\nKarenin alanı için 2'e basınız\n:"))

    def kareçvr ():
        sayı = int(input("Kenar ="))
        print("Karenin çevresi : ", sayı*4)
    def karealn ():
        sayı = int(input("Kenar = "))
        print("Karenin alanı : ", sayı*2)

    if kareisttn == 1:
        kareçvr()
    elif kareisttn == 2:
        karealn()
def Üçgen ():
    üçgnisttn = int(input("Üçgenin çevresi için 1'e basınız\nÜçgenin alanı için 2'e basınız\nÜçgenin iç açılarınnın toplamını bulmak için 3'e basınız\nÜçgenin 3.bilinmeyen açısını bulmak için 4'e basınız\n:"))
    def üçgnçvr ():
        bkenar = int(input("1.Kenarı giriniz = "))
        ikenar = int(input("2.Kenarı giriniz = "))
        ükenar = int(input("3.Kenarı giriniz = "))
        print("Üçgenin çevresi : ", bkenar+ikenar+ükenar)
    def üçgnaln ():
        taban = int(input("Tabanı giriniz = "))
        yükseklik = int(input("Yüksekliği giriniz = "))
        print("Üçgenin alanı : ",taban*yükseklik/2)
    def üçgniçtplm ():
        baçı = int(input("1.Açıyı giriniz = "))
        iaçı = int(input("2.Açıyı giriniz = "))
        üaçı = int(input("3.Açıyı giriniz = "))
        print("Üçgenin iç açılarının toplamı : ",baçı+iaçı+üaçı)
    def blnmyaçlıüçgn ():
        baçı = int(input("1.Açıyı giriniz = "))
        iaçı = int(input("2.Açıyı giriniz = "))
        sonuç = 180-baçı+iaçı
        if sonuç >= 180:
            print("Kayıp açınız : ",sonuç)
        elif sonuç < 180:
            print("Sallama götünden kanks")
            
        

    if üçgnisttn == 1:
        üçgnçvr()
    elif üçgnisttn == 2:
        üçgnaln()
    elif üçgnisttn == 3:
        üçgniçtplm()
    elif üçgnisttn == 4:
        blnmyaçlıüçgn()
def Daire ():
    daireistnn = int(input("Dairenin çevresi için 1'e basınız\nDairenin alanı için 2'e basınız\n:"))
    
    PI = 3.14

    def daireçvr ():
        yarıçap = int(input("Yarıçapı giriniz"))
        print("Dairenin çevresi : ",2*PI*yarıçap)
    def dairaln ():
        yarıçap = int(input("Yarıçapı giriniz"))
        print("Dairenin alanı : ",PI*yarıçap**2)
    
    if daireistnn == 1:
        daireçvr()
    elif daireistnn == 2:
        dairaln()
def HESAP ():
    hspistnn = int(input("Hesap makinesini terminalde kullanmak için 1'e basınız\nHesap makinesini uygulama olarak kullanmak için 2'ye basınız\n:"))
    def HspTrmnl ():
        trmnlklln = input()
        print("Sonucunuz : ",eval(trmnlklln))
    def Hspmknsprogram ():
        os.system("C:\\Windows\\system32\\calc.exe")

    if hspistnn == 1:
        HspTrmnl()
    elif hspistnn == 2:
        Hspmknsprogram()
def Özel():
    iste = int(input("Faktör işlemi için 1'e basınız\n"))
    def fnksyn():
        a = 1
        rkm = int(input("Faktörünü bulmak istediğiniz rakamı yazınız\n"))
        for i in range(rkm):
            a = a * (i+1)
        print()
        
    if iste == 1:
        fnksyn()

if grşisn == 1:
    Dikdörgen()
elif grşisn == 2:
    Kare()
elif grşisn == 3:
    Üçgen()
elif grşisn == 4:
    Daire()
elif grşisn == 5:
    HESAP()
elif grşisn == 6:
    Özel()
else:
    print("Yanlış tuş kullanımı")
    exit()












