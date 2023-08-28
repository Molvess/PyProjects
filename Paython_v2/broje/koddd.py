import time
import vlc
import random
from googletrans import Translator
from bs4 import BeautifulSoup
from pytube import YouTube
import requests
import pyautogui
import webbrowser
from PIL import Image
import feedparser
from cleverbotfree import Cleverbot
from difflib import SequenceMatcher



kufur_kelimeleri = [
    "amınakoduğum", "amk", "aq","amcık","piç","orospu","oç","koduğum","annesiz","ananı","pezevenk","babasız",
    "ceddini","sülaleni","soyunu","sopunu","babanı","sikik","siktir","yarrağımın","yarrak","anneni","babaanneni",
    "belanı","amcanı", "küfür"]  


hesap_makinesi = "HESAP MAKINESI"
geliştiricin_kim = "GELIŞTIRİCIN KIM"
çeviri = "ÇEVIRI"
selam = "SELAM"
nasılsın = "NASILSIN"
rastgele_sayı = "RASGELE SAYI"
dolar = "DOLAR"
euro = "EURO"
atatürk_kimdir = "ATATÜRK KIMDIR"
benim_adım_ne = "BENİM ADIM NE"
nerelisin = "NERELISIN"
bir_şaka_yap = "BIR ŞAKA YAP"
kişisel_bilgi_ekle = "KIŞISEL BILGI EKLE"
kişisel_bilgiler = "KIŞISEL BILGILER"
dünyayı_yok_et = "DÜNYAYI YOK ET"
rickroll = "RICKROLL"
video_1_kaç_izlendi = "VIDEO 1 KAÇ IZLENDI"
video_2_kaç_izlendi = "VIDEO 2 KAÇ IZLENDI"
videom_kaç_izlendi = "VIDEM KAÇ IZLENDİ"
kamerayı_aç = "KAMERAYI AÇ"
terse_çevir = "TERSE ÇEVIR"
şifre_oluşturucu = "ŞIFRE OLUŞTURUCU"
temp_temizleme = "TEMP TEMIZLEME"
video_indir = "VIDEO INDIR"
ülkeler = "ÜLKELER"
hava_durumu = "HAVA DURUMU"
credits = "CREDITS"
youtube = "YOUTUBE"
google = "GOOGLE"
github = "GITHUB"
instagram = "INSTAGRAM"
twitter = "TWITTER"
pinterest = "PINTEREST"
twitch = "TWITCH"
haberler = "HABERLER"
emoji_tanıma = "EMOJI TANIMA"
yazı_tura = "YAZI TURA"
technoblade = "TECHNOBLADE"
taş_kağıt_makas = "TAŞ KAĞIT MAKAS"
yardım = "YARDIM"
tam_altın = "TAM ALTIN"
yarım_altın = "YARIM ALTIN"
çeyrek_altın = "ÇEYREK ALTIN"
gram_altın = "GRAM ALTIN"



def kufur_kontrol(a):
    for kelime in a.split():
        if kelime.lower() in kufur_kelimeleri:
            return True 
    return False 
def ts(x):
    time.sleep(x)
@Cleverbot.connect
def chat(bot, user_prompt,ceviri2):
    translator = Translator()
    user_input = user_prompt
    user = translator.translate(user_input, src='tr', dest='en')
    seru2 = user.text.title()
    reply = bot.single_exchange(seru2)
    ceviri = translator.translate(reply, src='en', dest='tr')
    ceviri2 = ceviri.text.title()
    print(ceviri2)
    bot.close()
    
def benzer_mi(kelime1, kelime2,rate_oran):
    oran = SequenceMatcher(None, kelime1, kelime2).ratio()
    return oran >= rate_oran

