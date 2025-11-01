import subprocess
import os
import time 

HONEYGAIN_YOLU = r"C:\Program Files (x86)\Honeygain\Honeygain.exe"


GIZLI_BAYRAK = 0x08000000 

while True:
    task_list = subprocess.check_output("tasklist").decode("utf-8") 

    if "Honeygain.exe" in task_list:
        print("Program açık")
    else:
        print("Program kapalı, gizlice yeniden başlatılıyor...")
        try:
            subprocess.Popen([HONEYGAIN_YOLU], creationflags=GIZLI_BAYRAK)
            print("Honeygain gizlice başlatıldı.")
        except FileNotFoundError:
            print(f"HATA: {HONEYGAIN_YOLU} yolu bulunamadı.")
            
    time.sleep(5)
