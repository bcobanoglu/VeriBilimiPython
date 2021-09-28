'''
Örnek 24.5: Girintili kutu grafiği: Seaborn ‘tips’ veri setini kullanarak boxplot()
ve stripplot() grafiklerini yatay eksende çizdiriniz.
'''
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="whitegrid")                      #çizim arka planına ızgara yerleştirir
df = sns.load_dataset('tips')                   #seaborn 'tips' veri setini yükle
sns.boxplot(x='tip', y='day', notch=1, data=df) #yatayda girintili kutu grafiği çiz.
#verilerin dağılımını cinsiyete (sex) göre listele
sns.stripplot(x='tip', y='day', jitter=False, hue="sex",data=df)
plt.show()                                      #şekli göster