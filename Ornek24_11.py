'''
Örnek 24.11. (Covid-19 ölüm oranları): https://www.worldometers.info/
coronavirus/ adresinden 15.02.2021 tarihi itibari ile alınan güncel covid-19
bulaşıcı hastalık verileri (ülke adları, nüfusları, vaka, test ve ölüm sayıları)
bilgisayarda ‘covid.xls’ ismi ile tablo şeklinde kaydedilir
'''
__author__ = "Bulent Cobanoglu"
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
tablo = pd.read_excel("covid.xlsx") #excel dosyasını oku
df = pd.DataFrame(tablo)
#Veri çerçevesinin her bir alanını Numpy dizisine dönüştür
ulke = df["Ülke"].to_numpy()
olum = df["Vefat"].to_numpy()
vaka = df["Vaka"].to_numpy()
sns.barplot(ulke,olum)
plt.ylabel("Covid-19 Ölümleri (bin)")
#Her bir sütun üzerine ölüm rakamlarını yazdırma
for i,data in enumerate(olum):
    plt.text(x=i-0.5 , y=data+1, s=f"{data}")
plt.show()
