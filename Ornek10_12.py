'''
Örnek 10.12:
1’den 100’e kadar sayıların toplamını lambda ve reduce() fonksiyonu ile
kodlayalım.
'''
from functools import reduce
liste = list(range(1,101)) #1-100 arası sayıları tutan liste
toplam = reduce(lambda x, y: x+y, liste)
print (toplam)