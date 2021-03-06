'''
Örnek 24.10: Bir ürünün yıllara göre satış miktarını gösteren programı trend
eğrisini çizdirerek kodlayınız.
'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
tarih=[2019, 2020, 2021, 2022, 2023, 2024, 2025]
df=pd.DataFrame({'Yıl':tarih,'satış':[10,25,35,33,41,45,59]})
sns.set()                               #arka plana seaborn ızgarasını yerleştirir
sns.lmplot(x='Yıl', y='satış', data=df) #grafiği çiz
plt.show()