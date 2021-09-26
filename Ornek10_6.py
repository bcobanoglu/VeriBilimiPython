'''
Örnek 10.6:
Bir listeyi (diziyi) fonksiyon parametresi olarak alan ve bu listeye yeni elemanlar
ekleyen bir programı kodlayalım
'''

#f fonksiyonu parametresi: L listesi
def f(L): #veya eşdeğeri: def f(L=[])
    L.append(5) #listeye eleman ekle
    return L

#Ana program
L = [1,2,3,4]
print (f(L)) #f fonksiyonu çağrıldı