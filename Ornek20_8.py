'''
Örnek 20.8: Bir veri kümesinin medyan, mod, varyans, ortalama mutlak sapma
ve standart sapmasını hesaplayan, aynı zamanda küçükten büyüğe sıralayan
programı kodlayalım.
'''
import numpy as np
import pandas as pd
dizi = [3, 10, 8, 10, 5, 4, 8, 4, 8]
df=pd.DataFrame(dizi, columns=['a'])
#Ortalamalar:
print ("medyan.:",np.median(dizi))  #ortadaki değer
print ("ortalama.:", np.mean(dizi)) #aritmetik ortalama
#Standart Sapma:
print ("Standart Sapma.:", np.std(dizi))
print ("Varyans karekökü.:", np.sqrt((np.var(dizi))))
#varyansın karekökü
print ("Mod.:", *df['a'].mode())    #en sık tekrar eden veri
#Ortalama mutlak sapma
print ("Mutlak Sapma.:",df['a'].mad())
#’a’ sütununa göre küçükten büyüğe sırala
print ("Sırala.:\n", df.sort_values(by="a"))