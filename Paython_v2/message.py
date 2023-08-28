import time
import vlc
import random
from googletrans import Translator
from bs4 import BeautifulSoup
from pytube import YouTube
import requests
import pyautogui
import webbrowser
import tkinter


memleket = ""
yas = 0
sevilenyemek = ""
print("""Selam Ben ChatBot Size Nasıl Yardımcı olabilirim.""")
ısım = input("İsminiz :")
print("Anladım isminiz", ısım)
while True:
    a = input("Yanıtınız :")
    a = a.upper()

    if (a == "çıkış"):
        print("Çıkış Yapılıyor...")
        break
    elif len(a) >= 30:
        yakupses = vlc.MediaPlayer("ıoıo.mp3") #bu dosyayı bana fırlatsana ; bunu internette açalım + bu dosyayı online olarak yüklememiz gerek
        yakupses.play()
        time.sleep(5)
        yakupses.stop()
    elif a == "HESAP MAKINESI" or a == "CALCULATOR":
         while True:
            d = input("İşlem Tipi :").upper()
            if d == "ÇIKIŞ":
                print("Çıkış Yapılıyor...")
                break

            elif d == "TOPLAMA" or d == "TOPLAM":
                b = int(input("1. Sayı :"))
                c = int(input("2. Sayı :"))
                sonuc = b+c
                if sonuc == 40:
                    g = vlc.MediaPlayer("devlet-bahceli-40-yapar (mp3cut.net).mp3")
                    g.play()
                    time.sleep(0.6)
                    g.stop()
                elif b == 2 and c == 2:
                    print(5)
                    continue
                print(sonuc)
            elif d == "ÇIKARMA" or d == "ÇIKAR":
                b = int(input("1. Sayı :"))
                c = int(input("2. Sayı :"))
                sonuc = b-c
                print(sonuc)
                if sonuc == 40:
                    g = vlc.MediaPlayer("devlet-bahceli-40-yapar (mp3cut.net).mp3")
                    g.play()
                    time.sleep(0.6)
                    g.stop()
            elif d == "ÇARPMA" or d == "ÇARPIM":
                b = int(input("1. Sayı :"))
                c = int(input("2. Sayı :"))
                sonuc = b*c
                print(sonuc)
                if sonuc == 40:
                    g = vlc.MediaPlayer("devlet-bahceli-40-yapar (mp3cut.net).mp3")
                    g.play()
                    time.sleep(0.6)
                    g.stop()
            elif d == "BÖLME" or d == "BÖLÜM":
                b = int(input("1. Sayı :"))
                c = int(input("2. Sayı :"))
                sonuc = b / c
                print(sonuc)
                if sonuc == 40:
                    g = vlc.MediaPlayer("devlet-bahceli-40-yapar (mp3cut.net).mp3")
                    g.play()
                    time.sleep(0.6)
                    g.stop()
            else:
                print("4 İşlemden Bir İşlem Tipi Giriniz")
                print("1.Toplama")
                print("2.Çıkarma")
                print("3.Çarpma")
                print("4.Toplama")
    elif a == "GELIŞTIRICIN KIM":
        print("Geliştiricimi mi merak ediyorsun")
        time.sleep(0.8)
        print("Ama O Anlatılamayacak Kadar Mükemmel")
        time.sleep(2)
        print("1. özelliği: O Çoook Yakışıklı O Kadar Yakışıklı Ki Aynaya Bile Güneş Gözlüğü İle Bakıyor")
        time.sleep(4.5)
        print("2. Özelliği: O Ultra Mega Tega Sega Duble Triple Zeki O Kadar Zeki Ki Beni Kusursuz Bir Biçimde Yaptı")
        time.sleep(4.5)
        print("3. Özelliği: Onun IQ Seviyesi Ülkenin IQ seviyesi Olan 86.2'nin Çok Üstünde Hatta Yıllar Önce ÖLçürdüğümüzde 120-130 Arası Çıkmıştı")
        time.sleep(5.8)
        print("3 Maddede Geliştiricimi Anlattım Onun Adı 'Tuna' Ve O Çok Mükemmel")
    elif a == "YAKUP KIMDIR":
        print("ismi yakup")
        time.sleep(0.4)
        print("o derslerine çalışır")
        time.sleep(1)
        print("notları yüksedir")
        time.sleep(1.5)
        print("Zekidir")
        time.sleep(1.5)
        print("Bu Kadar")
    elif a == "ERDEM BINGOL KIMDIR":
        print("O Kimdi Ya???")
        time.sleep(0.8)
        print("Hee Bizim Malı Diyorsun")
        time.sleep(1)
        print("Hemen Anlatayım")
        time.sleep(1.5)
        print("1. özelliği: O Çoook Gerizekalı O Kadar Gerizekalı Ki Geliştiricim Beni Yaparken Bu Kod Beni Gömsün Dedi")
        time.sleep(4.5)
        print("2. Özelliği: O Geliştiricimin Arkadaşı Ama Geliştiricim Onunla Arkadaş Olduğuna Çok Pişman")
        time.sleep(4.5)
        print("3. Özelliği: Onun Ağazı Çok Bozuk Çünkü Geliştiricime Hakaret Ediyor")
        time.sleep(5.8)
        print("3 Maddede Edoyu Anlattım O Çok Salak")
    elif a == "ÇEVIRI":
        while True:
            translator = Translator()

            ceviri = translator.translate(input("Çevrilicek Yazı: "),
                                          src='tr',
                                          dest='en')
            print(ceviri.text)
            cıkıs = input("Çıkış Yapmak İçin Çıkış yazınız: ").upper()
            if cıkıs == "ÇIKIŞ":
                break
    elif a == "SELAM":
        liste = ['Merhaba', 'Selam', 'Sanada Merhaba', 'AS', 'Merhabalar', 'Hi', 'Hola']
        print(random.choice(liste))
    elif a == "NASILSIN":
        liste = ['İyiyim Sen Nasılsın', 'İyi Sen', 'Teşekkürler iyiyim sen nasılsın', 'Çok iyiyim', 'Mükemmelim']
        print(random.choice(liste))
    elif a == "RASTGELE SAYI":
        sayı = random.randint(int(input("en az: ")), int(input("en çok: ")))
        print(sayı)
    elif a == "DOLAR":
            url = "https://www.google.com/finance/quote/USD-TRY?hl=tr"
            sayfa = requests.get(url)
            htmlsayfa = BeautifulSoup(sayfa.content, "html.parser")
            dolar = htmlsayfa.find("div", class_="YMlKec fxKbKc").getText()
            print(dolar)
    elif a == "EURO":
        url = "https://www.google.com/finance/quote/EUR-TRY?hl=tr&comparison="
        sayfa = requests.get(url)
        htmlsayfa = BeautifulSoup(sayfa.content, "html.parser")
        dolar = htmlsayfa.find("div", class_="YMlKec fxKbKc").getText()
        print(dolar)
    elif a == "ATATÜRK KIMDIR":
        cumleler = [
            "Mustafa Kemal Atatürk, 1881 yılında Selanik'te doğdu.",
            "Babası Ali Rıza Efendi, annesi Zübeyde Hanım'dır.",
            "Babası görevleri arasında vakıflar kâtipliği ve gümrük memurluğu yapmıştır.",
            "Ailesi arasında eğitim konusunda görüş ayrılıkları yaşandı.",
            "Mustafa Kemal önce mahalle mektebine gitti, ardından Şemsi Efendi Okulu'na geçti.",
            "Babasının vefatı üzerine geçim sıkıntısı yaşayan ailesiyle birlikte Selanik yakınlarındaki bir çiftliğe taşındı.",
            "Adamın bviri gülmüş diğeri papatya.",
            "Ortaokulu tamamladıktan sonra İstanbul'daki Harp Okulu'na girdi ve askeri eğitim aldı.",
            "Askeri eğitimde matematik alanında yetenekli olduğu fark edildi ve adı 'Mustafa Kemal' olarak değiştirildi.",
            "Harp Okulu'nu başarıyla tamamladıktan sonra askerlik kariyerine devam etti."
        ]

        for cumle in cumleler:
            print(cumle)
            time.sleep(1.5)
    elif a == "BENIM ADIM NE":
        print("Sizin Adınınız", ısım)
    elif a == "NERELISIN":
        print("Senin Var Diye Herkesin Vatandaşlığı Var Olacak Diye Bişey Yok :(")
    elif a == "BIR ŞAKA YAP":
        liste = [ "Adamın biri gülmüş, saksıya koymuşlar.",
    "En iyi şarap hangi şaraptır? Çok şarap.",
    "Gece uyurken hangi renk pijama giyersin? Hangi renk olursa olsun, çünkü gece kimse seni göremez.",
    "Geçen gün taksi çevirdim, hala dönüyor.",
    "Bir gün dağlar sizi çağırırsa, gitmeyin. Çünkü dağlar çağırmaz, karşı gelir.",
    "Çok temizlik yapmayın, hırsızlar pis eve girmez.",
    "Birisi sizi havaya atarsa, ona havanı mı atarsın?",
    "Adamın biri güneşte yanmış, ay da düz.",
    "Sineklerin neden uçtuğunu biliyor musunuz? Kendi evlerinde hava durumu yok.",
    "Temel ile Dursun kayıkla gezerken düşmüş, kim düşer? Tabii ki Dursun, çünkü Temel düşmez."]
        print(random.choice(liste))
        time.sleep(1.5)
        #yakupses2 = vlc.MediaPlayer("4324324.mp3")
        #yakupses2.play()
        time.sleep(3)
        #yakupses2.stop()
    elif a == "KIŞISEL BILGI EKLE":
        print("Tamam Sorulara Yanıt Verirseniz Bilgilerinizi Kayıt Edeceğim")
        memleket = input("Memleketiniz :")
        yas = input("Yaşınız :")
        sevilenyemek = input("En Sevdiğiniz Yemek :")
    elif a == "KIŞISEL BILGILER":
        time.sleep(0.3)
        print("Sizin Adınız", ısım)
        time.sleep(1)
        print("Memleketiniz" , memleket)
        time.sleep(1)
        print("Yaşınız", yas)
        time.sleep(1)
        print("En Sevdiğiniz Yemek", sevilenyemek)
    elif a == "DÜNYAYI YOK ET":
        #ses = vlc.MediaPlayer("C:/Users/Salim/Downloads/dunya.mp3")
        #ses.play()
        time.sleep(3)
        #ses.stop()
    elif a == "RICKROLL":
        url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        webbrowser.open(url)
    elif a == "VIDEO 1 KAÇ IZLENDI":
        video_url = "https://www.youtube.com/watch?v=qaVHBZwyL3I&t=5s"
        yt = YouTube(video_url)
        print(yt.views ,"görüntülenme")
    elif a == "VIDEO 2 KAÇ IZLENDI":
        video_url = "https://www.youtube.com/watch?v=tGpyLm-tsTE"
        yt = YouTube(video_url)
        print(yt.views ,"görüntülenme")
    elif a == "KAMERAYI AÇ":
        print("""Zaten kameran hep açık, ben seni izliyorum!
            Ama senin görmen için açayım!""")
        time.sleep(2.5)
        pyautogui.hotkey('win', 'r')
        time.sleep(0.2)
        pyautogui.typewrite('microsoft.windows.camera:')
        pyautogui.press('enter')
    elif a == "TERSE ÇEVIR" or a == "TERSE DÖNDÜR" or a == "TERSINE ÇEVIR":
        tesine = input("Çevrilcek yazı: ")
        tn = str(tesine[::-1])
        print(tn)
    elif a == "ŞIFRE OLUŞTUR" or a == "ŞIFRE OLUŞTURUCU" or a == "ŞIFRE YAP":
        karakterler = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'Y', 'Z',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', '\\', ';', ':', '<', '>', ',', '.', '/']

        uzunluk = int(input("Şifre Uzunluğu: "))
        sifre = ""

        for i in range(uzunluk):
            sifre += random.choice(karakterler)

        print("Oluşturulan Şifre: ", sifre)
    elif a == "TEMP TEMIZLEME" or a == "GEREKSIZ DOSYALARI SIL":
        pyautogui.hotkey('win', 'r')
        time.sleep(0.7)
        pyautogui.typewrite('%temp%')
        time.sleep(0.7)
        pyautogui.press('enter')
        time.sleep(0.7)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.7)
        pyautogui.press('delete')
        time.sleep(0.7)
        pyautogui.press('enter')
        time.sleep(0.7)
        pyautogui.hotkey('alt', 'F4')
        time.sleep(1)
        
        pyautogui.hotkey('win', 'r')
        time.sleep(0.7)
        pyautogui.typewrite('Temp')
        time.sleep(0.7)
        pyautogui.press('enter')
        time.sleep(0.7)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.7)
        pyautogui.press('delete')
        time.sleep(0.7)
        pyautogui.press('enter')
        time.sleep(0.7)
        pyautogui.hotkey('alt', 'F4')
    elif a == "VIDEO INDIR":
        urele = input("İndirmek istediğiniz bağlantının https://www sız halini atınız \nÖrnek = 'https://www.youtube.com/watch?v=bU9a3eggcE0' \n")
        url = f"ss{urele}"
        print(url)
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url)
    elif a == "":
        None
    elif a == "":
        None
    elif a == "":
        None
    elif a == "":
        None
    elif a == "":
        None
    elif a == "YARDIM":
        print("""
Hesap makinesi: İki sayının toplamını, farkını, çarpımını veya bölümünü hesaplar.
2+2 girdisi verilirse sonuç 5 olacak ve sonuç 40 olursa devlet bahçelinin 40 yapar ses dosyasını oynatır

Geliştiricin kim: Geliştiricim hakkında troll bilgi verir.

Çeviri: Girilen bir metni Türkçeden İngilizceye çevirir.
Selam: Sizi selamlar.

Nasılsın: Nasıl olduğunuzu sorar.

Rastgele sayı: Belirtilen aralıkta rastgele bir sayı üretir.

Dolar: Güncel dolar kuru bilgisini verir.

Euro: Güncel euro kuru bilgisini verir.

Atatürk kimdir: Mustafa Kemal Atatürk hakkında bilgi verir.

Benim adım ne: Sizin adınızı söyler.

Nerelisin: Sizin memleketinizi söyler.

Bir şaka yap: Size rastgele bir şaka anlatır.

Kişisel bilgi ekle: Memleketiniz, yaşınız ve en sevdiğiniz yemek gibi kişisel bilgilerinizi kaydeder.

Kişisel bilgiler: Kaydedilen kişisel bilgilerinizi gösterir.

Dünyayı yok et: Şaka amaçlı "dünya yok edilmesi başlatılıyor" der.

Rickroll: Sizi Rick Astley'in "Never Gonna Give You Up" şarkısının klibine yönlendirir.

Video 1 kaç izlendi: Belirli bir YouTube videosunun kaç kez izlendiğini gösterir.

Video 2 kaç izlendi: Başka bir YouTube videosunun kaç kez izlendiğini gösterir.

Kamerayı aç: Bilgisayarınızda bulunan kamera uygulamasını sizi trolleyerek açar.""")
    else:
        print("Şimdilik Böyle Bir komutum Yok")
