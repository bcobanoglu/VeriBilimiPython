'''
Örnek 24.8.
2015-2021 yılları arasında ‘Hayvanat Bahçesini’ ziyaret eden kişi sayısını
sezona (yaz, kış, bahar) göre gruplandırarak poinplot() ile çizdiriniz.
'''
import pandas as pds
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
#Hayvanat Bahçesi Ziyaretçi Sayısı
ziyaretci = {"Yıl":[2015, 2016, 2017, 2018, 2019, 2020, 2021],
            "Kişi Sayısı(Bin)":[100, 150, 300, 400, 250, 210, 180],
            "Sezon":["Yaz", "Yaz", "Kış", "Bahar", "Yaz", "Kış","Bahar"]
            }
sns.set(style="darkgrid")
df = pds.DataFrame(ziyaretci)
print(df)
#Grafiği çiz
sns.pointplot(x="Sezon", y="Kişi Sayısı(Bin)",data=df, estimator=np.median)
plt.title("Hayvanat Bahçesi Ziyaretçi Sayısı")
plt.show()