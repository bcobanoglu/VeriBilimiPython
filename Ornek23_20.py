'''
Örnek 23.20: Çizilen bir kosinüs grafiğin, ‘cosFigure.png’ ismi ile proje dosyası
ile aynı klasörde saklayan programı kodlayınız.
'''
#Program dosyası adı: Ornek23_20.py
#Grafik dosyası adı: cosFigure.png
import matplotlib.pyplot as plt
import numpy as np
#Kosinüs dalgası
x = np.arange(0, 10, 0.1)
y = np.cos(x)
plt.plot(x, y,'b--')
plt.savefig('cosFigure.png')
plt.show()