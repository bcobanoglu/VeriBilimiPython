'''
Örnek 9.11:
Bir metindeki harflerin ve kelimelerin sayısını veren programı kodlayınız.
Çözüm:
'''
metin = "Gözler boştu donuktu."
hS = 0 #harf sayısı
kS = 0 #kelime sayısı
for i in metin:
    if (i.isalpha()!=0):
        hS+=1
    if (i.isspace()!=0):
        kS+=1
print ("Kelime sayısı: ", kS+1)
print ("Harf sayısı: ", hS)