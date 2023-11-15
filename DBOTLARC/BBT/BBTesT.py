import discord
from discord import message
from discord.activity import Game
from discord.ext import commands
from discord.flags import Intents
from random import randint as r

intents = intents = discord.Intents.all()
Bot = commands.Bot(command_prefix= "!bb ", intents=intents)

 
 

@Bot.event
async def on_ready():
    print("LETZ GOO")
@Bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name ="bot-sohbet")
    await channel.send(f"{member} aramıza katıldı :D")
    print(f"{member} aramıza katıldı :D")
@Bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name ="bot-sohbet")
    await channel.send(f"{member} aramızdan gitti :(")
    print(f"{member} aramızdan gitti :(")
@Bot.command()
async def sa(ctx,):
        await ctx.send("Aleykümselam.")
@Bot.command()
async def napim(ctx,):
        await ctx.send("!Bokye!")
@Bot.command()
async def bane(ctx,):
        await ctx.send("Yarrağımı YE!")
@Bot.command()
async def otuzbir(ctx,):
        await ctx.send("Mal Vales!")
@Bot.command()
async def ülkeyanıyorneyapacağız(msg):
    await msg.send("!ÇAY İÇ SÖNDÜRÜR!")
#bak şuan söndü :D
@Bot.command()
async def amsikçükmemeyarraktaşşakotuzbir(msg):
    await msg.send(":face_with_raised_eyebrow:")
#NE BİÇİM KOD MK

@Bot.command()
async def barış(msg):
    await msg.send("<@!429614390489120770>")

@Bot.command()
async def yasin(msg):
    await msg.send("<@!875183719818887178>")

@Bot.command()
async def ırmak(msg):
    await msg.send("<@!836909961589948446>")

@Bot.command()
async def ömer(msg):
    await msg.send("<@!888366390942244915>")

@Bot.command()
async def salih(msg):
    await msg.send("<@!789951612097134603>")

@Bot.command()
async def tugay(msg):
    await msg.send("<@!743117387255119893>")

@Bot.command()
async def fadime(msg):
    await msg.send("<@!862748015898918912>")

@Bot.command()
async def durmuş(msg):
    await msg.send("<@!591612120383094785>")

@Bot.command()
async def enver(msg):
    await msg.send("<@!887301303607386122>")

@Bot.command()
async def aşkın(msg):
    await msg.send("<@!787061754936426506>")

@Bot.command()
async def zeynep(msg):
    await msg.send("<@!608260229829885992>")
    
@Bot.command()
async def abdullah(msg):
    await msg.send("<@!852613513959833620>")
@Bot.command()
async def bekir(msg):
    await msg.send("<@!565348520677343232>")
@Bot.command()
async def herkes(msg):
    await msg.send("<@!429614390489120770>")
    await msg.send("<@!875183719818887178>")
    await msg.send("<@!836909961589948446>")
    await msg.send("<@!888366390942244915>")
    await msg.send("<@!789951612097134603>")
    await msg.send("<@!743117387255119893>")
    await msg.send("<@!862748015898918912>")
    await msg.send("<@!591612120383094785>")
    await msg.send("<@!887301303607386122>")
    await msg.send("<@!787061754936426506>")
    await msg.send("<@!608260229829885992>")
    await msg.send("<@!852613513959833620>")
    await msg.send("<@!565348520677343232>")

"""
@Bot.command()
async def zarat(ctx):
    await ctx.send("Zar Atıldı")
    await ctx.send(game.zar_at())
@Bot.command()
async def sayısalla(ctx):
    await ctx.send("Sayıyı Salladın")
    await ctx.send(game.sayı_salla())
"""


@Bot.command()
async def yardım(ctx):
    await ctx.send("Yapımcılar için ""!bb yapımcılar"" yazınız")
    await ctx.send("Kodları görmek için ""!bb kodlar"" yazınız")
    await ctx.send("Zar atmak için ""!bb zarat"" yazınız")
    await ctx.send("Napim cevabını vermek için kullanılır""!bb napim"" yazınız")
    await ctx.send("Bane yazmak için ""!bb bane"" yazınız")
    await ctx.send("Sayı sallamak için ""!bb sayısalla"" yazınız")
    await ctx.send("Belli bir sayıdaki mesajları silmek için ""!bb tnt (miktar)"" yazınız")
    await ctx.send("Tüm mesajları silmek için ""!bb nuke"" yazınız")

@Bot.command()
async def kodlar(ctx):
    await ctx.send("zarat,yardım,ülkeyanıyorneyapacağız,yapımcılar,tnt,napim,bane,otuzbir,sayısalla,nuke,amsikçükmemeyarraktaşşakotuzbir")

@Bot.command()
async def tnt(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
@Bot.command()
async def nuke(ctx, amount=9999):
    await ctx.channel.purge(limit=amount)
    await ctx.send("MESAJLAR PATLATILDI :radioactive:")
    await ctx.channel.purge(limit=1)
    print("HEPSİ PATLADI")

@Bot.command()
async def yapımcılar(msg):
    await msg.send("Kodlayan:" "" "@Shaker#2824" )
    await msg.send("Tasarım :" "" "@reiki#8431")
    await msg.send("Test Edenler:" "" "@Shaker#2824,@reiki#8431,@TugayEkin#0011" )

Bot.run('')
