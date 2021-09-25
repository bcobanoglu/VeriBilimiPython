'''
Örnek 8.2 (Sayısal Loto Çekilişi):
Bilgisayarın rastgele ürettiği 1-49 arasındaki 6 adet sayıyı sayısal loto çekiliş
sonucu olarak ekrana yazan programı kodlayalım.
'''

from random import *
L = [] # boş liste
print("Sayısal Loto Çekilişi\n")
for i in range (6):
    loto = randint(1,49)
    #üretilen sayı listede varsa
    while loto in L:
        #yeniden sayı üret
        loto = randint(1,49)
    #sayıları listeye ekle
    L.append (loto)

print (*L) #listeyi yazdır