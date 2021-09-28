'''
Örnek 23.14:
2012-2020 yılları arasındaki aktif Facebook kullanıcı sayısını gösteren tabloyu
nokta (scatter) grafiği ile gösteriniz.
'''
# %%
import numpy as np
import matplotlib.pyplot as plt
yil = np.arange(2012, 2021) #2021 dahil değil
kSay = [1056, 1228, 1393, 1591, 1860, 2129, 2320, 2498, 2797]
#nokta grafiği farklı şekil ve renklerde olabilir
plt.scatter(yil, kSay,
        c='gray',           #simge iç rengi
        linewidths = 2,     #çizgi kalınlığı
        marker ="^",        #simge: üçgen
        edgecolor ="red",   #kenar çizgi rengi
        s=80                #simge boyutu
        )

plt.xlabel('(Yıl)')         #x ekseni etiketi
plt.ylabel('(Milyon)')      #y ekseni etiketi
plt.title('Facebook Aktif Kullanıcı Sayısı')

plt.show()                  #grafiği ekranda göster
#Visual studio code için Shift + Enter ile çalıştırabilirsiniz..
