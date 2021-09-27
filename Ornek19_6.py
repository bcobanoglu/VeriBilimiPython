'''
Örnek 19.6:
Şimdi verilen bir listeyi heap yapısına dönüştüren ve öbeğe (heap) eleman
ekleme ve silme işlemlerini gerçekleştiren programı kodlayalım.
'''
import heapq as hp
import binarytree as bt
li = [5, 7, 9, 1, 3, 11, 6]
#listeyi heap yapısına dönüştürelim
hp.heapify(li)
print ("Heap veri yapısı:")
print (list(li))
#heap yapısına eleman ekle
hp.heappush(li,4)
#heap yapısından eleman sil
hp.heappop(li)
#heap yapısının son halini göster
print ("push/pop işleminden sonra:")
print (li)
#şimdi de ağaç şeklinde ekrana basalım
agac = bt.build(li) #tree şekline dönüştür
print ("Ağaç gösterim:\n", agac)