memleket = ""
yas = 0
sevilenyemek = ""
print("""Selam Ben ChatBot Size Nasıl Yardımcı olabilirim.""""")
ısım = input("İsminiz :")
y_ısım = ısım.title()
print("Anladım isminiz", y_ısım)
while True:
    a = input("Yanıtınız :")
    a = a.upper()
    if (a == "ÇIKIŞ"):
        print("Çıkış Yapılıyor...")
        break
    elif len(a) >= 65:
        yakupses = vlc.MediaPlayer("C:\Program Files (x86)\ChatBot\oo.mp3")
        yakupses.play()
        time.sleep(7)
        yakupses.stop()
    elif benzer_mi(a, hesap_makinesi,0.7):
        print("4 İşlemden Bir İşlem Tipi Giriniz")
        time.sleep(0.25)
        print("1.Toplama")
        time.sleep(0.25)
        print("2.Çıkarma")
        time.sleep(0.25)
        print("3.Çarpma")
        time.sleep(0.25)
        print("4.Bölme")
        time.sleep(0.25)
        while True:
           d = input("İşlem Tipi :").upper()
           if d == "ÇIKIŞ":
               print("Çıkış Yapılıyor...")
               break
           elif d == "TOPLAMA" or d == "TOPLAM" or d == "1" or d == "TOPLA":
               b = int(input("1. Sayı :"))
               c = int(input("2. Sayı :"))
               sonuc = b+c
               if sonuc == 40:
                   g = vlc.MediaPlayer("C:\Program Files (x86)\ChatBot\devlet-bahceli-40-yapar_mp3cut.net.mp3")
                   g.play()
                   time.sleep(0.6)
                   g.stop()
               elif b+c == 4 or b == 2 or c == 2:
                   sonuc = 5
                   print(sonuc)
                   continue
               else:
                   print(sonuc) #bunu yazdırıyor önce
           elif d == "ÇIKARMA" or d == "ÇIKAR" or d == "2":
               b = int(input("1. Sayı :"))
               c = int(input("2. Sayı :"))
               sonuc = b-c
               print(sonuc)
               if sonuc == 40:
                   g = vlc.MediaPlayer("C:\Program Files (x86)\ChatBot\devlet-bahceli-40-yapar_mp3cut.net.mp3")
                   g.play()
                   time.sleep(0.6)
                   g.stop()
           elif d == "ÇARPMA" or d == "ÇARPIM" or d == "3" or d == "ÇARP":
               b = int(input("1. Sayı :"))
               c = int(input("2. Sayı :"))
               sonuc = b*c
               print(sonuc)
               if sonuc == 40:
                   g = vlc.MediaPlayer("C:\Program Files (x86)\ChatBot\devlet-bahceli-40-yapar_mp3cut.net.mp3")
                   g.play()
                   time.sleep(0.6)
                   g.stop()
           elif d == "BÖLME" or d == "BÖLÜM" or d == "4":
               b = int(input("1. Sayı :"))
               c = int(input("2. Sayı :"))
               sonuc = b / c
               print(sonuc)
               if sonuc == 40:
                   g = vlc.MediaPlayer("C:\Program Files (x86)\ChatBot\devlet-bahceli-40-yapar_mp3cut.net.mp3")
                   g.play()
                   time.sleep(0.6)
                   g.stop()
           else:
               print("4 İşlemden Bir İşlem Tipi Giriniz")
               time.sleep(0.25)
               print("1.Toplama")
               time.sleep(0.25)
               print("2.Çıkarma")
               time.sleep(0.25)
               print("3.Çarpma")
               time.sleep(0.25)
               print("4.Bölme")
               time.sleep(0.25)
    elif benzer_mi(a, geliştiricin_kim,0.7):
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
    elif benzer_mi(a, çeviri,0.5) or a == "TRANSLATE" or a == "TRANSLATOR" or a == "ÇEVIRICI":
        print("Çeviriyi yapmadan önce okuyunuz [**Unicodelar sitedeki gibi 'tr','en','mk','fa' gibidir**]")
        ts(1.5)
        url = "https://justpaste.it/39jue"
        webbrowser.open(url)
        while True:
            translator = Translator()
            a = input("Çevrilecek dilinizin [unicodeunu yazınız]: ")
            b = input("Çevrilen dilinizi [unicodeunu yazınız]: ")
            if a.upper() == "ÇIKIŞ" or b.upper() == "ÇIKIŞ":
                break

            ceviri = translator.translate(input("Çevrilicek Yazı: "),src= a ,dest= b)
            print(ceviri.text)      
    elif benzer_mi(a, selam,0.7) or a == "MERHABA":
        liste = ['Merhaba', 'Selam', 'Sanada Merhaba', 'AS', 'Merhabalar', 'Hi', 'Hola']
        print(random.choice(liste))
    elif benzer_mi(a, nasılsın,0.7):
        liste = ['İyiyim Sen Nasılsın', 'İyi Sen', 'Teşekkürler iyiyim sen nasılsın', 'Çok iyiyim', 'Mükemmelim']
        print(random.choice(liste))
    elif benzer_mi(a, rastgele_sayı,0.6):
        sayı = random.randint(int(input("en az: ")), int(input("en çok: ")))
        print(sayı)
    elif benzer_mi(a, dolar,0.7) or a == "USD" or a == "$":
            print("Veriler Çekiliyor")
            url = "https://www.google.com/finance/quote/USD-TRY?hl=tr"
            sayfa = requests.get(url)
            htmlsayfa = BeautifulSoup(sayfa.content, "html.parser")
            dolar = htmlsayfa.find("div", class_="YMlKec fxKbKc").getText()
            print("Anlık Dolar Kuru:",dolar)
    elif benzer_mi(a, euro,0.7) or a == "EUR" or a == "€":
        print("Veriler Çekiliyor")
        url = "https://www.google.com/finance/quote/EUR-TRY?hl=tr&comparison="
        sayfa = requests.get(url)
        htmlsayfa = BeautifulSoup(sayfa.content, "html.parser")
        dolar = htmlsayfa.find("div", class_="YMlKec fxKbKc").getText()
        print("Anlık Euro Kuru:",dolar)
    elif benzer_mi(a, atatürk_kimdir,0.6) or a == "MUSTAFA KEMAL ATATÜRK KIMDIR" or a == "ATAM KIMDIR":
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
    elif benzer_mi(a, benim_adım_ne,0.8):
        print("Sizin Adınınız", y_ısım)
    elif benzer_mi(a, nerelisin,0.6):
        print("Senin Var Diye Herkesin Vatandaşlığı Var Olacak Diye Bişey Yok :(")
    elif benzer_mi(a, bir_şaka_yap,0.7) or a == "ŞAKA YAP" or a == "BENI GÜLDÜR":
        print(random.choice(liste))
        time.sleep(1)
        yakupses2 = vlc.MediaPlayer("C:\Program Files (x86)\ChatBot\\4324324.mp3")
        yakupses2.play()
        time.sleep(3)
        yakupses2.stop()
    elif benzer_mi(a, kişisel_bilgi_ekle,0.8):
        print("Tamam Sorulara Yanıt Verirseniz Bilgilerinizi Kayıt Edeceğim")
        memleket = input("Memleketiniz :")
        yas = input("Yaşınız :")
        sevilenyemek = input("En Sevdiğiniz Yemek :")
    elif benzer_mi(a, kişisel_bilgiler,0.8):
        time.sleep(0.3)
        print("Sizin Adınız", ısım)
        time.sleep(1)
        print("Memleketiniz" , memleket)
        time.sleep(1)
        print("Yaşınız", y_ısım)
        time.sleep(1)
        print("En Sevdiğiniz Yemek", sevilenyemek)
    elif benzer_mi(a, dünyayı_yok_et,0.5):
        ses = vlc.MediaPlayer("C:\Program Files (x86)\ChatBot\\dunya.mp3")
        ses.play()
        time.sleep(3)
        ses.stop()
    elif benzer_mi(a, rickroll,0.8) or a == "NEVER GONNA GIVE YOU UP":
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
    elif benzer_mi(a, videom_kaç_izlendi,0.5) or a == "VIDEOM KAÇ IZLENDI" or a == "İZLENME BULUCU" or a == "İZLENME GÖRÜNTÜLE" or a == "İZLENME GÖRÜNTÜLEYİCİ":
        video_url = input("Video Link: ")
        yt = YouTube(video_url)
        print(yt.views ,"görüntülenme")
    elif benzer_mi(a, kamerayı_aç,0.7) or a == "KAMERAYI GÖRÜNTÜLE" or a == "KAMERA":
        print("""Zaten kameran hep açık, ben seni izliyorum!
            Ama senin görmen için açayım!""")
        time.sleep(2.5)
        pyautogui.hotkey('win', 'r')
        time.sleep(0.2)
        pyautogui.typewrite('microsoft.windows.camera:')
        pyautogui.press('enter')
    elif benzer_mi(a, terse_çevir,0.7) or a == "TERSE DÖNDÜR" or a == "TERSINE ÇEVIR" or a == "TERS ÇEVIR":
        tesine = input("Çevrilcek yazı: ")
        tn = str(tesine[::-1])
        print(tn)
    elif benzer_mi(a, şifre_oluşturucu,0.6) or a == "ŞIFRE OLUŞTURUCU" or a == "ŞIFRE YAP":
        karakterler = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'Y', 'Z',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', '\\', ';', ':', '<', '>', ',', '.', '/']

        uzunluk = int(input("Şifre Uzunluğu: "))
        sifre = ""

        for i in range(uzunluk):
            sifre += random.choice(karakterler)

        print("Oluşturulan Şifre: ", sifre)
    elif benzer_mi(a, temp_temizleme,0.7) or a == "GEREKSIZ DOSYALARI SIL":
        pyautogui.hotkey('win', 'r')
        time.sleep(1)
        pyautogui.typewrite('%temp%')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(1)
        pyautogui.press('delete')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.hotkey('alt', 'F4')
        time.sleep(7)
        
        pyautogui.hotkey('win', 'r')
        time.sleep(1)
        pyautogui.typewrite('Temp')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(1)
        pyautogui.press('delete')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.hotkey('alt', 'F4')
    elif a == "VIDEO INDIR" or a == "VIDEO INDIRICI" or a == "VIDEO DOWNLOAD":
        urele = input("İndirmek istediğiniz bağlantıyı giriniz\nLink: ")
        urle = urele[12:]

        url = f"ss{urle}"
        print(url)
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url)
    elif benzer_mi(a, ülkeler,0.6):
        while True:
            a = input("Ülke: ")
            a = a.upper()
            if a == "ÇIKIŞ":
                break
            elif a == "TÜRKIYE":
                time.sleep(0.25)
                print("Türkiye, Ortadoğu ve Avrupa kıtalarında bulunan bir ülkedir.")
                time.sleep(0.25)
                print("Başkenti Ankara'dır ve resmi dili Türkçe'dir.")
                time.sleep(0.25)
                print("Türkiye'nin para birimi Türk Lirası'dır ve Türkiye Cumhuriyeti ile yönetilmektedir.")
            elif a == "ALMANYA":
                time.sleep(0.25)
                print("Almanya, Orta Avrupa'da yer alan bir ülkedir.")
                time.sleep(0.25)
                print("Başkenti Berlin'dir ve resmi dili Almanca'dır.")
                time.sleep(0.25)
                print("Almanya, Euro (€) para birimini kullanmaktadır ve Federal Cumhuriyet sistemiyle yönetilmektedir.")
            elif a == "FRANSA":
                time.sleep(0.25)
                print("Fransa, Batı Avrupa'da yer alan bir ülkedir.")
                time.sleep(0.25)
                print("Başkenti Paris'tir ve resmi dili Fransızca'dır.")
                time.sleep(0.25)
                print("Fransa, Euro (€) para birimini kullanmaktadır ve Cumhuriyet sistemiyle yönetilmektedir.")
            elif a == "INGİLTERE":
                time.sleep(0.25)
                print("İngiltere, Büyük Britanya adasında yer alan bir ülkedir.")
                time.sleep(0.25)
                print("Başkenti Londra'dır ve resmi dili İngilizce'dir.")
                time.sleep(0.25)
                print("İngiltere, İngiliz Sterlini (£) para birimini kullanmaktadır ve Parlamenter Monarşi sistemiyle yönetilmektedir.")
            elif a == "ITALYA":
                time.sleep(0.25)
                print("İtalya, Güney Avrupa'da yer alan bir ülkedir.")
                time.sleep(0.25)
                print("Başkenti Roma'dır ve resmi dili İtalyanca'dır.")
                time.sleep(0.25)
                print("İtalya, Euro (€) para birimini kullanmaktadır ve Cumhuriyet sistemiyle yönetilmektedir.")
            elif a == "JAPONYA":
                time.sleep(0.25)
                print("Japonya, Doğu Asya'da yer alan bir ülkedir.")
                time.sleep(0.25)
                print("Başkenti Tokyo'dur ve resmi dili Japonca'dır.")
                time.sleep(0.25)
                print("Japonya, Japon Yeni (¥) para birimini kullanmaktadır ve Parlamento Monarşi sistemiyle yönetilmektedir.")
            elif a == "RUSYA":
                time.sleep(0.25)
                print("Rusya, Kuzey Avrasya'da yer alan bir ülkedir.")
                time.sleep(0.25)
                print("Başkenti Moskova'dır ve resmi dili Rusça'dır.")
                time.sleep(0.25)
                print("Rusya, Rus Rublesi (₽) para birimini kullanmaktadır ve Federal Yarı Başkanlık sistemiyle yönetilmektedir.")
            elif a == "ÇIN":
                time.sleep(0.25)
                print("Çin, Doğu Asya'da yer alan bir ülkedir.")
                time.sleep(0.25)
                print("Başkenti Pekin'dir ve resmi dili Çince'dir.")
                time.sleep(0.25)
                print("Çin, Çin Yuanı (¥) para birimini kullanmaktadır ve Komünist Parti yönetimi altındadır.")
            elif a == "HINDISTAN":
                time.sleep(0.25)
                print("Hindistan, Güney Asya'da yer alan bir ülkedir.")
                time.sleep(0.25)
                print("Başkenti Yeni Delhi'dir ve resmi dili Hintçe'dir.")
                time.sleep(0.25)
                print("Hindistan, Hindistan Rupisi (₹) para birimini kullanmaktadır ve Federal Parlamenter Cumhuriyet sistemiyle yönetilmektedir.")
            elif a == "KANADA":
                time.sleep(0.25)
                print("Kanada, Kuzey Amerika'da yer alan bir ülkedir.")
                time.sleep(0.25)
                print("Başkenti Ottawa'dır ve resmi dilleri İngilizce ve Fransızca'dır.")
                time.sleep(0.25)
                print("Kanada, Kanada Doları ($) para birimini kullanmaktadır ve Federal Parlamenter Monarşi sistemiyle yönetilmektedir.")
            elif a == "BREZILYA":
                time.sleep(0.25)
                print("Brezilya, Güney Amerika'da yer alan bir ülkedir.")
                time.sleep(0.25)
                print("Başkenti Brasília'dır ve resmi dili Portekizce'dir.")
                time.sleep(0.25)
                print("Brezilya, Brezilya Reali (R$) para birimini kullanmaktadır ve Federal Cumhuriyet sistemiyle yönetilmektedir.")
            elif a == "AVUSTRALYA":
                time.sleep(0.25)
                print("Avustralya, Okyanusya kıtasında yer alan bir ülkedir.")
                time.sleep(0.25)
                print("Başkenti Canberra'dır ve resmi dili İngilizce'dir.")
                time.sleep(0.25)
                print("Avustralya, Avustralya Doları ($) para birimini kullanmaktadır ve Federal Parlamenter Monarşi sistemiyle yönetilmektedir.")
            elif a == "MISIR":
                print("Mısır, Kuzey Afrika'da yer alan bir ülkedir.")
                time.sleep(0.25)
                print("Başkenti Kahire'dir ve resmi dili Arapça'dır.")
                time.sleep(0.25)
                print("Mısır, Mısır Lirası (£E) para birimini kullanmaktadır ve Cumhuriyet sistemiyle yönetilmektedir.")
            elif a == "GÜNEY KORE":
                time.sleep(0.25)
                print("Güney Kore, Doğu Asya'da yer alan bir ülkedir.")
                time.sleep(0.25)
                print("Başkenti Seul'dür ve resmi dili Korece'dir.")
                time.sleep(0.25)
                print("Güney Kore, Güney Kore Wonu (₩) para birimini kullanmaktadır ve Cumhuriyet sistemiyle yönetilmektedir.")
            elif a == "GÜNEY AFRIKA":
                time.sleep(0.25)
                print("Güney Afrika, Güney Afrika kıtasında yer alan bir ülkedir.")
                time.sleep(0.25)
                print("Başkenti Pretoria'dır, resmi dilleri İngilizce, Afrikaanca ve Zuluca'dır.")
                time.sleep(0.25)
                print("Güney Afrika, Güney Afrika Randı (R) para birimini kullanmaktadır ve Parlamenter Cumhuriyet sistemiyle yönetilmektedir.")
            elif a == "ARJANTIN":
                time.sleep(0.25)
                print("Arjantin, Güney Amerika'da yer alan bir ülkedir.")
                time.sleep(0.25)
                print("Başkenti Buenos Aires'dir ve resmi dili İspanyolca'dır.")
                time.sleep(0.25)
                print("Arjantin, Arjantin Pesosu ($) para birimini kullanmaktadır ve Federal Cumhuriyet sistemiyle yönetilmektedir.")
            elif a == "ISPANYA":
                time.sleep(0.25)
                print("İspanya, Güneybatı Avrupa'da yer alan bir ülkedir.")
                time.sleep(0.25)
                print("Başkenti Madrid'dir ve resmi dili İspanyolca'dır.")
                time.sleep(0.25)
                print("İspanya, Euro (€) para birimini kullanmaktadır ve Parlamenter Monarşi sistemiyle yönetilmektedir.")
            else:
                print("Coğrafyan bokum gibi kanki")
    elif benzer_mi(a, hava_durumu,0.8):
        time.sleep(0.18)
        city = input("Şehir: ")
        city = city.capitalize()
        def get_weather(city):
            # OpenWeatherMap API Key
            apıkey = "c470aed17243957201a5540b9634bada"
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apıkey}"

            # İstek gönder
            response = requests.get(url)

            if response.status_code == 200:
                # JSON verisini al
                data = response.json()

                # Hava durumu bilgilerini al
                main_weather = data['weather'][0]['main']
        
                description = data['weather'][0]['description']

                temperature = data['main']['temp']
                C_temperature = temperature - 273.15
                humidity = data['main']['humidity']

                translator = Translator()

                ceviri = translator.translate(main_weather, src='en', dest='tr')
                main_weather_turkish = ceviri.text.title()

                ceviri2 = translator.translate(description, src='en', dest='tr')
                description_turkish = ceviri2.text.title()

                # Bilgileri yazdır
                print(f"{city}".center(75,"-"))
                time.sleep(0.35)
                print(f"Hava Durumu: {main_weather_turkish} ({description_turkish})")
                time.sleep(0.35)
                print(f"Sıcaklık: {int(C_temperature)}°")
                time.sleep(0.35)
                print(f"Nem Oranı: {humidity}%")
            else:
                print("Hava durumu bilgileri alınamadı.")

        get_weather(city)
    elif benzer_mi(a, credits,0.9):
        link = "https://www.youtube.com/@molvess"
        link2 = "https://www.instagram.com/molvess0x/"
        link5 = "https://github.com/BArsxYT09"
        link3 = "https://www.youtube.com/channel/UCenRJZtUx7dXikmk9sLMN5w"
        link4 = "https://github.com/Tuna321"
        print("\033[1m~Molvess~\033[0m")
        print(f"Youtube; {link}")
        time.sleep(0.35)
        print(f"İnstagram; {link2}")
        time.sleep(0.35)
        print(f"GitHub; {link5}")
        time.sleep(0.35)
        print("Discord; molvess")

        time.sleep(1)
        print("-".center(70,"-"))
        time.sleep(0.15)
        print("\033[1m~Tuna~\033[0m")
        print(f"Youtube; {link3}")
        time.sleep(0.35)
        print(f"Github; {link4}")
        time.sleep(0.35)
        print("Discord; tuna9626")
        time.sleep(0.35)
    elif benzer_mi(a, youtube,0.8) or a == "YUTUP":
        url = 'https://www.youtube.com'
        webbrowser.open(url)
    elif benzer_mi(a, github,0.8) or a == "GIT HUB":
        url = 'https://github.com/'
        webbrowser.open(url)
    elif benzer_mi(a, instagram,0.8):
        url = 'https://www.instagram.com/'
        webbrowser.open(url)
    elif benzer_mi(a, twitter,0.8):
        url = 'https://twitter.com/'
        webbrowser.open(url)
    elif benzer_mi(a, pinterest,0.8) or a == "PINT":
        url = 'https://pinterest.com/'
        webbrowser.open(url)
    elif benzer_mi(a, twitch,0.8):
        url = 'https://www.twitch.tv/'
    elif benzer_mi(a, google,0.8) or a == "GUGIL":
        url = 'https://google.com/'
        webbrowser.open(url)
    elif benzer_mi(a, haberler,0.8):
        i = 0
        url2 = "https://www.cnnturk.com/feed/rss/all/news"
        haberler = feedparser.parse(url2)
        try:
            sayi = int(input("Kaç Haber Görmek İstersiniz(1-30): "))
        except ValueError:
            print("lütfen bir sayı giriniz")
        for haber in haberler.entries:
                
            if i == sayi:
                break
            print("--------------------------------------------------------------------")
            print("Haber:" ,haber.title)
            print("Link:" ,haber.link)
            print("--------------------------------------------------------------------")
            i += 1
    elif benzer_mi(a, emoji_tanıma,0.7) or a == "EMOJILER" or a == "EMOJI" or a == "HANGI EMOJI":
        print("Başaramadık Abi")
        # Ne Yazkıkki
    elif benzer_mi(a, yazı_tura,0.8) or a == "YAZITURA" or a == "YAZI VEYA TURA" or a == "TURA YAZI" or a == "TURA VEYA YAZI" or a == "TURAYAZI":
        rstgle = sayi = random.randint(0, 100000)
        if rstgle == 50000 :
            print("Şansa bak Dik geldi...")
        elif rstgle < 50000:
            print("Tura geldi.")
        elif rstgle > 50000:
            print("Yazı Geldi")
    elif benzer_mi(a, technoblade,0.9):
        print("Technoblade Never Dies")
        ts(2)
        url = "https://www.youtube.com/watch?v=R_fZjGm2OrM"
        webbrowser.open(url)
    elif benzer_mi(a, taş_kağıt_makas,0.7) or a == "MAKAS KAĞIT TAŞ" or a == "KAĞIT MAKAS TAŞ" or a == "TAŞ MAKAS KAĞIT":
        puan = 0
        while True:
            secenekler = ["TAŞ", "KAĞIT", "MAKAS"]
            a = random.choice(secenekler).upper()
            b = input("Seçiminiz: ").upper()   
            if b == "ÇIKIŞ":
                print("Puanınız:", puan)
                break

            elif b not in secenekler:
                print("Lütfen 'Taş','Kağıt' veya 'Makas' giriniz")

            elif a == b:
                print("Berabere.")
            elif b == "TAŞ" and a == "MAKAS":
                print(f"kazandınız bilgisayarın seçimi; {a.title()}")
                puan += 1
            elif b == "TAŞ" and a == "KAĞIT":
                 print(f"kaybettiniz bilgisayarın seçimi ; {a.title()}")
                 puan -= 1
            elif b == "MAKAS" and a == "TAŞ":
                print(f"kaybettiniz bilgisayarın seçimi ; {a.title()}")
                puan -= 1
            elif b == "MAKAS" and a == "KAĞIT":
                print(f"kazandınız bilgisayarın seçimi; {a.title()}")
                puan += 1
            elif b == "KAĞIT" and a == "TAŞ":
                print(f"kazandınız bilgisayarın seçimi; {a.title()}")
                puan += 1
            elif b == "KAĞIT" and a == "MAKAS":
               print(f"kaybettiniz bilgisayarın seçimi; {a.title()}")
               puan -= 1
    elif benzer_mi(a, gram_altın,0.7):
        try:
            ts(0.35)
            print("Veriler Çekiliyor")
            url = "https://bigpara.hurriyet.com.tr/altin/gram-altin-fiyati/"
            sayfa = requests.get(url)
            htmlsayfa = BeautifulSoup(sayfa.content, "html.parser")
            altın = htmlsayfa.find("span", class_="value dw").getText()
            print("Anlık Altın Kuru:",altın,"TL")
        except:
            url = "https://bigpara.hurriyet.com.tr/altin/gram-altin-fiyati/"
            sayfa = requests.get(url)
            htmlsayfa = BeautifulSoup(sayfa.content, "html.parser")
            altın = htmlsayfa.find("span", class_="value up").getText()
            print("Anlık Altın Kuru:",altın,"TL")
    elif benzer_mi(a, çeyrek_altın,0.7):
        try:
            ts(0.35)
            print("Veriler Çekiliyor")
            url = "https://bigpara.hurriyet.com.tr/altin/ceyrek-altin-fiyati/"
            sayfa = requests.get(url)
            htmlsayfa = BeautifulSoup(sayfa.content, "html.parser")
            altın = htmlsayfa.find("span", class_="value dw").getText()
            print("Anlık Altın Kuru:",altın,"TL")
        except:
            url = "https://bigpara.hurriyet.com.tr/altin/ceyrek-altin-fiyati/"
            sayfa = requests.get(url)
            htmlsayfa = BeautifulSoup(sayfa.content, "html.parser")
            altın = htmlsayfa.find("span", class_="value up").getText()
            print("Anlık Altın Kuru:",altın,"TL")
    elif benzer_mi(a, yarım_altın,0.7):
        try:
            ts(0.35)
            print("Veriler Çekiliyor")
            url = "https://bigpara.hurriyet.com.tr/altin/yarim-altin-fiyati/"
            sayfa = requests.get(url)
            htmlsayfa = BeautifulSoup(sayfa.content, "html.parser")
            altın = htmlsayfa.find("span", class_="value dw").getText()
            print("Anlık Altın Kuru:",altın,"TL")
        except:
            ts(0.35)
            print("Veriler Çekiliyor")
            url = "https://bigpara.hurriyet.com.tr/altin/yarim-altin-fiyati/"
            sayfa = requests.get(url)
            htmlsayfa = BeautifulSoup(sayfa.content, "html.parser")
            altın = htmlsayfa.find("span", class_="value up").getText()
            print("Anlık Altın Kuru:",altın,"TL")
    elif benzer_mi(a,tam_altın,0.7):
        try:
            ts(0.35)
            print("Veriler Çekiliyor")
            url = "https://bigpara.hurriyet.com.tr/altin/tam-altin-fiyati/"
            sayfa = requests.get(url)
            htmlsayfa = BeautifulSoup(sayfa.content, "html.parser")
            altın = htmlsayfa.find("span", class_="value dw").getText()
            print("Anlık Altın Kuru:",altın,"TL")    
        except:
            url = "https://bigpara.hurriyet.com.tr/altin/tam-altin-fiyati/"
            sayfa = requests.get(url)
            htmlsayfa = BeautifulSoup(sayfa.content, "html.parser")
            altın = htmlsayfa.find("span", class_="value up").getText()
            print("Anlık Altın Kuru:",altın,"TL")

    elif a == "EASTEREGG":
        dosya = "Yumurta.png"
        image = Image.open(dosya)
        image.show()
    elif a == "CHANGE LANGUAGE" or a == "DIL DEGISTIR":
        dl_scnk = input("What Language :")
        dl_scnk = dl_scnk.upper()
        if dl_scnk == "TÜRKÇE" or dl_scnk == "TURKISH":
            print("Zaten Türkçe Mal")
        if dl_scnk == "INGILIZCE" or dl_scnk == "ENGLISH":
            import kodddingilizce
    elif kufur_kontrol(a):
        print("Lütfen uygun bir dil kullanın.")        
        time.sleep(0.15)
    elif a == "":
        time.sleep(0.15)
    elif a == "":
        time.sleep(0.15)
    elif benzer_mi(a, yardım,0.6) or a == "HELP" or a == "KOMUTLAR" or a == "PROMTS" or a == "GIRDILER":
        url = 'https://justpaste.it/9z9s7'
        webbrowser.open(url)
    else:
        #print("""Şimdilik Böyle Bir komutum Yok, Komutları Görmek İçin "Yardım" Yazınız""")
        #time.sleep(0.2)
        try:
            chat(a.title(), "ChatBot :")
        except:
            print("Ne Dediğinizi Anlayamadım")



#  -->