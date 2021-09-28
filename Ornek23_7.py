'''
Örnek 23.7. (Donut Grafiği): Şimdi de bir önceki örnekteki pasta (pie) dilimini
donut şeklinde gösterelim
'''
import numpy as np
import matplotlib.pyplot as plt
il = ('Bursa', 'Erzurum', 'Erzincan', 'Kocaeli', 'Bolu')
x = np.arange(len(il))
nfsY = [3056120, 762062, 234747, 1029650, 316126]
rnk = ['gold', 'gray', 'red', 'magenta', 'lightblue']
sec1 = (0, 0, 0, 0, 0.2) #Son dilim secildi
plt.pie(nfsY, explode=sec1, labels=None, colors=rnk, autopct='%1.1f')
#Donut Çizimi: plt.Circle ((x,y), donut kalınlığı, iç dolgu rengi)
donut = plt.Circle( (0,0), 0.7, color='white')
plt.gcf().gca().add_artist(donut)
# il isimlerini sağ üst köşeye taşıyalım
plt.legend(il, fontsize = 10, loc = 'upper right')
plt.axis('equal') #Veri aralığını genişleterek ölçekleri eşitler
plt.title('İller ve Nüfus Oranları')
plt.show()