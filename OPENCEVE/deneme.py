import cv2
import sys

fotograf = cv2.imread("sen.jpeg")
gray = cv2.cvtColor(fotograf, cv2.COLOR_BGR2GRAY)

yuz_belirleme = cv2.CascadeClassifier("data\\haarcascade_frontalface_alt.xml")
goz_belirleme = cv2.CascadeClassifier("data\\haarcascade_eye.xml")

yuz = yuz_belirleme.detectMultiScale(
    gray, 
    scaleFactor=1.075, 
    minNeighbors=5, 
    minSize=(15, 15))

for (x,y,w,h) in yuz: 
    cv2.rectangle(
    fotograf, 
    (x,y), 
    (x+w,y+h), 
    (255,0,0),
    2) 

    roi_gray = gray[y:y+h, x:x+w] 
    roi_color = fotograf[y:y+h, x:x+w] 
      
    eyes = goz_belirleme.detectMultiScale(roi_gray) 
    for (ex,ey,ew,eh) in eyes: 
        cv2.rectangle(
        roi_color, 
        (ex,ey), 
        (ex+ew,ey+eh), 
        (0,255,0), 
        1)

print("[INFO] {0} Yüz Bulundu! Bulunan Yüz Sayısı = ".format(len(yuz)))

for (x, y, w, h) in yuz:
    cv2.rectangle(
    fotograf,
    (x, y), 
    (x + w, y + h), 
    (0,0,255), 
    2)

durum = cv2.imwrite('foto2.jpg', fotograf)
print("[ Bilgi Mesajı… ] Görsel kaydedildi: ", durum)