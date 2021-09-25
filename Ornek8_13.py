'''
Örnek 8.13: Farkı daha iyi anlamak için “1+1/2+1/4+1/8+1/16+1/32+1/64"
şeklinde verilen serinin toplamını bulan programı hem döngü hem de
‘accumulate’ fonksiyonu ile kodlayalım.
'''
from itertools import accumulate
Dizi = [1, 2, 4, 8, 16, 32, 64]
Fx= map(lambda x: 1/x, Dizi)
#map ile dizideki her elemana aynı işlem (1/x) uygulandı
print (list(accumulate(Fx)))