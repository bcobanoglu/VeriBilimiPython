'''
Örnek 23.13:
u1 = Sin(x) ve u2 = Cos(x) sinyalleri ile bu iki sinyalin toplamını aynı çerçeve
içerisine çizdiriniz
'''
# %%
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 10, 0.1) #0- 10 aralığında 0.1 adımlı değerler üretir.
u1 = np.sin(x) #1.sinyal
u2 = np.cos(x) #2.sinyal
ut = u1 + u2 #iki sinyalin toplamı
#2 satır, 1 sütundan oluşan 2 farklı çizim alanı tanımlandı
fig, (ax1, ax2) = plt.subplots(2, 1)
#sin ve cos grafiklerini aynı pencerede gösterelim
ax1.plot(x, u1, 'b', label= 'sinx') #mavi düz çizgi: sinx
ax1.plot(x, u2, 'r-.', label= 'cosx')#kırmızı kesikli çizgi:cosx
ax1.legend() #etiketleri yerleştir

#3. grafiği (toplamını) farklı pencerede gösterelim
ax2.plot(x, ut, label= 'sinx+cosx', linewidth=3)
#çizgi kalınlığı ‘linewidth’ özelliği ile ayarlanabilir.
ax2.legend( loc = 'upper right') #3.etiketi sağ üste yerleştir
ax2.set_xlabel('Zaman(s)') #x ekseni etiketini ayarla
# %%
fig.tight_layout() #sıkışık grafikleri ayrıştır
fig.show() #grafikleri göster