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
import json
import feedparser
import speech_recognition as sr

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dinliyorum...")
        audio = r.listen(source)


        a = r.recognize_google(audio, language='tr')
        print("Sesli Komut:", a)

        a = a.upper()
        if a == "ÇIKIŞ":
            print("Çıkış Yapılıyor...")
            break
        elif len(a) >= 40:
            yakupses = vlc.MediaPlayer("C:\Program Files (x86)\ChatBot\oo.mp3") #bu dosyayı bana fırlatsana ; bunu internette açalım + bu dosyayı online olarak yüklememiz gerek
            yakupses.play()
            time.sleep(5)
            yakupses.stop()
        if a == "HESAP MAKINESI" or a == "CALCULATOR" or a == "HESAPLA" or a == "HESAPLAYICI":
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
              print("İşlem Tipi: ")
              d = r.recognize_google(audio, language='tr')
              if d == "ÇIKIŞ":
                  print("Çıkış Yapılıyor...")
                  break

              elif d == "TOPLAMA" or d == "TOPLAM" or d == "1":
                  b = int(input("1. Sayı :"))
                  c = int(input("2. Sayı :"))
                  sonuc = b+c
                  print(sonuc)
                  if sonuc == 40:
                      g = vlc.MediaPlayer("C:\Program Files (x86)\ChatBot\devlet-bahceli-40-yapar_mp3cut.net.mp3")
                      g.play()
                      time.sleep(0.6)
                      g.stop()
                  elif b == 2 and c == 2:
                      print(5)
                      continue
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
              elif d == "ÇARPMA" or d == "ÇARPIM" or d == "3":
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
        elif a == "ÇEVIRI" or a == "TRANSLATE":
          while True:
              translator = Translator()
              
              ceviri = translator.translate(input("Çevrilicek Yazı: "),
                                            src='tr',
                                            dest='en')
              print(ceviri.text)
              cıkıs = input("Çıkış Yapmak İçin Çıkış yazınız: ").upper()
              if cıkıs == "ÇIKIŞ":
                  break
        elif a == "SELAM" or a == "MERHABA":
          liste = ['Merhaba', 'Selam', 'Sanada Merhaba', 'AS', 'Merhabalar', 'Hi', 'Hola']
          print(random.choice(liste))
        elif a == "NASILSIN":
          liste = ['İyiyim Sen Nasılsın', 'İyi Sen', 'Teşekkürler iyiyim sen nasılsın', 'Çok iyiyim', 'Mükemmelim']
          print(random.choice(liste))
        elif a == "RASTGELE SAYI":
          sayı = random.randint(int(input("en az: ")), int(input("en çok: ")))
          print(sayı)
        elif a == "DOLAR" or a == "USD" or a == "$":
              print("Veriler Çekiliyor")
              url = "https://www.google.com/finance/quote/USD-TRY?hl=tr"
              sayfa = requests.get(url)
              htmlsayfa = BeautifulSoup(sayfa.content, "html.parser")
              dolar = htmlsayfa.find("div", class_="YMlKec fxKbKc").getText()
              print("Anlık Dolar Kuru: ",dolar)
        elif a == "EURO" or a == "EUR" or a == "€":
          print("Veriler Çekiliyor")
          url = "https://www.google.com/finance/quote/EUR-TRY?hl=tr&comparison="
          sayfa = requests.get(url)
          htmlsayfa = BeautifulSoup(sayfa.content, "html.parser")
          dolar = htmlsayfa.find("div", class_="YMlKec fxKbKc").getText()
          print("Anlık Euro Kuru: ",dolar)
        elif a == "ATATÜRK KIMDIR" or a == "MUSTAFA KEMAL ATATÜRK KIMDIR" or a == "ATAM KIMDIR":
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
        elif a == "NERELISIN":
          print("Senin Var Diye Herkesin Vatandaşlığı Var Olacak Diye Bişey Yok :(")
        elif a == "BIR ŞAKA YAP" or a == "BENI GÜLDÜR":

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
            time.sleep(1)
            yakupses2 = vlc.MediaPlayer("C:\Program Files (x86)\ChatBot\\4324324.mp3")
            yakupses2.play()
            time.sleep(3)
            yakupses2.stop()
        if a == "DÜNYAYI YOK ET":
          #ses = vlc.MediaPlayer("C:/Users/Salim/Downloads/dunya.mp3")
          #ses.play()
          time.sleep(3)
          #ses.stop()
        if a == "RICKROLL" or a == "NEVER GONNA GIVE YOU UP":
          url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
          webbrowser.open(url)
        if a == "VIDEO 1 KAÇ IZLENDI":
          video_url = "https://www.youtube.com/watch?v=qaVHBZwyL3I&t=5s"
          yt = YouTube(video_url)
          print(yt.views ,"görüntülenme")
        if a == "VIDEO 2 KAÇ IZLENDI":
          video_url = "https://www.youtube.com/watch?v=tGpyLm-tsTE"
          yt = YouTube(video_url)
          print(yt.views ,"görüntülenme")
        if a == "VIDEO KAÇ IZLENDI" or a == "VIDEOM KAÇ IZLENDI" or a == "İZLENME BULUCU" or a == "İZLENME GÖRÜNTÜLE" or a == "İZLENME GÖRÜNTÜLEYİCİ":
          video_url = input("Video Link: ")
          yt = YouTube(video_url)
          print(yt.views ,"görüntülenme")
        if a == "KAMERAYI AÇ" or a == "KAMERAYI GÖRÜNTÜLE" or a == "KAMERA":
          print("""Zaten kameran hep açık, ben seni izliyorum!
              Ama senin görmen için açayım!""")
          time.sleep(2.5)
          pyautogui.hotkey('win', 'r')
          time.sleep(0.2)
          pyautogui.typewrite('microsoft.windows.camera:')
          pyautogui.press('enter')
        if a == "TERSE ÇEVIR" or a == "TERSE DÖNDÜR" or a == "TERSINE ÇEVIR" or a == "TERS ÇEVIR":
          tesine = input("Çevrilcek yazı: ")
          tn = str(tesine[::-1])
          print(tn)
        if a == "ŞIFRE OLUŞTUR" or a == "ŞIFRE OLUŞTURUCU" or a == "ŞIFRE YAP":
          karakterler = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'y', 'z',
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'Y', 'Z',
          '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', '\\', ';', ':', '<', '>', ',', '.', '/']

          uzunluk = int(input("Şifre Uzunluğu: "))
          sifre = ""

          for i in range(uzunluk):
              sifre += random.choice(karakterler)

          print("Oluşturulan Şifre: ", sifre)
        if a == "TEMP TEMIZLEME" or a == "GEREKSIZ DOSYALARI SIL":
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
        if a == "VIDEO INDIR" or a == "VIDEO INDIRICI" or a == "VIDEO DOWNLOAD":
          urele = input("İndirmek istediğiniz bağlantıyı giriniz\nLink: ")
          urle = urele[12:]

          url = f"ss{urle}"
          print(url)
          chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
          webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
          webbrowser.get('chrome').open_new_tab(url)
        if a == "ÜLKELER":
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
                  print("Coğrafyan bokum gibi kanka")
        if a == "HAVA DURUMU":
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
        if a == "CREDITS":
          link = "https://www.youtube.com/@molvess"
          link2 = "https://www.instagram.com/molvess0x/"
          link5 = "https://github.com/BArsxYT09"
          link3 = "https://www.youtube.com/channel/UCenRJZtUx7dXikmk9sLMN5w"
          link4 = "https://github.com/Tuna321"
          print("Molvess")
          print(f"Youtube; {link}")
          time.sleep(0.35)
          print(f"İnstagram; {link2}")
          time.sleep(0.35)
          print(f"GitHub; {link5}")
          time.sleep(0.35)
          print("Discord; molvess")

          time.sleep(1)
          print("°".center(70,"-"))
          time.sleep(0.15)
          print("Tuna")
          print(f"Youtube; {link3}")
          time.sleep(0.35)
          print(f"Github; {link4}")
          time.sleep(0.35)
          print("Discord; tuna9626")
          time.sleep(0.35)
        if a == "YOUTUBE":
          url = 'https://www.youtube.com'
          webbrowser.open(url)
        if a == "GITHUB" or a == "GIT HUB":
          url = 'https://github.com/'
          webbrowser.open(url)
        if a == "INSTAGRAM":
          url = 'https://www.instagram.com/'
          webbrowser.open(url)
        if a == "TWITTER":
          url = 'https://twitter.com/'
          webbrowser.open(url)
        if a == "PITEREST" or a == "PINT":
          url = 'https://pinterest.com/'
          webbrowser.open(url)
        if a == "TWITCH":
          url = 'https://www.twitch.tv/'
        if a == "GOOGLE":
          url = 'https://google.com/'
          webbrowser.open(url)
        if a == "HABERLER":
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
              
        if a == "":
          None
        if a == "":
          None
        if a == "":
          None
        if a == "":
          None
        if a == "YARDIM" or a == "HELP" or a == "KOMUTLAR" or a == "PROMTS" or a == "GIRDILER":
          url = 'https://justpaste.it/aqp0b'
          webbrowser.open(url)
        else:
          print("""Şimdilik Böyle Bir komutum Yok, Komutları Görmek İçin "Yardım" Yazınız""")# Devam eden kod blokları...


