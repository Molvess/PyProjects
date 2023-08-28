import discord
from discord.activity import Game
from discord.ext import commands
from discord.ext.commands import bot
from discord.flags import Intents


intents = discord.Intents.all()
Bot = commands.Bot(command_prefix="-", intents=intents)


@Bot.event
async def on_ready():
    print("BANE")
    

@Bot.command()
async def YardımEtBot(msg):
    await msg.send("Kullanabilceğin Komutlar : ")
    await msg.send("aglamak")
    await msg.send("pepedans")
    await msg.send("otuzbir")
    await msg.send("öpücük")
    await msg.send("supra")
    await msg.send("Fbı")
    await msg.send("np")
    await msg.send("bruh")
    await msg.send("amogus")
    await msg.send("lol")
    await msg.send("like")
    await msg.send("dislike")
    await msg.send("nazarboncuğu")
    await msg.send("tr")
    await msg.send("us")
    await msg.send("ukraynaya_destek_ol")
    await msg.send("savaşbitsin , #SAVAŞBİTSİNARTIK(SBA)")
    await msg.send("bluuscren")
    await msg.send("UnoTers")
    await msg.send("patlakedi")
    await msg.send("golem")
    await msg.send("belkii")
    await msg.send("sismankity")
    await msg.send("ekmekarasıkity")
    await msg.send("ok")
    await msg.send("şakakanka")
    await msg.send("amogus")
    await msg.send("öperim")
    await msg.send("senaglıon")
    await msg.send("coktatlısın")
    await msg.send("vayderdogan")
    await msg.send("dil")
    await msg.send("aaaaa")
    await msg.send("haddinibil")
    await msg.send("sewgili")
    await msg.send("hokage")
    await msg.send("muzcukedy")
    await msg.send("dans")
    await msg.send("sewgili2")
    await msg.send("ağlama")
    await msg.send("lütfen")
    await msg.send("opucuk")
    await msg.send("utangaç")
    await msg.send("koşgelio")
    await msg.send("sıkıldım")
    await msg.send("yokbe")
    await msg.send("senhemenarkaya")
    await msg.send("loading")
    await msg.send("şaşykedy")
    await msg.send("öpüşşşş")
    await msg.send("Drakbakış")
    await msg.send("nahh")
    await msg.send("sinsrock")
    await msg.send("gayu")
    await msg.send("cıkarmayacalışıyorsundur")
    await msg.send("çay")
    await msg.send("crykedy")
    await msg.send("muck")
    await msg.send("adanalıkedy")
    await msg.send("djkedy")
    await msg.send("hackerkedy")
    await msg.send("gelgel")
    await msg.send("supermenkedy")
    await msg.send("ısırırım")
    await msg.send("dans2")
    await msg.send("aduket")
    await msg.send("ehehe")
    await msg.send("*Emekigeçenler*")

@Bot.command()
async def aglamak(ctx,):
        await ctx.send("https://cdn.discordapp.com/emojis/877129505863516160.png?size=64")
@Bot.command()
async def pepedans(ctx,):
        await ctx.send("https://cdn.discordapp.com/emojis/880906167562416248.gif?size=64")
@Bot.command()
async def otuzbir(ctx,):
        await ctx.send("https://cdn.discordapp.com/emojis/853947691860230164.gif?size=64")
@Bot.command()
async def öpücük(ctx):
    await ctx.send("https://cdn.discordapp.com/emojis/842050273740455967.png?size=64")
@Bot.command()
async def supra(ctx):
    await ctx.send("https://tenor.com/view/supra-gif-22160855")
@Bot.command()
async def Fbı(ctx):
    await ctx.send("https://tenor.com/view/fbi-fbiopenup-carlwhitman-gif-19586039")
@Bot.command()
async def np(ctx):
    await ctx.send("https://tenor.com/view/np-nope-check-boxes-gif-7864220")
@Bot.command()
async def bruh(ctx):
    await ctx.send("https://tenor.com/view/monkey-bruh-weak-sick-gif-16818912")
@Bot.command()
async def amongus(ctx):
    await ctx.send("https://cdn.discordapp.com/emojis/764770867661242379.png?size=64 ")
@Bot.command()
async def lol(ctx):
    await ctx.send("https://cdn.discordapp.com/emojis/754413401610125352.png?size=64 ")
