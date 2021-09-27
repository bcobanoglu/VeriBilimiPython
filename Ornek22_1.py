'''
Örnek 22.1. (İller ve plakaları): İlleri ve plakalarını pandas serisi şeklinde
tanımlayıp ekranda gösteren programı kodlayınız.
'''
import pandas as pd
#indis değerleri
plaka = [1, 19, 66, 6, 55, 16, 31, 53]
#veriler
il = ['Adana', 'Çorum', 'Yozgat', 'Ankara', 'Samsun','Bursa', 'Hatay', 'Rize']
# Seri indis (plaka) değerlerini, il listesi ile eşleyelim.
il = pd.Series(il, index = plaka)
print (il)