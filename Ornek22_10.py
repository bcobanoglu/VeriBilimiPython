'''
Örnek 22.10: Bir ürünün yıllara göre satış miktarını gösteren programı
kodlayınız.
'''
import pandas as pd
#2020-2028 arası zaman serisi
tarih = pd.Series(pd.date_range("2020", periods=8, freq="Y"))
#Yıllara göre satış rakamları
df = pd.DataFrame(pd.Series([11,21,33,24,15,16,27,38],
index=tarih))
#sütun ismini ‘satış’ olarak değiştirelim
df.rename(columns = {list(df)[0]:'Satış'}, inplace=True)
print (df)
print ("2025 Yılı Satış Rakamı.:")
print (df["2025"]) #Sadece 2025 yılı satış rakamını listele