@Bot.command()
async def like(ctx):
    await ctx.send("https://cdn.discordapp.com/emojis/638921289305948180.png?size=64 ")
@Bot.command()
async def dislike(ctx):
    await ctx.send("https://cdn.discordapp.com/emojis/638921287892336690.png?size=64 ")
@Bot.command()
async def nazarboncuğu(ctx):
    await ctx.send("https://cdn.discordapp.com/emojis/754413405984784525.png?size=64 ")
@Bot.command()
async def tr(ctx):
    await ctx.send(":flag_tr:")
@Bot.command()
async def us(ctx):
    await ctx.send(":flag_us:")
@Bot.command()
async def ukraynaya_destek_ol(ctx):
    await ctx.send(":flag_ua:")
    await ctx.send(":flag_ua:")
    await ctx.send(":flag_ua:")
@Bot.command()
async def savaşbitsin(ctx):
    await ctx.send(":flag_ru:")
    await ctx.send(":skull_crossbones:")
@Bot.command()
async def bluuscren(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/850766598246629436/852901398923575326/220px-Maviekran.gif")
@Bot.command()
async def UnoTers(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/850766598246629436/950435121113206794/uno-yon-degistir-ters-kart.png")
@Bot.command()
async def patlakedi(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/1015373400182636654/1016746991734231180/853009304605294593-unscreen.gif")
@Bot.command()
async def golem(ctx):
    await ctx.send("https://cdn.discordapp.com/emojis/829327424138903572.gif?size=48")
@Bot.command()
async def belkii(ctx):
    await ctx.send("https://tenor.com/view/maybe-shy-rosycheeks-mochi-cat-peach-cat-gif-16992928")
@Bot.command()
async def sismankity(ctx):
    await ctx.send("https://tenor.com/view/cat-standing-fat-epic-gif-23115386")
@Bot.command()
async def ekmekarasıkity(ctx):
    await ctx.send("https://tenor.com/view/kitty-gif-25023528")
@Bot.command()
async def ok(ctx):
    await ctx.send("https://tenor.com/view/crycat-crying-cat-crying-cat-thumbs-up-thumbs-up-ok-gif-22851318")
@Bot.command()
async def şakakanka(ctx):
    await ctx.send("https://tenor.com/view/%C5%9Faka-kanka-aykut-elmas-halil-ibrahim-g%C3%B6ker-vine-gif-19541733")
@Bot.command()
async def amogus(ctx):
    await ctx.send("https://c.tenor.com/gQV5VzHLWQIAAAAd/among-us-sus.gif")
@Bot.command()
async def öperim(ctx):
    await ctx.send("https://tenor.com/view/milk-and-mocha-bear-couple-kiss-gif-12554112")
@Bot.command()
async def senaglıon(ctx):
    await ctx.send("https://tenor.com/view/sen-aglion-tr-rock-gif-22349919")
@Bot.command()
async def coktatlısın(ctx):
    await ctx.send("https://tenor.com/view/cok-tatlisin-recep-tayyip-erdogan-akp-gif-11392700")
@Bot.command()
async def vayderdogan(ctx):
    await ctx.send("https://tenor.com/view/wide-erdogan-thic-erdogan-erdogan-tayyip-gif-18108354")
@Bot.command()
async def dil(ctx):
    await ctx.send("https://tenor.com/view/grimace-cat-grimace-cat-cats-cat-fun-gif-17582724")
@Bot.command()
async def aaaaa(ctx):
    await ctx.send("https://tenor.com/view/cat-impressed-cat-wow-drewisme-fun-cat-funny-cat-gif-17551257")
@Bot.command()
async def haddinibil(ctx):
    await ctx.send("https://tenor.com/view/rte-receptayyip-erdo%C4%9Fan-haddinibil-rtehaddinibil-gif-21346531")
@Bot.command()
async def sewgili(ctx):
    await ctx.send("https://tenor.com/view/kiss-gif-22640695")
@Bot.command()
async def hokage(ctx):
    await ctx.send("https://tenor.com/view/naruto-gif-23864298")
@Bot.command()
async def muzcukedy(ctx):
    await ctx.send("https://tenor.com/view/cat-monkey-costume-banana-cat-eating-a-banana-gif-7396869")    
@Bot.command()
async def dans(ctx):
    await ctx.send("https://tenor.com/view/smile-dancing-dance-moves-milk-and-mocha-bear-gif-17303508")
@Bot.command()
async def sewgili2(ctx):
    await ctx.send("https://tenor.com/view/camocaio-moio-gif-19828093")
@Bot.command()
async def ağlama(ctx):
    await ctx.send("https://tenor.com/view/milk-and-mocha-bears-cry-tears-stop-crying-gif-13093760")
@Bot.command()
async def lütfen(ctx):
    await ctx.send("https://tenor.com/view/milk-mocha-milk-and-mocha-bears-cute-sad-gif-13418496")
@Bot.command()
async def opucuk2(ctx):
    await ctx.send("https://tenor.com/view/milk-and-mocha-bear-couple-kiss-gif-12554112")
@Bot.command()
async def utangaç(ctx):
    await ctx.send("https://tenor.com/view/milk-and-mocha-bear-couple-aww-thanks-blush-gif-12498619")
@Bot.command()
async def koşgelio(ctx):
    await ctx.send("https://tenor.com/view/love-me-bear-run-gif-10271399")
@Bot.command()
async def sıkıldım(ctx):
    await ctx.send("https://tenor.com/view/dnddn-cat-love-you-gif-22100648")
@Bot.command()
async def yokbe(ctx):
    await ctx.send("https://tenor.com/view/recep-tayyip-erdo%C4%9Fan-rte-yok-turk-turkish-gif-16348590")    
@Bot.command()
async def senhemenarkaya(ctx):
    await ctx.send("https://tenor.com/view/mai-sakurajima-ao-buta-serious-hairflip-gif-12680892")
@Bot.command()
async def loading(ctx):
    await ctx.send("https://tenor.com/view/mai-sakurajima-sakurajima-mai-thinking-anime-girl-thinking-gif-23732831")  
@Bot.command()
async def şaşykedy(ctx):
    await ctx.send("https://tenor.com/view/crazy-eyes-cat-cat-fun-fun-cat-funny-cat-cat-funny-gif-17550699")    
@Bot.command()
async def öpüşşşş(ctx):
    await ctx.send("https://cdn.discordapp.com/emojis/597207108005658634.gif?size=48")
@Bot.command()
async def Drakbakış(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/904832141060370493/1016797648814088242/11a4a5840abda69d656105e63500e161.jpeg")    
@Bot.command()
async def nahh(ctx):
    await ctx.send("https://tenor.com/view/kocaman-bir-nah-nah-el-hareketi-dance-lick-hands-gif-17894624")   
@Bot.command()
async def gayu(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/798636646077300757/1016792930805104720/unknown.png")   
@Bot.command()
async def cıkarmayacalışıyorsundur(ctx):
    await ctx.send("https://tenor.com/view/rraenee-rraene-rane-rrane-twitch-gif-25767735")
@Bot.command()
async def sinsrock(ctx):
    await ctx.send("https://tenor.com/view/the-rock-gif-22026928")
@Bot.command()
async def çay(ctx):
    await ctx.send("https://tenor.com/view/kermit-sips-tea-tea-gif-8953704")
@Bot.command()
async def crykedy(ctx):
    await ctx.send("https://tenor.com/view/cry-cat-crying-cat-crying-cat-crying-gif-26105855")
@Bot.command()
async def muck(ctx):
    await ctx.send("https://tenor.com/view/come-here-hugs-hugs-and-love-hug-me-cat-hug-gif-18029548")
@Bot.command()
async def adanalıkedy(ctx):
    await ctx.send("https://tenor.com/view/adana-adanali-adanalikedi%CC%87-adanal%C4%B1kedi-kedi-gif-22702447")
@Bot.command()
async def djkedy(ctx):
    await ctx.send("https://tenor.com/view/cat-dance-catto-dace-dj-cat-gif-24258085")
@Bot.command()
async def hackerkedy(ctx):
    await ctx.send("https://tenor.com/view/work-working-working-cat-working-from-home-cat-gif-19630802")
@Bot.command()
async def gelgel(ctx):
    await ctx.send("https://tenor.com/view/cat-cute-baby-cat-cats-cat-lady-gif-20142216")
@Bot.command()
async def supermenkedy(ctx):
    await ctx.send("https://tenor.com/view/fat-cat-laser-eyes-angry-cat-cyclops-nara-gif-26030753")
@Bot.command()
async def ısırırım(ctx):
    await ctx.send("https://tenor.com/view/love-cat-love-cats-cat-cats-gif-24534809")
@Bot.command()
async def dans2(ctx):
    await ctx.send("https://tenor.com/view/dancing-bear-eisha-idgaf-bear-dance-gif-18806083")
@Bot.command()
async def aduket(ctx):
    await ctx.send("https://tenor.com/view/kick-mad-cute-love-gif-20621967")
@Bot.command()
async def ehehe(ctx):
    await ctx.send("https://tenor.com/view/excited-milk-and-mocha-cute-bear-white-bear-love-bear-gif-15248522")


@Bot.command()
async def komvoy(msg):
    await msg.send("https://cdn.discordapp.com/emojis/877129505863516160.png?size=64")
    await msg.send("https://cdn.discordapp.com/emojis/880906167562416248.gif?size=64")
    await msg.send("https://cdn.discordapp.com/emojis/853947691860230164.gif?size=64")
    await msg.send("https://cdn.discordapp.com/emojis/842050273740455967.png?size=64")
    await msg.send("https://tenor.com/view/supra-gif-22160855")
    await msg.send("https://tenor.com/view/fbi-fbiopenup-carlwhitman-gif-19586039")
    await msg.send("https://tenor.com/view/np-nope-check-boxes-gif-7864220")
    await msg.send("https://tenor.com/view/monkey-bruh-weak-sick-gif-16818912")
    await msg.send("https://cdn.discordapp.com/emojis/764770867661242379.png?size=64 ")
    await msg.send("https://cdn.discordapp.com/emojis/754413401610125352.png?size=64 ")
    await msg.send("https://cdn.discordapp.com/emojis/638921289305948180.png?size=64 ")
    await msg.send("https://cdn.discordapp.com/emojis/638921287892336690.png?size=64 ")
    await msg.send("https://cdn.discordapp.com/emojis/754413405984784525.png?size")
    await msg.send(":flag_tr:")
    await msg.send(":flag_us:")
    await msg.send(":flag_ua:")
    await msg.send(":flag_ua:")
    await msg.send(":flag_ua:")
    await msg.send(":flag_ru:")
    await msg.send(":skull_crossbones:")
    await msg.send("https://cdn.discordapp.com/attachments/850766598246629436/852901398923575326/220px-Maviekran.gif")
    await msg.send("https://cdn.discordapp.com/attachments/850766598246629436/950435121113206794/uno-yon-degistir-ters-kart.png")
    await msg.send("https://cdn.discordapp.com/attachments/1015373400182636654/1016746991734231180/853009304605294593-unscreen.gif")
    await msg.send("https://cdn.discordapp.com/emojis/829327424138903572.gif?size=48")
    await msg.send("https://tenor.com/view/maybe-shy-rosycheeks-mochi-cat-peach-cat-gif-16992928")
    await msg.send("https://tenor.com/view/cat-standing-fat-epic-gif-23115386")
    await msg.send("https://tenor.com/view/kitty-gif-25023528")
    await msg.send("https://tenor.com/view/crycat-crying-cat-crying-cat-thumbs-up-thumbs-up-ok-gif-22851318")
    await msg.send("https://tenor.com/view/%C5%9Faka-kanka-aykut-elmas-halil-ibrahim-g%C3%B6ker-vine-gif-19541733")
    await msg.send("https://c.tenor.com/gQV5VzHLWQIAAAAd/among-us-sus.gif")
    await msg.send("https://tenor.com/view/milk-and-mocha-bear-couple-kiss-gif-12554112")
    await msg.send("https://tenor.com/view/sen-aglion-tr-rock-gif-22349919")
    await msg.send("https://tenor.com/view/cok-tatlisin-recep-tayyip-erdogan-akp-gif-11392700")
    await msg.send("https://tenor.com/view/wide-erdogan-thic-erdogan-erdogan-tayyip-gif-18108354")
    await msg.send("https://tenor.com/view/grimace-cat-grimace-cat-cats-cat-fun-gif-17582724")
    await msg.send("https://tenor.com/view/cat-impressed-cat-wow-drewisme-fun-cat-funny-cat-gif-17551257")
    await msg.send("https://tenor.com/view/rte-receptayyip-erdo%C4%9Fan-haddinibil-rtehaddinibil-gif-21346531")
    await msg.send("https://tenor.com/view/kiss-gif-22640695")
    await msg.send("https://tenor.com/view/naruto-gif-23864298")
    await msg.send("https://tenor.com/view/cat-monkey-costume-banana-cat-eating-a-banana-gif-7396869")
    await msg.send("https://tenor.com/view/smile-dancing-dance-moves-milk-and-mocha-bear-gif-17303508")
    await msg.send("https://tenor.com/view/camocaio-moio-gif-19828093")
    await msg.send("https://tenor.com/view/milk-and-mocha-bears-cry-tears-stop-crying-gif-13093760")
    await msg.send("https://tenor.com/view/milk-mocha-milk-and-mocha-bears-cute-sad-gif-13418496")
    await msg.send("https://tenor.com/view/milk-and-mocha-bear-couple-kiss-gif-12554112")
    await msg.send("https://tenor.com/view/milk-and-mocha-bear-couple-aww-thanks-blush-gif-12498619")
    await msg.send("https://tenor.com/view/love-me-bear-run-gif-10271399")
    await msg.send("https://tenor.com/view/dnddn-cat-love-you-gif-22100648")
    await msg.send("https://tenor.com/view/recep-tayyip-erdo%C4%9Fan-rte-yok-turk-turkish-gif-16348590")
    await msg.send("https://tenor.com/view/mai-sakurajima-ao-buta-serious-hairflip-gif-12680892")
    await msg.send("https://tenor.com/view/mai-sakurajima-sakurajima-mai-thinking-anime-girl-thinking-gif-23732831")
    await msg.send("https://tenor.com/view/crazy-eyes-cat-cat-fun-fun-cat-funny-cat-cat-funny-gif-17550699")
    await msg.send("https://cdn.discordapp.com/emojis/597207108005658634.gif?size=48")
    await msg.send("https://cdn.discordapp.com/attachments/904832141060370493/1016797648814088242/11a4a5840abda69d656105e63500e161.jpeg")
    await msg.send("https://tenor.com/view/kocaman-bir-nah-nah-el-hareketi-dance-lick-hands-gif-17894624")
    await msg.send("https://tenor.com/view/rraenee-rraene-rane-rrane-twitch-gif-25767735")
    await msg.send("https://tenor.com/view/the-rock-gif-22026928")
    await msg.send("https://tenor.com/view/kermit-sips-tea-tea-gif-8953704")
    await msg.send("https://tenor.com/view/cry-cat-crying-cat-crying-cat-crying-gif-26105855")
    await msg.send("https://tenor.com/view/come-here-hugs-hugs-and-love-hug-me-cat-hug-gif-18029548")
    await msg.send("https://tenor.com/view/adana-adanali-adanalikedi%CC%87-adanal%C4%B1kedi-kedi-gif-22702447")
    await msg.send("https://tenor.com/view/cat-dance-catto-dace-dj-cat-gif-24258085")
    await msg.send("https://tenor.com/view/work-working-working-cat-working-from-home-cat-gif-19630802")
    await msg.send("https://tenor.com/view/cat-cute-baby-cat-cats-cat-lady-gif-20142216")
    await msg.send("https://tenor.com/view/fat-cat-laser-eyes-angry-cat-cyclops-nara-gif-26030753")
    await msg.send("https://tenor.com/view/love-cat-love-cats-cat-cats-gif-24534809")
    await msg.send("https://tenor.com/view/dancing-bear-eisha-idgaf-bear-dance-gif-18806083")
    await msg.send("https://tenor.com/view/kick-mad-cute-love-gif-20621967")
    await msg.send("https://tenor.com/view/excited-milk-and-mocha-cute-bear-white-bear-love-bear-gif-15248522")



@Bot.command()
async def Emekigeçenler(msg):
    await msg.send("Kodlayan:" "" "<@429614390489120770>" )
    await msg.send("Fikir verenler :" "" "<@758756135472988176>,<@429614390489120770>")
    await msg.send("Test Edenler:" "" "<@429614390489120770>,<@758756135472988176>,KıraathaneYetkilileri")


Bot.run('ODk1NzM5MTAyMTE5NDczMTYy.Gi_QWS.N52UIlMn7bhR96NDI3Qptk3TQtwN0yLdFZa-WU')