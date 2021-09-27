'''
Örnek 17.4: “D:\sifre.txt” dosyasındaki kelimelerden bir password oluşturan
programı Python dilinde kodlayınız.
'''
import random as r
dosya = "D:\sifre.txt" #öncelikle böyle bir dosya oluşturup, içerisine kelimeler yazınız
kelime = [] #kelime dizisi
#dosyadan kelimeleri oku
f = open (dosya, 'r')
for k in f:
    #sağ taraftaki boşlukları sil
    k = k.rstrip()
    #kelime listesine ekle
    kelime.append(k)
f.close() #dosyayı kapat

#listeden rastgele ilk kelimeyi seç
ilk = kelime[r.randrange(0,len(kelime))]
sifre = ilk
#8 karakterlik bir sifre olusturalım
while len(sifre)<8:
    #listeden ikinci kelime seçildi
    iki = kelime[r.randrange(0,len(kelime))]
    sifre = ilk + iki
#şifreyi gösterelim
print("Üretilen şifre.: ", sifre)