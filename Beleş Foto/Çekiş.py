import urllib.request
import os

current_folder = os.getcwd()
images_folder = current_folder + os.sep + "FOTOLAR"

if not os.path.isdir(images_folder):
    os.mkdir(images_folder)
    print("Foto Klasörü Oluştu")

n = int(input("Foto Adedi = "))
url = "https://source.unsplash.com/random"

for i in range(1, n+1):
    filename = images_folder + os.sep + f"Foto{i}" + ".png"
    urllib.request.urlretrieve(url, filename)

