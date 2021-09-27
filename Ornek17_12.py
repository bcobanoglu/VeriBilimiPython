'''
Örnek 17.12. to_csv: Bir sözlük veri yapısını pandas veri çerçevesine
dönüştürüp ‘.csv’ formatında ‘veri.csv’ olarak kaydeden programı kodlayalım.
'''
import pandas as pd
veri = {'il' :['bursa','bolu','ordu'],
        'plk':[16, 14, 52 ]}
df = pd.DataFrame(veri) #dataframe'e dönüştür
df.to_csv('veri.csv')   #'veri.csv' dosyasında sakla
print (df[['il']])      #sadece il sütununu listele
