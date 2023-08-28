import time

name = input("Terse dönüştürmek istediğiniz kelimeyi yazınız : ")
tn = str(name[::-1])
print(tn)

l = "Kayıt başlatılıyor.".center(25,"*")
print(*l)
kaydet = open("kayit.txt","w",encoding="utf8")                   #open dosya açar 
print(tn,file=kaydet)                                 #print file ile kaydeder
o = "Bilgiler kaydedildi !".center(50,"*")
print(*o)