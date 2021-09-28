'''
Örnek 23.10: Önceki örneklerdeki 2012-2020 yılları arasındaki aktif Facebook
kullanıcı sayısını gösteren tabloyu adım (step) grafiği ile gösteriniz
'''
import numpy as np
import matplotlib.pyplot as plt
yil = np.arange(2012, 2021)
kSay = [1056, 1228, 1393, 1591, 1860, 2129, 2320, 2498, 2797]
#'g^': üçgen yerine 'r*': Yıldız, 'cs':kare, 'C0o': daire şekilleri de kullanılabilir
plt.plot(yil, kSay, 'g^', alpha=0.5 )
plt.step(yil, kSay,label='[2012-2020]')
plt.legend() #Etiketi (label) sağ-üst köşede göster
plt.title('Facebook aktif kullanıcı sayısı')
plt.ylabel("Milyon")
plt.show()