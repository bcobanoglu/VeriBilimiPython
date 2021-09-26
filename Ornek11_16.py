'''
Örnek 11.16: Aşağıdaki tabloyu sözlük yapısını kullanarak oluşturup ekranda
gösteriniz.
ad yaş bölüm
a 34 MUH
b 25 CEO
c 44 ARGE
d 54 MUH
e 19 ARGE
'''
#pandas paketini import et ve pd ismi ile programda kullan
import pandas as pd
import numpy as np
#iç içe sözlük yapısı ile tablo oluşturulabilir
personel = {
'ad' : ["a", "b", "c", "d", "e"],   #ad sütunu
'yas' : [34, 25, 44, 54, 19],       #yas sütunu
'bolum': ["MUH", "CEO", "ARGE", "MUH", "ARGE"] }
#Sözlüğü dataframe nesnesine dönüştür ve ekranda göster
tablo = pd.DataFrame(personel)
print (tablo)