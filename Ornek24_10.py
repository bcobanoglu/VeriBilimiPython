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


#Alkol kullanımı ile araç kazaları arasında güçlü bir bağ vardır. Örneğin car_crashes veri kümesini ele alalım
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
arac_kazalari = sns.load_dataset('car_crashes')
sns.lmplot(x='alcohol', y='total', data=arac_kazalari) #grafiği çiz
plt.show()
