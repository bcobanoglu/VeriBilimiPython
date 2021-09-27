'''
Örnek 22.8: Bir veri setinde iller ve plakaları tablo halinde tutulmaktadır. Bu
veri setinin çift kayıtları içerip içermediğini sorgulayan ve bu çift kayıtlardan veri
setini temizleyen programı kodlayınız.
'''
import pandas as pd
#veri seti
veri = {'il' :['bursa','bolu','ordu', 'izmit', 'bolu'],
        'plk':[16, 14, 52, 41, 14 ]}
df = pd.DataFrame(veri) #dataframe nesnesine dönüştür
print (df) #listele
print ("Çift veri indisi.:", end='')
print (df.duplicated().sum()) #toplam çift kayıt sayısını yazdırır
#çiftlerden arındırılmış tabloyu listele
yTablo = df.drop_duplicates()
print(yTablo)