import discord
import requests
from bs4 import BeautifulSoup
from discord.ext import commands
import random
import lance
import feedparser
from pytube import YouTube

token = "MTEzMjM0MzIzMjkxMTY1OTEwOQ.G49-5x.ix4cNzFDyQaB9esyr40N5JDQ24i4JARfjuKWoo"
Bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@Bot.event
async def on_ready():
     print(f'{Bot.user} Giriş Yaptı')


@Bot.command()
async def dolar(ctx,):
    url = "https://www.google.com/finance/quote/USD-TRY?hl=tr"
    sayfa = requests.get(url)
    htmlsayfa = BeautifulSoup(sayfa.content, "html.parser")
    dolar = htmlsayfa.find("div", class_="YMlKec fxKbKc").getText()
    yn = str(dolar)
    await ctx.send("Anlık Dolar Kuru: " + yn)

@Bot.command()
async def euro(ctx,):
    url = "https://www.google.com/finance/quote/EUR-TRY"
    sayfa = requests.get(url)
    htmlsayfa = BeautifulSoup(sayfa.content, "html.parser")
    dolar = htmlsayfa.find("div", class_="YMlKec fxKbKc").getText()
    yn = str(dolar)
    await ctx.send("Anlık Euro Kuru: " + yn)

@Bot.command()
async def geliştiricin_kim(ctx,):
    await ctx.send("Geliştiricimi mi merak ediyorsun")
    await ctx.send("Ama O Anlatılamayacak Kadar Mükemmel")
    await ctx.send("1. özelliği: O Çoook Yakışıklı O Kadar Yakışıklı Ki Aynaya Bile Güneş Gözlüğü İle Bakıyor")
    await ctx.send("2. Özelliği: O Ultra Mega Tega Sega Duble Triple Zeki O Kadar Zeki Ki Beni Kusursuz Bir Biçimde Yaptı")
    await ctx.send("3. Özelliği: Onun IQ Seviyesi Ülkenin IQ seviyesi Olan 86.2'nin Çok Üstünde Hatta Yıllar Önce ÖLçürdüğümüzde 120-130 Arası Çıkmıştı")

@Bot.command()
async def randomsayı(ctx,):
    sayı = random.randint(0,100)
    y_sayı = str(sayı)
    await ctx.send(y_sayı)
@Bot.command()
async def ataturk_kimdir(ctx,):
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
            await ctx.send(cumle)
@Bot.command()
async def video_bilgi(ctx):
    await ctx.send("Lütfen videonun bağlantısını giriniz:")

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    try:
        message = await Bot.wait_for('message', timeout=10.0, check=check)
        video_link = message.content

        yt = YouTube(video_link)

        await ctx.send(f"Video Başlığı: {yt.title}")
        sure = yt.length / 60
        suree = round(sure, 2)
        await ctx.send(f"Video Süresi: {suree} dakika")
        await ctx.send(f"Video İzlenme Sayısı: {yt.views}")

    except ValueError:
        await ctx.send("Geçersiz video bağlantısı, lütfen doğru bir YouTube video bağlantısı girin.")
    except TimeoutError:
        await ctx.send("Zaman aşımına uğradı, lütfen daha hızlı girin.")
    except Exception as e:
        await ctx.send(f"Bir hata oluştu: {e}")
@Bot.command()
async def hesap_makinesi(ctx):
    await ctx.send("4 İşlemden Bir İşlem Tipi Giriniz")
    await ctx.send("1.Toplama")
    await ctx.send("2.Çıkarma")
    await ctx.send("3.Çarpma")
    await ctx.send("4.Bölme")

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    try:
        message = await Bot.wait_for('message', timeout=20.0, check=check)
        veri = int(message.content)

        if veri not in [1, 2, 3, 4,]:
            await ctx.send("Geçerli bir işlem tipi seçmelisiniz.")
            return

        await ctx.send(f"İşlem Tipiniz: {veri}")

        await ctx.send("İlk sayıyı girin:")

        message = await Bot.wait_for('message', timeout=17.0, check=check)
        sayi1 = int(message.content)

        await ctx.send("İkinci sayıyı girin:")

        message = await Bot.wait_for('message', timeout=17.0, check=check)
        sayi2 = int(message.content)

        if veri == 1:
            sonuc = sayi1 + sayi2
            sonuc = str(sonuc)
            await ctx.send("Sonuç: " + sonuc )
        elif veri == 2 :
            sonuc = sayi1 - sayi2
            sonuc = str(sonuc)
            await ctx.send("Sonuç: " + sonuc )
        elif veri == 3:
            sonuc = sayi1 * sayi2
            sonuc = str(sonuc)
            await ctx.send("Sonuç: " + sonuc )
        elif veri == 4:
            sonuc = sayi1 / sayi2
            sonuc = str(sonuc)
            await ctx.send("Sonuç: " + sonuc )
        else:
            None

    except ValueError:
        await ctx.send("Lütfen geçerli bir sayı girin.")
    except TimeoutError:
        await ctx.send("Zaman aşımına uğradı, lütfen daha hızlı girin.")
@Bot.command()
async def haberler(ctx):
    await ctx.send("Kaç haber Görmek İstersiniz? (1-10): ")
    
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    try:
        message = await Bot.wait_for('message', timeout=15.0, check=check)
        veri = int(message.content)

        if veri <= 1 or veri >= 10:
            await ctx.send("Lütfen 1 ile 10 arasında geçerli bir sayı girin.")
            return

        url = "https://www.cnnturk.com/feed/rss/all/news"
        haberler = feedparser.parse(url)

        i = 0
        for haber in haberler.entries:
            if i == veri:
                break
            await ctx.send("** **")
            await ctx.send("Haber :" + haber.title)
            await ctx.send("Link :" + haber.link)
            await ctx.send("** **")
            i += 1

    except ValueError:
        await ctx.send("Lütfen geçerli bir sayı girin.")
    except TimeoutError:
        await ctx.send("Zaman aşımına uğradı, lütfen daha hızlı girin.")
@Bot.command()
async def yazı_tura(ctx):
    rstgle = random.randint(0, 100000)
    if rstgle == 50000 :
        await ctx.send("Şansa bak Dik geldi...")
    elif rstgle < 50000:
        await ctx.send("Tura Geldi.")
    elif rstgle > 50000:
        await ctx.send("Yazı Geldi")

     

Bot.run(token)