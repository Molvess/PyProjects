import json


ogurencı1 = {
    "ad" : "Alice",
    "soyad" : "Gellikur",
    "yas" : 18,
    "sehir" : "Los angellos",
    "adres" : {
        "cadde" : "Salla vursunlar caddesi",
        "sokak" : "Ben neden varım sokak",
        "numara" : 254,
    },
    "dalı" : "Engineer Software",
    "hobbies" : ["footbal","basketball"]
    }


ogurencı2 = {
    "ad" : "Johny",
    "soyad" : "Hellur",
    "yas" : 22,
    "sehir" : "Los angellos",
    "adres" : {
        "cadde" : "Salla vursunlar caddesi",
        "sokak" : "Ben neden varım sokak",
        "numara" : 254,
    },
    "dalı" : "Sofware Software",
    "hobbies" : ["handball","basketball"],
    }


json_string1 = json.dumps(ogurencı1, indent=4)
parsed_data1 = json.loads(json_string1)
json_string2 = json.dumps(ogurencı2, indent=4)
parsed_data2 = json.loads(json_string2)


print("Ad = " , parsed_data1["ad"])
print("Yaşı = " , parsed_data1["yas"])
print("Dalı = " , parsed_data1["dalı"])
print("Adresi = " , parsed_data1["adres"]["cadde"],parsed_data1["adres"]["sokak"],parsed_data1["adres"]["numara"])
print("Hobileri = " , parsed_data1["hobbies"])

print("Ad = " , parsed_data2["ad"])
print("Yaşı = " , parsed_data2["yas"])
print("Dalı = " , parsed_data2["dalı"])
print("Adresi = " , parsed_data2["adres"]["cadde"],parsed_data2["adres"]["sokak"],parsed_data2["adres"]["numara"])
print("Hobileri = " , parsed_data2["hobbies"])











'''
x = {
    "name": "Barış",
     "age" : 15,
     "city" : "Aydın",
    }


x = {
    "ad" : "Johny",
    "soyad" : "Hellur",
    "yas" : 36,
    "sehir" : "Los angellos",
    "adres" : "Salla vursunlar caddesi,Ben neden varım sokak no 254",
    "evlimi" : True,
    "cocukvarmi" : False,
    }

print(x)

'''








