'''
Örnek 22.4: Bir veri setinde araçlar ve hızları tablo hâlinde tutulmaktadır. Bu
araçların ortalama (mean) hızlarını ekrana yazdıran programı kodlayalım
'''
import pandas as pd
#veri seti
df = pd.DataFrame({'Araba': ['Ferrari', 'Bmw', 'Bmw', 'Ferrari'],
'Hızı': [380., 370., 260., 300.]})
#ortalama hızları
print (df.groupby(['Araba']).mean())
