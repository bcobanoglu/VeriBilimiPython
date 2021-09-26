'''
Örnek 10.2:
Girilen bir metni listeye dönüştürüp o metnin palindrom olup olmadığını
sorgulayan ve eğer palindrom değilse de palindroma dönüştüren programı
kodlayalım.
'''
metin = input("Bir metin gir.:")
L = list(metin) #listeye dönüştürdük
if( L == L[::-1]): #ilk ve son elemanı karşılaştır
    print(metin, ":palindrom")
else:
    print(metin, ":palindrom degil")
    t = L[::-1]
    for i in t:
        L.append(i)
    print("Ama şimdi palindrom oldu:", *L)