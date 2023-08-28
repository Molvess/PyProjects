import time

kullanıcıadı = "molvess"
password = str('123456')
akullanıcıadı = input("KULLANICI ADI GİRİNİZ :")
apassword = input("ŞİFRENİZİ GİRİNİZ :")

while True:
        if apassword+password == akullanıcıadı+kullanıcıadı:
            print("BAŞARIYLA Sisteme girdiniz")
            print("Kullanıcı adınız : ", kullanıcıadı )
            print("Şifreniz : ",password)
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
