'''
Örnek 23.5. (3D=n*2D): Bir önceki örnekteki 3 boyutlu çizim şeklini yandaki
gibi de çizdirebiliriz. Aslında 3 boyutlu bir dizi; n adet 2 boyutlu bir dizinin
birleşimidir. Buna göre bir 2D bar (çubuk) grafiği aşağıdaki gibi bir for döngüsü ile 3D bar grafiğine
dönüştürülebilir:
'''
import matplotlib.pyplot as plt
import numpy as np
kSay = [1056, 1228, 1393, 1591, 1860, 2129, 2320, 2498, 2797] #Kullanıcı sayısı
fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')
for c, z in zip(['r', 'g', 'b', 'y', 'c'], [8, 6, 4, 2, 0]):
    x = np.arange(9)
    y = kSay
    ax.bar(x, y, z, zdir='y', color=c)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()