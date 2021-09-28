'''
Örnek 24.12: Bir önceki örneği ‘covid’ modülü ile kodlayarak güncel verileri
alalım.
'''
import matplotlib.pyplot as plt
import seaborn as sns
from covid import Covid
import pandas as pd
cvd = Covid() #varsayılan veri tabanı seçildi
df = pd.DataFrame(cvd.get_data())
top10=df.head(10) #güncel ilk 10 ülkeyi listele
print(top10)
x = top10.country #ülke adları
y1 = top10.active #aktif vaka sayıları
y2 = top10.deaths #vefat sayıları
y3 = top10.recovered #iyileşen hasta sayıları
sns.barplot(x, y2, data=top10) #ülke adı-vefat sayılarını göster
plt.title("Vefat Sayıları")
plt.show()