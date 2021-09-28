'''
Örnek 23.6. (Pasta grafiği): Daha önce çubuk grafik ile çizdirdiğimiz il
nüfuslarını, pasta (pie) dilimi grafiği şeklinde çizdirelim
'''
import numpy as np
import matplotlib.pyplot as plt
il = ('Bursa', 'Erzurum', 'Erzincan', 'Kocaeli', 'Bolu')
x = np.arange(len(il))
nfsY = [3056120, 762062, 234747, 1029650, 316126]
#Pasta dilimi renk sırası
renk_dizisi = ['gold', 'gray', 'red', 'magenta', 'lightblue']
secilen_dilim = (0, 0, 0, 0, 0.2) #Son dilim secildi
# Pasta dilimi çizimi
plt.pie(nfsY, explode=secilen_dilim, labels=il, colors=renk_dizisi,
autopct='%1.1f', shadow=True)
plt.title('İller ve Nüfus Oranları')
plt.show()