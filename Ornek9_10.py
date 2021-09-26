'''
Örnek 9.10: Bir metindeki kelime ve cümle sayısını ekranda gösteren programı
kodlayınız
'''
metin = "Gözler boştu donuktu. Sözler anlamsızdı soğuktu. Belli ki buradan kopmuştu."
cumle = metin.split(".")
cS=0 #cumle sayacı
kelime = metin.split(" ")
kS=0 #kelime sayacı
for x in cumle:
    cS = cS + 1
for y in kelime:
    kS = kS + 1
print ("Cümle sayısı: ", cS-1)
print ("Kelime sayısı: ", kS)