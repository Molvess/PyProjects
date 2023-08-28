import random
import time

sorular = [
    "En büyük gezegen hangisidir?",
    "Python dilinin yaratıcısı kimdir?",
    "Türkiye'nin başkenti neresidir?",
    "Dünyadaki en uzun nehir hangisidir?"
    # Soru listesini istediğiniz kadar uzatabilirsiniz
]

def rastgele_soru():
    soru = random.choice(sorular)
    return soru

kullanici_adi = input("Lütfen kullanıcı adını giriniz : ")
password = input("Şifrenizi giriniz : ")
password2 = input("Tekrardan Şifrenizi giriniz : ")
while True:
        if password == password2:
            print("BAŞARIYLA KAYIT OLDUNUZ :D ")
            kullanıcıadı = kullanici_adi
            password = password
            akullanıcıadı = input("KULLANICI ADI GİRİNİZ :")
            apassword = input("ŞİFRENİZİ GİRİNİZ :")
            while True:
                    if apassword+password == akullanıcıadı+kullanıcıadı:
                        print("BAŞARIYLA Sisteme girdiniz")
                        print("Kullanıcı adınız : ", kullanıcıadı )
                        print("Şifreniz : ",password)
                        while True:
                            input("Bir soru için Enter tuşuna basın...")
                            soru = rastgele_soru()
                            print(soru)
                        break
                    elif apassword!=password:
                        print("Şifreniz yanlış")
                        print("Önceki şifre temizleniyor".center(50,"*"))
                        time.sleep(2)
                        akullanıcıadı = input("Lütfen kullanıcı adını giriniz : ")
                        apassword = input("Şifrenizi giriniz : ")
                        continue
                    elif akullanıcıadı!=kullanıcıadı:
                        print("Kullanıcı adınız yanlış")
                        print("Önceki kullanıcı adınız temizleniyor".center(50,"/"))
                        time.sleep(2)
                        akullanıcıadı = input("Lütfen kullanıcı adını giriniz : ")
                        apassword = input("Şifrenizi giriniz : ")
        else:
            if password != password2:
                print("ŞİFRE YANLIŞ")
                kullanici_adi = input("Lütfen kullanıcı adını giriniz : ")
                password = input("Şifrenizi giriniz : ")
                password2 = input("Tekrardan Şifrenizi giriniz : ") 
            continue
