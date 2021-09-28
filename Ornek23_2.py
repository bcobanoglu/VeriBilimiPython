'''
Örnek 23.2:
2019 yılı nüfus sayımı verilerine göre Bursa, Erzurum, Erzincan, Kocaeli ve Bolu
illerinin yaklaşık nüfusu sırası ile ‘3_056_120, 762_062, 234_747, 1_029_650,
316_126’dir. Bu illerin nüfusunu yatay çubuk (barh) grafik şeklinde gösteren
programı yazınız.
'''
import numpy as np
import matplotlib.pyplot as plt
il = ('Bursa', 'Erzurum', 'Erzincan', 'Kocaeli', 'Bolu')
x = np.arange(len(il))
nfsY = [3056120, 762062, 234747, 1029650, 316126]
plt.barh(x, nfsY, color='blue') #yatay eksen ve çubuk rengi mavi seçildi
plt.yticks(x, il)
plt.xlabel('Nüfus(Milyon)')
plt.title('İl Nüfusları')
plt.show()