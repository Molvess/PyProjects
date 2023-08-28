from random import randint

while True:
    zar1 = randint(1,100)
    print(zar1)
    if zar1 % 5 == 0:
        print("Bölünüyor")
    else:
        print("Bölünmez")