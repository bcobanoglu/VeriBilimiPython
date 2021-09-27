'''
Örnek 22.2: Bir Numpy dizisini Pandas veri çerçevesine dönüştüren programı
kodlayınız
'''
import numpy as np
import pandas as pd
dizi = np.array([['Ali',1996,2016],['Veli',1974,1997],['Bade',2002,2020]])
df = pd.DataFrame(dizi, columns = ['Ad','D.Tarihi','İş Başı'])
print(df)