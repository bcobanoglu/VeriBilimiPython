'''
Örnek 6.8:
1’den 34’e kadar olan tek sayıları ekranda yan yana gösteren programı
continue komutunu kullanarak kodlayalım.
'''
for a in range(1,35):
    if (a%2 ==0):
        continue
    print (a, end=" ")
