#a = 10 
#b = 15
#if b > a :
#   print("b , a'dan buyuktur.")
#elif a == b : 
#      print("a ve b birbirine esittir")
#else:
#     print("a, b'den buyuktur.") 


x = int(input("Yaşınızı alalım :"))

if  x >= 18 :
  print("Hoşgeldin kardeş") 
else:
  print(f"{x} yaşındasın ama ;Dur bakalım daha " +str(18-x) +" Yılın Kadar var cıkcık")