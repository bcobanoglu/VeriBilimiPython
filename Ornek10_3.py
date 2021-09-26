'''
Örnek 10.3:
Kullanıcının girdiği bir cümleyi listeye dönüştüren ve bu listeden sesli harfleri
çıkaran (sessiz harflerden bir liste oluşturan) programı kodlayalım.
'''
L = [] #boş liste
cumle=input('Bir Cümle Giriniz.:')
L=list(cumle) #listeye dönüştür
print ("Sessiz Harfler Listesi.:")
for k in L:
    if k in 'aeıioöuü ':
        L.remove(k)
        #sesli harfi listeden sil
    #döngü sonu

print (L) #listeyi yaz