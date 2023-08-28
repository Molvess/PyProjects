import time
import os

# kategoride ekleyebilirisn

sorular = [
    "Türkiye'nin başkenti neresidir?",
    "Dünyadaki en uzun nehir hangisidir?",
    "En büyük gezegen hangisidir?",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",

    # Soru listesini istediğiniz kadar uzatabilirsiniz
]


kullanici_adi = input("Lütfen kullanıcı adını giriniz : ")
password = input("Şifrenizi giriniz : ")
password2 = input("Tekrardan Şifrenizi giriniz : ")

while True:
    if password == password2:
        print("BAŞARIYLA KAYIT OLDUNUZ :D ")
        os.system('cls')
        kullanıcıadı = kullanici_adi
        password = password
        akullanıcıadı = input("KULLANICI ADI GİRİNİZ :")
        apassword = input("ŞİFRENİZİ GİRİNİZ :")
        while True:
            if apassword + password == akullanıcıadı + kullanıcıadı:
                time.sleep(1)
                print("Kullanıcı adınız : ", kullanıcıadı)
                print("Şifreniz : ", password)
                print("Hoşgeldiniz".center(70, "|"))
                time.sleep(2)
                os.system('cls')
                # BURDA BAŞLIYOR
                print(sorular[0])
                cvp = input("Cevap = ").upper()
                if cvp == "ANKARA":
                    print("Cevap doğru 🤍")
                    time.sleep(0.78)
                    os.system('cls')
                    print(sorular[1])
                    cvp = input("Cevap = ").upper()
                    if cvp == "NİL" or cvp == "NEHİR":
                        print("Cevap doğru 🤍")
                        time.sleep(0.78)
                        os.system('cls')
                        print(sorular[2])
                        cvp = input("Cevap = ").upper()
                        if cvp == "JÜPİTER":
                            print("Cevap doğru 🤍")
                            time.sleep(0.78)
                            os.system('cls')
                            print(sorular[3])
                            cvp = input("Cevap = ").upper()
                            if cvp == "NİL" or cvp == "NEHİR":
                                print("Cevap doğru 🤍")
                                time.sleep(0.78)
                                os.system('cls')
                                print(sorular[2])
                                cvp = input("Cevap = ").upper()




                            else:
                                exit()
                        else:
                            exit()
                    else:
                        exit()
                else:
                    exit()




                break
            elif apassword != password:
                print("Şifreniz yanlış")
                print("Önceki şifre temizleniyor".center(50, "*"))
                time.sleep(2)
                akullanıcıadı = input("Lütfen kullanıcı adını giriniz : ")
                apassword = input("Şifrenizi giriniz : ")
                continue
            elif akullanıcıadı != kullanıcıadı:
                print("Kullanıcı adınız yanlış")
                print("Önceki kullanıcı adınız temizleniyor".center(50, "/"))
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
