import random
import os
import time

def FirstcomeFirstserved():
#FCFS ilk gelen geçer
#P1-P2-P3-P4
    for i in range(len(sayılar)-1):  # sondan bir öncekine kadar
        sayılar[i] = sayac + sayılar[i]
        sayılar[i+1] = sayılar[i+1] + sayılar[i]
    Procces = {
        "p1":p1,
        "p2":p2,
        "p3":p3,
        "p4":p4
    }
    print(Procces)
    cvp = float(input("Cevap nedir = "))
    sayılar.pop()
    doru_cevap = sum(sayılar)/4
    if cvp == doru_cevap:
        print("Doğru cevap tebriklerr!")
    else:
        print("Yanlış gral tekrar dene ustam")
        print(doru_cevap)
def ShortestJobFirst():
    kopya = sayılar.copy()
    kopya.sort()
    # Procces'leri kullanıcıya göstermek için orijinal listeyi kullan
    Procces = {f"p{i+1}": sayılar[i] for i in range(len(sayılar))}
    print(Procces)

    # Ortalama bekleme süresini SJF mantığıyla hesapla
    toplam = 0
    beklemeler = []
    for i in range(len(kopya)):
        beklemeler.append(toplam)
        toplam += kopya[i]
    doru_cevap = sum(beklemeler) / len(beklemeler)

    # Kullanıcıdan cevap al
    try:
        cvp = float(input("Cevap nedir = "))
    except ValueError:
        print("Geçerli bir sayı gir ustam.")
        return

    if abs(cvp - doru_cevap) < 1e-6:
        print("Doğru cevap tebriklerr!")
    else:
        print("Yanlış gral tekrar dene ustam")
        print("Doğru cevap:", doru_cevap)
def prioritys():
    # Processler ve burst time
    processes = ["p1","p2","p3","p4"]
    bursts = [random.randint(1,20) for _ in processes]

    # Öncelikler 1-4 rastgele
    prio = [1,2,3,4]
    random.shuffle(prio)

    print("Processler ve değerleri:")
    for i in range(4):
        print(f"{processes[i]}: Burst={bursts[i]}, Öncelik={prio[i]}")

    # Önceliğe göre sıralama (küçük öncelik önce)
    for i in range(4):
        for j in range(i+1,4):
            if prio[i] > prio[j]:
                prio[i], prio[j] = prio[j], prio[i]
                bursts[i], bursts[j] = bursts[j], bursts[i]
                processes[i], processes[j] = processes[j], processes[i]

    # Tamamlanma süreleri ve MS
    cum_time = 0
    waiting_total = 0
    for i in range(4):
        waiting_total += cum_time
        cum_time += bursts[i]
    ms = waiting_total / 4

    # Kullanıcıdan float girişi
    try:
        user_input = float(input("\nCevabınız nedir = "))
        if abs(user_input - ms) < 1e-2:
            print(f"Doğru! MS = {ms:.2f}")
        else:
            print(f"Yanlış. Doğru MS = {ms:.2f}")
    except:
        print("⚠ Geçerli bir sayı gir.")

while True:
    print("İşletim sistemi çizelgeleme algoritma araştırmasına hoşgeldiniz")
    print("Algoritmanın tam adını giriniz")
    print("Çıkış yapmak için 'q' basınız")
    a_deger = input("Hangi algoritmanın alıştırmasını yapmak istersiniz = ")
    a_deger = a_deger.lower()

    p1 = random.randint(1,15)
    p2 = random.randint(1,15)
    p3 = random.randint(1,15)
    p4 = random.randint(1,15)

    sayılar = [p1,p2,p3,p4]
    sayac = 0
    
    match a_deger:
        case "fcfs":
            FirstcomeFirstserved()
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
        case "sjf":
            ShortestJobFirst()
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
        case "ps":
            prioritys()
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
        case "q":
            break
        case _:
            print("Yanlış tuşlama")
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue