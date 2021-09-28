'''
Örnek 24.9: Seaborn kütüphanesinin ‘tips’ test veri setindeki değerlerin
korelasyon matrisini heatmap() fonksiyonu ile gösteriniz.
'''
import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('tips')
#ısı haritası
sns.heatmap(df.corr(),annot=True,center=1)
print (df.corr())   #korelasyonu verir
plt.show()          #şekli göster