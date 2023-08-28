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
from cleverbotfree import Cleverbot
from difflib import SequenceMatcher


#dosya = "resim.png"
#image = Image.open(dosya)
#image.show()

kufur_kelimeleri = [
    "amen", "wtf", "aq","cunt","bastard","bitch","och","fuck","motherless","your mother","pimp","fatherless",
    "ceddini","sülaleni","soyunu","sopunu","babanı","sikik","siktir","yarrağımın","yarrak","anneni","babaanneni",
    "your trouble,"""]

def kufur_kontrol(a):
    for kelime in a.split():
        if kelime.lower() in kufur_kelimeleri:
            return True 
    return False  

def ts(x):
    time.sleep(x)

@Cleverbot.connect
def chat(bot, user_prompt,bot_prompt):
    user_input = user_prompt
    user_input = user_input.upper()
    reply = bot.single_exchange(user_input)
    print(reply)
    bot.close()

memleket = ""
yas = 0
sevilenyemek = ""
print("""Hello I Am ChatBot How Can Help You""""")
ısım = input("Your Name :")
y_ısım = ısım.title()
print("I get your name is", y_ısım)
while True:
    a = input("Your Answer :")
    a = a.upper()
    if (a == "EXIT"):
        print("Logging Out...")
        break
    elif len(a) >= 40:
        yakupses = vlc.MediaPlayer("C:\Program Files (x86)\ChatBot\oo.mp3") #bu dosyayı bana fırlatsana ; bunu internette açalım + bu dosyayı online olarak yüklememiz gerek
        yakupses.play()
        time.sleep(5)
        yakupses.stop()
    elif a == "HESAP MAKINESI" or a == "CALCULATOR" or a == "CALCULATE" or a == "HESAPLAYICI":
         print("Enter a Transaction Type from 4 Transactions")  
         time.sleep(0.25)
         print("1.Addition")
         time.sleep(0.25)
         print("2.Subtraction")
         time.sleep(0.25)
         print("3.Multiplication")
         time.sleep(0.25)
         print("4.Division")
         time.sleep(0.25)
         while True:
            d = input("Process type :").upper()
            if d == "EXIT":
                print("Checking Out...")
                break

            elif d == "ADDONTION" or d == "ADD" or d == "1":
                b = int(input("First Number :"))
                c = int(input("Second Number :"))
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
            elif d == "SUBTRACTION" or d == "ÇIKAR" or d == "2":
                b = int(input("First Number :"))
                c = int(input("Second Number :"))
                sonuc = b-c
                print(sonuc)
                if sonuc == 40:
                    g = vlc.MediaPlayer("C:\Program Files (x86)\ChatBot\devlet-bahceli-40-yapar_mp3cut.net.mp3")
                    g.play()
                    time.sleep(0.6)
                    g.stop()
            elif d == "Multiplication".upper() or d == "ÇARPIM" or d == "3":
                b = int(input("First Number :"))
                c = int(input("Second Number :"))
                sonuc = b*c
                print(sonuc)
                if sonuc == 40:
                    g = vlc.MediaPlayer("C:\Program Files (x86)\ChatBot\devlet-bahceli-40-yapar_mp3cut.net.mp3")
                    g.play()
                    time.sleep(0.6)
                    g.stop()
            elif d == "Division".upper() or d == "BÖLÜM" or d == "4":
                b = int(input("First Number :"))
                c = int(input("Second Number :"))
                sonuc = b / c
                print(sonuc)
                if sonuc == 40:
                    g = vlc.MediaPlayer("C:\Program Files (x86)\ChatBot\devlet-bahceli-40-yapar_mp3cut.net.mp3")
                    g.play()
                    time.sleep(0.6)
                    g.stop()
            else:
                print("Enter a Transaction Type from 4 Transactions")
                time.sleep(0.25)
                print("1.Addition")
                time.sleep(0.25)
                print("2.Subtraction")
                time.sleep(0.25)
                print("3.Multiplication")
                time.sleep(0.25)
                print("4.Division")
                time.sleep(0.25)
    elif a == "WHO IS YOUR DEVELOPER":
        print("Curious about my developer?")
        time.sleep(0.8)
        print("But She's Unspeakably Perfect")
        time.sleep(2)
        print("1. Feature: He's So Handsome He's So Handsome He Even Looks In The Mirror With Sunglasses")
        time.sleep(4.5)
        print("2. Feature : He's Ultra Mega Mega Mega Double Triple Clever So Clever He Made Me Perfectly")
        time.sleep(4.5)
        print("3. Feature: His IQ Level Is Well Above The Country's IQ Level Of 86.2. It Was Between 120-130 When We Measured It Years Ago")
        time.sleep(5.8)
        print("I Told My Developer In 3 Items His Name Is 'Tuna' And He Is So Perfect")
    elif a == "WHO IS YAKUP":
        print("His name is Yakup")
        time.sleep(0.4)
        print("He studies his lessons")
        time.sleep(1)
        print("High grades")
        time.sleep(1.5)
        print("Is clever")
        time.sleep(1.5)
        print("This much")
    elif a == "WHO IS ERDEM BINGOL":
        print("Who Was He???")
        time.sleep(0.8)
        print("Hee You Say It's Our İdiot")
        time.sleep(1)
        print("Let me tell you now")
        time.sleep(1.5)
        print("1. Feature: He's So Stupid He's So Stupid My Developer Said To Bury Me While He Was Making Me")
        time.sleep(4.5)
        print("2. Feature : He's A Friend of the Developer But The Developer Regrets Being Friends With Him")
        time.sleep(4.5)
        print("3. Feature : His Mouth Is So Bad Because He Insults The Developer")
        time.sleep(5.8)
        print("I Explained Edo in 3 Items It's So Dumb")
    elif a == "ÇEVIRI" or a == "TRANSLATE" or a == "TRANSLATOR" or a == "ÇEVIRICI":
        print("Please read before translating [**Unicodes are like 'tr','en','mk','fa' as on the site**]")
        ts(1.5)
        url = "https://justpaste.it/39jue"
        webbrowser.open(url)
        while True:
            translator = Translator()
            a = input("Your language to be translated [Insert unicode]:")
            b = input("Your translated language [insert uni code]:")
            if a.upper() == "EXIT" or b.upper() == "EXIT":
                break

            ceviri = translator.translate(input("Text to be translated: "),src= a ,dest= b)
            print(ceviri.text)
            
    elif a == "Hi" or a == "HELLO":
        liste = ['Hello', 'Hello', 'Hello to you', 'Hello', 'Hi', 'Hola']
        print(random.choice(liste))
    elif a == "NASILSIN":
        liste = ['Im fine How are you', 'Im fine', 'Im fine how are you', 'Im fine', 'Im perfect']
        print(random.choice(liste))
    elif a == "RANDOM NUMBER":
        sayı = random.randint(int(input("en az: ")), int(input("en çok: ")))
        print(sayı)
    elif a == "DOLLAR" or a == "USD" or a == "$":
            print("Data is being retrieved")
            url = "https://www.google.com/finance/quote/USD-TRY?hl=tr"
            sayfa = requests.get(url)
            htmlsayfa = BeautifulSoup(sayfa.content, "html.parser")
            dolar = htmlsayfa.find("div", class_="YMlKec fxKbKc").getText()
            print("Instant Dollar Rate: ",dolar)
    elif a == "EURO" or a == "EUR" or a == "€":
        print("Data is being retrieved")
        url = "https://www.google.com/finance/quote/EUR-TRY?hl=tr&comparison="
        sayfa = requests.get(url)
        htmlsayfa = BeautifulSoup(sayfa.content, "html.parser")
        dolar = htmlsayfa.find("div", class_="YMlKec fxKbKc").getText()
        print("Instant Euro Rate: ",dolar)
    elif a == "WHO IS ATATURK" or a == "WHO IS MUSTAFA KEMAL ATATURK" or a == "WHO IS ATAM":
        cumleler = [
        "Mustafa Kemal Atatürk was born in Selanik in 1881.",
        "His father is Ali Rıza Efendi and his m:)other is Zübeyde Hanım.",
        "His father served as a clerk in the foundations and worked as a customs officer.",
        "There were differences of opinion within the family regarding education.",
        "Mustafa Kemal first attended the neighborhood school, then transferred to Şemsi Efendi School.",
        "After his father's death, his family, facing financial difficulties, moved to a farm near Thessaloniki.",
        "One of the men laughed, the other picked a daisy.",
        "After completing middle school, he entered the Military Academy in Istanbul and received military training.",
        "He was recognized for his talent in mathematics during his military training, and his name was changed to 'Mustafa Kemal'.",
        "After successfully completing the Military Academy, he continued his military career."
        ]

        for cumle in cumleler:
            print(cumle)
            time.sleep(1.5)
    elif a == "WHAT IS MY NAME":
        print("Sizin Adınınız", y_ısım)
    elif a == "WHERE ARE YOU FROM":
        print("There is no such thing that everyone will have citizenship because you have :(")
    elif a == "MAKE A JOKE" or a == "MAKE ME LAUGH":
        print(random.choice(liste))
        time.sleep(1)
        yakupses2 = vlc.MediaPlayer("C:\Program Files (x86)\ChatBot\\4324324.mp3")
        yakupses2.play()
        time.sleep(3)
        yakupses2.stop()
    elif a == "ADD PERSONAL INFORMATION":
        print("OK If You Answer The Questions, I Will Record Your Information")
        memleket = input("Your hometown:")
        yas = input("Your Age:")
        sevilenyemek = input("Favorite Food :")
    elif a == "PERSONAL INFORMATION":
        time.sleep(0.3)
        print("Your name", ısım)
        time.sleep(1)
        print("Your Hometown" , memleket)
        time.sleep(1)
        print("Your Age İs", y_ısım)
        time.sleep(1)
        print("Your Favorite Food", sevilenyemek)
    elif a == "DESTROY EARTH":
        ses = vlc.MediaPlayer("C:\Program Files (x86)\ChatBot\\dunya.mp3")
        ses.play()
        time.sleep(3)
        ses.stop()
    elif a == "RICKROLL" or a == "NEVER GONNA GIVE YOU UP":
        url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        webbrowser.open(url)
    elif a == "VIDEO 1 WATCHED":
        video_url = "https://www.youtube.com/watch?v=qaVHBZwyL3I&t=5s"
        yt = YouTube(video_url)
        print(yt.views ,"Wiews")
    elif a == "VIDEO 2 WATCHED":
        video_url = "https://www.youtube.com/watch?v=tGpyLm-tsTE"
        yt = YouTube(video_url)
        print(yt.views ,"Wiews")
    elif a == "HOW MANY VIDEO WATCHED" or a == "HOW MANY VIDEOS WATCHED" or a == "TRACK FINDER" or a == "VIEW WATCH" or a == "VIEW VIEWER":
        video_url = input("Video Link: ")
        yt = YouTube(video_url)
        print(yt.views ,"Wiews")
    elif a == "OPEN CAMERA" or a == "SEE CAMERA" or a == "CAMERA":
        print("""The camera is already on, I'm watching you!
            But let me turn it on for you to see!""")
        time.sleep(2.5)
        pyautogui.hotkey('win', 'r')
        time.sleep(0.2)
        pyautogui.typewrite('microsoft.windows.camera:')
        pyautogui.press('enter')
    elif a == "INVERSION" or a == "REVERSE":
        tesine = input("Text to be translated:")
        tn = str(tesine[::-1])
        print(tn)
    elif a == "CREATE PASSWORD"or a == "PASSWORD CREATOR":
        karakterler = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'Y', 'Z',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', '\\', ';', ':', '<', '>', ',', '.', '/']

        uzunluk = int(input("Password length: "))
        sifre = ""

        for i in range(uzunluk):
            sifre += random.choice(karakterler)

        print("Generated Password: ", sifre)
    elif a == "TEMP CLEANING" or a == "DELETE ESSENTIAL FILES":
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
    elif a == "DOWNLOAD VIDEO" or a == "VIDEO DOWNLOAD" or a == "VIDEO DOWNLOAD":
        urele = input("Enter the link you want to download\nLink:")
        urle = urele[12:]

        url = f"ss{urle}"
        print(url)
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab(url)
    elif a == "COUNTRIES":
        while True:
            a = input("Country: ")
            a = a.upper()
            if a == "EXIT":
                break
            elif a == "TURKEY":
                time.sleep(0.25)
                print("Turkey is a country located in the Middle East and Europe.")
                time.sleep(0.25)
                print("Its capital is Ankara, and the official language is Turkish.")
                time.sleep(0.25)
                print("Turkey uses the currency Turkish Lira and is governed by the Republic of Turkey.")
            elif a == "GERMANY":
                time.sleep(0.25)
                print("Germany is a country located in Central Europe.")
                time.sleep(0.25)
                print("Its capital is Berlin, and the official language is German.")
                time.sleep(0.25)
                print("Germany uses the currency Euro (€) and is governed by the Federal Republic system.")
            elif a == "FRANCE":
                time.sleep(0.25)
                print("France is a country located in Western Europe.")
                time.sleep(0.25)
                print("Its capital is Paris, and the official language is French.")
                time.sleep(0.25)
                print("France uses the currency Euro (€) and is governed by the Republic system.")
            elif a == "UNITED KINGDOM":
                time.sleep(0.25)
                print("The United Kingdom is a country located on the British Isles.")
                time.sleep(0.25)
                print("Its capital is London, and the official language is English.")
                time.sleep(0.25)
                print("The United Kingdom uses the currency British Pound (£) and is governed by the Parliamentary Monarchy system.")
            elif a == "ITALY":
                time.sleep(0.25)
                print("Italy is a country located in Southern Europe.")
                time.sleep(0.25)
                print("Its capital is Rome, and the official language is Italian.")
                time.sleep(0.25)
                print("Italy uses the currency Euro (€) and is governed by the Republic system.")
            elif a == "JAPAN":
                time.sleep(0.25)
                print("Japan is a country located in East Asia.")
                time.sleep(0.25)
                print("Its capital is Tokyo, and the official language is Japanese.")
                time.sleep(0.25)
                print("Japan uses the currency Japanese Yen (¥) and is governed by the Parliamentary Monarchy system.")
            elif a == "RUSSIA":
                time.sleep(0.25)
                print("Russia is a country located in Northern Eurasia.")
                time.sleep(0.25)
                print("Its capital is Moscow, and the official language is Russian.")
                time.sleep(0.25)
                print("Russia uses the currency Russian Ruble (₽) and is governed by the Federal Semi-Presidential system.")
            elif a == "CHINA":
                time.sleep(0.25)
                print("China is a country located in East Asia.")
                time.sleep(0.25)
                print("Its capital is Beijing, and the official language is Chinese.")
                time.sleep(0.25)
                print("China uses the currency Chinese Yuan (¥) and is under the governance of the Communist Party.")
            elif a == "INDIA":
                time.sleep(0.25)
                print("India is a country located in South Asia.")
                time.sleep(0.25)
                print("Its capital is New Delhi, and the official language is Hindi.")
                time.sleep(0.25)
                print("India uses the currency Indian Rupee (₹) and is governed by the Federal Parliamentary Republic system.")
            elif a == "CANADA":
                time.sleep(0.25)
                print("Canada is a country located in North America.")
                time.sleep(0.25)
                print("Its capital is Ottawa, and the official languages are English and French.")
                time.sleep(0.25)
                print("Canada uses the currency Canadian Dollar ($) and is governed by the Federal Parliamentary Monarchy system.")
            elif a == "BRAZIL":
                time.sleep(0.25)
                print("Brazil is a country located in South America.")
                time.sleep(0.25)
                print("Its capital is Brasília, and the official language is Portuguese.")
                time.sleep(0.25)
                print("Brazil uses the currency Brazilian Real (R$) and is governed by the Federal Republic system.")
            elif a == "AUSTRALIA":
                time.sleep(0.25)
                print("Australia is a country located in Oceania.")
                time.sleep(0.25)
                print("Its capital is Canberra, and the official language is English.")
                time.sleep(0.25)
                print("Australia uses the currency Australian Dollar ($) and is governed by the Federal Parliamentary Monarchy system.")
            elif a == "EGYPT":
                print("Egypt is a country located in North Africa.")
                time.sleep(0.25)
                print("Its capital is Cairo, and the official language is Arabic.")
                time.sleep(0.25)
                print("Egypt uses the currency Egyptian Pound (£E) and is governed by the Republic system.")
            elif a == "SOUTH KOREA":
                time.sleep(0.25)
                print("South Korea is a country located in East Asia.")
                time.sleep(0.25)
                print("Its capital is Seoul, and the official language is Korean.")
                time.sleep(0.25)
                print("South Korea uses the currency South Korean Won (₩) and is governed by the Republic system.")
            elif a == "SOUTH AFRICA":
                time.sleep(0.25)
                print("South Africa is a country located in the southernmost part of the African continent.")
                time.sleep(0.25)
                print("Its capital is Pretoria, and the official languages are English, Afrikaans, and Zulu.")
                time.sleep(0.25)
                print("South Africa uses the currency South African Rand (R) and is governed by the Parliamentary Republic system.")
            elif a == "ARGENTINA":
                time.sleep(0.25)
                print("Argentina is a country located in South America.")
                time.sleep(0.25)
                print("Its capital is Buenos Aires, and the official language is Spanish.")
                time.sleep(0.25)
                print("Argentina uses the currency Argentine Peso ($) and is governed by the Federal Republic system.")
            elif a == "SPAIN":
                time.sleep(0.25)
                print("Spain is a country located in Southwest Europe.")
                time.sleep(0.25)
                print("Its capital is Madrid, and the official language is Spanish.")
                time.sleep(0.25)
                print("Spain uses the currency Euro (€) and is governed by the Parliamentary Monarchy system.")
            else:
                print("Your geography is not great, mate.")

    elif a == "WEATHER":
        time.sleep(0.18)
        city = input("City: ")
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

                # Bilgileri yazdır
                print(f"{city}".center(75,"-"))
                time.sleep(0.35)
                print(f"Weather: {main_weather} ({description})")
                time.sleep(0.35)
                print(f"Temperature {int(C_temperature)}°")
                time.sleep(0.35)
                print(f"Humidity: {humidity}%")
            else:
                print("Weather information could not be retrieved.")

        get_weather(city)
    elif a == "CREDITS":
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
    elif a == "YOUTUBE":
        url = 'https://www.youtube.com'
        webbrowser.open(url)
    elif a == "GITHUB" or a == "GIT HUB":
        url = 'https://github.com/'
        webbrowser.open(url)
    elif a == "INSTAGRAM":
        url = 'https://www.instagram.com/'
        webbrowser.open(url)
    elif a == "TWITTER":
        url = 'https://twitter.com/'
        webbrowser.open(url)
    elif a == "PINTEREST" or a == "PINT":
        url = 'https://pinterest.com/'
        webbrowser.open(url)
    elif a == "TWITCH":
        url = 'https://www.twitch.tv/'
    elif a == "GOOGLE":
        url = 'https://google.com/'
        webbrowser.open(url)
    elif a == "NEWS":
        i = 0
        url2 = "http://rss.cnn.com/rss/edition.rss"
        haberler = feedparser.parse(url2)
        try:
            sayi = int(input("How Many News Would You Like To See (1-30):"))
        except ValueError:
            print("Please enter a number")
        for haber in haberler.entries:
                
            if i == sayi:
                break
            print("--------------------------------------------------------------------")
            print("News:" ,haber.title)
            print("Link:" ,haber.link)
            print("--------------------------------------------------------------------")
            i += 1
    elif a == "EMOJI RECOGNITION" or a == "EMOJIS" or a == "EMOJI" or a == "WHICH EMOJI":
        print("Başaramadık Abi")
        # Ne Yazkıkki
    elif a == "HEADS OR TAILS" or a == "PİTCH AND TOSS" or a == "TOSS UP" or a == "COİN TOSS":
         rstgle = sayi = random.randint(0, 100000)
         if rstgle == 50000 :
             print("Damn Luckily, came upright...")
         elif rstgle < 50000:
             print("Its came on heads.")
         elif rstgle > 50000:
             print("Its came on tails.")
    elif a == "TECHNOBLADE":
        print("Technoblade Never Dies")
        ts(2)
        url = "https://www.youtube.com/watch?v=R_fZjGm2OrM"
        webbrowser.open(url)
    elif a == "ROCK PAPER SCISSORS" or a == "SCISSORS PAPER ROCK" or a == "KAĞIT SCISSORS TAŞ" or a == "ROCK SCISSORS PAPER":
        puan = 0
        while True:
            secenekler = ["ROCK", "PAPER", "SCİSSORS"]
            a = random.choice(secenekler).upper()
            b = input("Seçiminiz: ").upper()   
            if b == "ÇIKIŞ":
                print("Puanınız:", puan)
                break

            elif b not in secenekler:
                print("Please enter 'Stone', 'Paper' or 'Scissors'")

            elif a == b:
                print("Draw...")
            elif b == "ROCK" and a == "SCISSORS":
                print(f"kazandınız bilgisayarın seçimi; {a.title()}")
                puan += 1
            elif b == "ROCK" and a == "PAPER":
                 print(f"kaybettiniz bilgisayarın seçimi ; {a.title()}")
                 puan -= 1
            elif b == "SCISSORS" and a == "ROCK":
                print(f"kaybettiniz bilgisayarın seçimi ; {a.title()}")
                puan -= 1
            elif b == "SCISSORS" and a == "PAPER":
                print(f"kazandınız bilgisayarın seçimi; {a.title()}")
                puan += 1
            elif b == "PAPER" and a == "ROCK":
                print(f"kazandınız bilgisayarın seçimi; {a.title()}")
                puan += 1
            elif b == "PAPER" and a == "SCISSORS":
               print(f"kaybettiniz bilgisayarın seçimi; {a.title()}")
               puan -= 1
    elif a == "GRAM GOLD":
        ts(0.35)
        print("Data is being retrieved")
        url = "https://bigpara.hurriyet.com.tr/altin/gram-altin-fiyati/"
        sayfa = requests.get(url)
        htmlsayfa = BeautifulSoup(sayfa.content, "html.parser")
        altın = htmlsayfa.find("span", class_="value dw").getText()
        print("Instant Gram Gold Rate:",altın,"TL")
    elif a == "QUARTER GOLD":
        ts(0.35)
        print("Data is being retrieved")
        url = "https://bigpara.hurriyet.com.tr/altin/ceyrek-altin-fiyati/"
        sayfa = requests.get(url)
        htmlsayfa = BeautifulSoup(sayfa.content, "html.parser")
        altın = htmlsayfa.find("span", class_="value dw").getText()
        print("Instant Quarter Gold Rate:",altın,"TL")
    elif a == "HALF GOLD":
        ts(0.35)
        print("Data is being retrieved")
        url = "https://bigpara.hurriyet.com.tr/altin/yarim-altin-fiyati/"
        sayfa = requests.get(url)
        htmlsayfa = BeautifulSoup(sayfa.content, "html.parser")
        altın = htmlsayfa.find("span", class_="value dw").getText()
        print("Instant Half Gold Rate:",altın,"TL")
    elif a == "FULL GOLD":
        ts(0.35)
        print("Data is being retrieved")
        url = "https://bigpara.hurriyet.com.tr/altin/tam-altin-fiyati/"
        sayfa = requests.get(url)
        htmlsayfa = BeautifulSoup(sayfa.content, "html.parser")
        altın = htmlsayfa.find("span", class_="value dw").getText()
        print("Instant Full Gold Rate:",altın,"TL")
    elif a == "EASTEREGG":
        dosya = "Yumurta.png"
        image = Image.open(dosya)
        image.show()
    elif a == "CHANGE LANGUAGE" or a == "DIL DEGISTIR":
        dl_scnk = input("What Language :")
        dl_scnk = dl_scnk.upper()
        if dl_scnk == "TÜRKÇE" or dl_scnk == "TURKISH":
            import koddd
        if dl_scnk == "INGILIZCE" or dl_scnk == "ENGLISH":
            print("Already english dump")
    elif a == "":
        time.sleep(0.15)
    elif a == "":
        time.sleep(0.15)
    elif a == "":
        time.sleep(0.15)
    elif a == "YARDIM" or a == "HELP" or a == "COMMANDS" or a == "PROMTS" or a == "GIRDILER":
        url = 'https://justpaste.it/crs7u'
        webbrowser.open(url)
    else:
        print("""I don't have such a command for now, type "Help" to see the commands""")
        time.sleep(0.2)
        chat(a.title(), "ChatBot :")
