'''
Örnek 23.15:
2012-2020 yılları arasındaki aktif Facebook kullanıcı sayısını gösteren tabloyu
nokta (scatter) ve çizgi (plot) grafikleri ile birlikte gösteriniz
'''
# %%
import numpy as np
import matplotlib.pyplot as plt
yil = np.arange(2012, 2021)             #2021 dahil değil
kSay = [1056, 1228, 1393, 1591, 1860, 2129, 2320, 2498, 2797]
plt.scatter (yil, kSay, color='gray')   #nokta koy
plt.plot (yil, kSay)                    #çizgi çiz
#Alternatifi: plt.plot (yil, kSay, '-o')

plt.xlabel('(Yıl)')                     #x ekseni etiketi
plt.ylabel('(Milyon)')                  #y ekseni etiketi
plt.title('Facebook aktif kullanıcı sayısı')
plt.show()

# %%
