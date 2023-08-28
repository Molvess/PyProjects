import time

ad = input("Lütfen başlamak için adınızı giriniz ?")
if ad == "":
    exit()
print(f"Yarışmaya Hoşgeldin {ad}".center(50,"*"))

cd = "Cevabınız doğru"
cy = "Cevabınız yanlıştır"

soru = f"1. Barış özcan hangi oyunu sever {ad}\n A)ROBLOX \n B)MİNECRAFT \n C)ZULA ?"
print(soru)
input("ŞIK : ")
Roblox = "A"
Minecraft = "B"
Zula = "C"
soru = Minecraft

if soru == "A":
    print(cy)
    exit()
elif soru == "B":
    print(cd)
    soru = f"2. Twitchte en çok takipçisi olan adam kimdir {ad} ? \n A)Pqueen \n B)Kaanflix \n C)Elrean"
    print(soru)
    input("ŞIK : ")
    Pqueen = "A"
    Kaanflix = "B"
    Elrean = "C"
    soru = Elrean
    if soru == "A":
        print("Çok yaklaştın")
        exit()
    if soru == "B":
        print(cy)
        exit()
    if soru == "C":
        print(cd)
        print(f"Yarışmayı bitirdinnnn {ad}".center(75,"*"))
        time.sleep(10)           
    else:
        exit()

elif soru == "C":
    print(cy)
    exit()
else:
    exit()
time.sleep(10)