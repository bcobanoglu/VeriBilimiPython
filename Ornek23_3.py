'''
Örnek 23.3:
2012-2020 yılları arasındaki aktif Facebook kullanıcı sayılarını gösteren tabloyu
dikey grafik ile gösteriniz. (Veri Kaynağı: www.statista.com)
'''
import numpy as np
import matplotlib.pyplot as plt
yil = ('2012','2013','2014','2015','2016','2017','2018','2019', '2020')
x = np.arange(len(yil))
#kSay: Kullanıcı sayısı (milyon)
kSay = [1056, 1228, 1393, 1591, 1860, 2129, 2320, 2498, 2797]
plt.bar (x, kSay, align='center', color='black') #dikey çubuk grafiği
plt.xticks(x, yil) #X eksenindeki her bir değere karşılık gelen yıl değerini yerleştir.
plt.xlabel('(Yıl)') #x ekseni etiketi
plt.ylabel('(Milyon)') #y ekseni etiketi
plt.title('Facebook aktif kullanıcı sayısı')
plt.show()