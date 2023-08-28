kullanici_adi = input("Lütfen kullanıcı adını giriniz : ")
password = input("Şifrenizi giriniz : ")
password2 = input("Tekrardan Şifrenizi giriniz : ")
while True:
        if password == password2:
            print("BAŞARIYLA KAYIT OLDUNUZ :D ")
            print("Kullanıcı adınız : ", kullanici_adi )
            print("Şifreniz : ",password)
            break
        else:
            if password != password2:
                print("ŞİFRE YANLIŞ")
                kullanici_adi = input("Lütfen kullanıcı adını giriniz : ")
                password = input("Şifrenizi giriniz : ")
                password2 = input("Tekrardan Şifrenizi giriniz : ") 
            continue