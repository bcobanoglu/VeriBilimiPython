'''
Örnek 22.6: Bir veri setinde arabalar ve hızları tablo hâlinde yandaki gibi
tutulmaktadır. Bu veri setinde kayıp veri var mı? Var ise bu kayıp veriyi silen
veya yerine başka değerler koyan programı kodlayalım
    Araba   Hızı
  Ferrari  380.0
      Bmw  370.0
      Bmw  260.0
    Honda  NaN
  Ferrari  300.0
    Honda  NaN
'''
import pandas as pd
#veri seti
df = pd.DataFrame({'Araba': ['Ferrari', 'Bmw', 'Bmw', 'Honda', 'Ferrari', 'Honda'],
                    'Hızı': [380., 370., 260., None, 300., None]})
#Kayıp veri var mı? test edelim:
if df.isna().any: #True ise
    print ("Kayıp veri var...")
else:
    print ("Kayıp veri yok...")
#Verilerin dağılımı hakkında istatiksel bilgiler alalım;
print(df.describe(include = "all"))
#Kayıp verileri mean() ile dolduralım
yeniDf = df.fillna(df.mean())
print(yeniDf)