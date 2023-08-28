okul= "İstanbul Medipol Üniversitesi"

isim= input("Adınızı giriniz= ")
soyisim= input("Soyadınızı giriniz= ")
okul=  input("Okulunuzu giriniz= ")

y1,y2,y3,y4,y5 = "Kırmızı Mercimek Çorba","Tavuk Döner","Patates Musakka","Soslu Sebze Kızartma","Nohutlu Pilav"
İ1,i2 = "Ayran","Kola"
y1 = 15
y2 = 20
y3 = 30
y4 = 25
y5 = 20
i1 = 5
i2 = 10


if okul == okul:
    print(" 1.Kırmızı Mercimek Çorba: 15 TL\n 2.Tavuk Döner: 20 TL\n 3.Patates Musakka: 30 TL\n 4.Soslu Sebze Kızartma: 25 TL\n 5.Nohutlu Pilav: 20 TL\n İÇECEKLER\n   6.Ayran 5 TL\n   7.Kola: 10 TL")
    birinci_yemek=(input("Almak istediğiniz 1. yemeğin numarasını giriniz: "))
    
    if birinci_yemek == "1":
        ikinci_yemek = input("Almak istediğiniz 2. yemeğin numarasını giriniz: ")
        if ikinci_yemek == "1":
            icecek = input("Almak isteidğiniz içeceğin kodunu yazınız: ")
            if icecek == "6":
                print(f"{isim}+{soyisim}",y1+y1+i1,"TL tutmaktadır")

else:
    print("Okulun bir öğrencisi değilsiniz.")

