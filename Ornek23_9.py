'''
Örnek 23.9. (Çizgi grafiği): Düz ve kesikli çizgi grafiklerini ve yazılarını
aşağıdaki gibi gösteren programları kodlayınız
'''
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2, 50)
#farklı çizim stilleri
plt.plot(x, x )
plt.plot(x, x**2, 'g-.')
#Çizim yazıları
plt.xlabel('x ekseni')
plt.ylabel('y ekseni')
plt.title("Çizgi grafikleri")
#oklar ve yazıları
plt.annotate('Kesikli', xy=(1.5,2.4), xytext=(1.0,2.5),
    arrowprops = { 'arrowstyle' : ' - > ', 'lw':2, 'color':'green'})
plt.annotate ( 'Doğrusal',xy=(0.45,0.5), xytext=(0.01,0.5),
    arrowprops=dict(arrowstyle='->',lw=1, color='blue') )
plt.show()