'''
Örnek 24.4. (İki değişkenli grafik): Seaborn ‘flights’ veri setini kullanarak
yıllara göre uçan yolcu sayısını jointplot() ile regresyon (reg) grafiği şeklinde
gösteren programı kodlayınız.
'''
import matplotlib.pyplot as plt
import seaborn as sns
df = sns.load_dataset("flights")
sns.jointplot(data=df,
            x="passengers", y="year",
            kind="reg")
plt.show()