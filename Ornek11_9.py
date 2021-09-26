'''
Örnek 11.9:
Kelimelerin zıt anlamlarını tutan bir sözlük yapısını başka bir sözlüğe
kopyalayan programı kodlayınız.
'''
tersi = {"Yukarı":"Aşağı", "Sağ":"Sol", "Evet":"Hayır", "Doğru":"Yanlış"}
zitKopya = {}           #boş sözlük
zitKopya = tersi.copy() # sözlüğün kopyası oluştu
zitKopya["Sağ"] = "Ölü"
# bir elemanın değeri değiştirildi
print (tersi)
print (zitKopya)
print ("Sağ tersi.:", tersi["Sağ"])