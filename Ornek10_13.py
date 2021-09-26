'''
Örnek 10.13:
1…100 arasındaki tam sayılardan oluşan bir listeden filter() fonksiyonu ile
tek sayıları filtreleyip yeni liste oluşturalım.
'''
liste = list(range(1,101)) #1-100 arası sayıları tutan liste
tekS= list(filter(lambda x: x%2!=0, liste))
print (tekS)
