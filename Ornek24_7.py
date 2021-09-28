'''
Örnek 24.7: Seaborn ‘tips’ veri setinin ‘size’ sütunundaki her bir değeri
‘countplot()’ sayım metodu ile çizdiriniz.
'''
import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('tips')

print(df.head(10))          #ilk 10 satırını listele
sns.countplot(df['size'])   #sayım grafiği ile 'size' alanını grafikleştir
plt.show()                  #şekli göster