'''
Örnek 24.6. Keman grafiği: Seaborn ‘tips’ veri setini kullanarak violinplot()
ve swarmplot() grafiklerini birlikte çizdiriniz.
'''
import seaborn as sns
import matplotlib.pyplot as plt
# çizim arka planına ızgara yerleştir.
sns.set(style="darkgrid")
#Seaborn ‘tips’ veri setini kullan
df = sns.load_dataset('tips')
#keman grafiğini ortasındaki çizgileri kaldırarak, kalın çizgilerle çiz
sns.violinplot(x='day', y='tip', inner=None, linewidth= 3, data=df)
#verilerin saçılımını cinsiyete göre siyah - beyaz renk paletinde göster
sns.swarmplot(x='day', y='tip', hue="sex", palette=["k","w"], data=df)
plt.show()      #şekli göster