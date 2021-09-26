'''
Örnek 9.9:
Bir metindeki sesli harf sayısını hesaplayan programı kodlayalım.
'''
metin = "ilim kendini bilmektir."
sesli = "aeıiouü"
sayac = 0
for harf in metin.lower():
    if harf in sesli:
        sayac = sayac + 1

print ("Sesli harf sayısı: ", sayac)