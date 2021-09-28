'''
Örnek 23.8: Aktif Facebook kullanıcı sayısını gösteren tabloyu siyah-gri sütun
(brar) grafiği ile her bir çubuk üzerine text yerleştirerek yeniden çizdiriniz.
'''
import numpy as np
import matplotlib.pyplot as plt
yil = np.arange(2012, 2021) #2012-2020 yıl dizisi
kSay = [1056, 1228, 1393, 1591, 1860, 2129, 2320, 2498, 2797] #(milyon)
#Sütun grafiği: çerçeve rengi:siyah, iç rengi:açık gri
ax= plt.bar(yil, kSay, color="lightgray",edgecolor = 'black')
#Her bir çubuk üzerine kullanıcı sayısını yazdıralım
for p in ax:
    plt.annotate(p.get_height(), #text
    xy= (p.get_x() + p.get_width() / 2, p.get_height()),
    xytext = (0, 9),
    textcoords = 'offset points',
    ha = 'center', va = 'center')

plt.xlabel('(Yıl)') #x ekseni etiketi
plt.ylabel('(Milyon)') #y ekseni etiketi
plt.title('Facebook aktif kullanıcı sayısı')
plt.show() #grafiği ekranda göster