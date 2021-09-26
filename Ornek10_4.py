'''
Örnek 10.4:
Bir L listesinde aranan sayı varsa sayının listedeki yerini ve sırasını veren
programı kodlayalım.
'''
L = [2, 3, 5, 8, 9, 12, 33, 6, 7, 11]
Ara=int(input("Aranan Sayı: "))
if Ara in L:#True ise
    i=L.index(Ara)#Arananin indisi
    print("Aranan", i+1, ". sırada bulundu")
else:#False ise
    print ("Aranan bulunamadı.")