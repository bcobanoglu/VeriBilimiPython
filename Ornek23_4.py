'''
Örnek 23.4. (3 boyutlu Çubuk Çizimi): Bir önceki örnekteki 2012-2020 yılları
arasındaki aktif Facebook kullanıcı sayısını gösteren tabloyu 3 boyutlu grafik ile
gösteriniz. (Veri Kaynağı: www.statista.com)
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#2012-2022 yıl değerleri ‘period_range’ ile de oluşturulabilir
yil =pd.period_range(start="2012", end="2020",freq="Y")
#aktif Facebook kullanıcı sayıları
kSay = [1056, 1228, 1393, 1591, 1860, 2129, 2320, 2498, 2797]
x = y = np.arange(len(yil))
z = len(kSay)
#çizgi derinlikleri
dx = dy = np.ones(z)
dz = kSay
#Gri renkte 3 boyutlu yeni çizim çerçevesi tanımlandı ve ‘bar3d’ şekli çizdirildi
fig = plt.figure()
ax1 = fig.add_subplot(projection='3d')
ax1.bar3d(x, y, z, dx, dy, dz, color='grey')
ax1.set_xlabel('x ekseni')
ax1.set_ylabel('y ekseni')
ax1.set_zlabel('z ekseni')
plt.title("Aktif Facebook kullanıcıları")
plt.show()