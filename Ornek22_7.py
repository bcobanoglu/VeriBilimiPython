'''
Örnek 22.7: İki farklı tabloyu (veri çerçevesini) birleştirip kayıp veriler yerine
sabit değerler yerleştiren programı kodlayalım
'''
import pandas as pd
df1 = pd.DataFrame({'a': ['foo', 'bar'], 'b': [1,2]})   #tablo 1
df2 = pd.DataFrame({'a': ['3', '4'], 'c': [6,7]})       #tablo 2
df3 = pd.merge(df1, df2, how='outer')                   #birleştirilmiş tablo
#Alternatifi: df3 = pd.concat((df1, df2))
print (df3)
print ("#NaN yerine farklı değerler yerleştir")
doldur = {'a': 0, 'b': 1, 'c': 2}
print (df3.fillna(value=doldur))