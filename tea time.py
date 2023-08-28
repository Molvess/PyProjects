import time

İçecekler = ["Çay","Ihlamur","Adaçayı","İcetea","Milkshake","Nescafe","Kola","Fanta","Sprite"]
print(İçecekler[0])
print(İçecekler[1])
print(İçecekler[2])
print(İçecekler[3])
print(İçecekler[4])
print(İçecekler[5])
print(İçecekler[6])
print(İçecekler[7])
print(İçecekler[8])
time.sleep(2)
print("ÇAY İÇİN 1'E BASINIZ : ")
print("IHLAMUR İÇİN 2'YE BASINIZ : ")
print("ADAÇAYI İÇİN 3'E BASINIZ : ")
print("İCETEA İÇİN 4'E BASINIZ : ")
print("MİLKSHAKE İÇİN 5'E BASINIZ : ")
print("NESACFE İÇİN 6'YA BASINIZ : ")
print("KOLA İÇİN 7'YE BASINIZ : ")
print("FANTA İÇİN 8'E BASINIZ : ")
print("SPRİTE İÇİN 9'A BASINIZ : ")

SayıAlma = int(input("RAKAMI TUŞLAYINIZ : "))

if SayıAlma == 1:
    print("\nÇAYLARRRR\n")
elif SayıAlma == 2:
    print("\nIHLAMUR GELİYOOOO\n")
elif SayıAlma == 3:
    print("\nADAÇAYIIII\n")
elif SayıAlma == 4:
    print("\nİCETEA BUZZ GİBİ\n")
elif SayıAlma == 5:
    print("\nBUZLU BUZLU MİLKSHAKE\n")
elif SayıAlma == 6:
    print("\nSICACIK NESCAFE\n")
elif SayıAlma == 7:
    print("\nKOKOKOLA\n")
elif SayıAlma == 8:
    print("\nFANTACIK\n")
elif SayıAlma == 9:
    print("\nSPRİTE ÇARPAN FERAHLIK\n")
else:
    print("BİŞİYE TIKLA")