'''
Örnek 24.1: Seaborn ‘flights’ veri setini kullanarak yıllara göre ‘Mayıs’ ayında
uçan yolcu sayısını çizgi grafiği şeklinde gösteren programı kodlayınız.
'''
import matplotlib.pyplot as plt
import seaborn as sns
df = sns.load_dataset("flights")
print(df)
ucus = df.pivot("year", "month", "passengers")
print(ucus)
sns.lineplot(data=ucus["May"])
plt.show()