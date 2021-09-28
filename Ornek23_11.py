'''
Örnek 23.11:
2010-2020 yılları arasında Türkiye karayollarında gerçekleşen ölümlü,
yaralanmalı trafik kazası sayılarını iki farklı grafik halinde gösteren programı
kodlayınız.
'''
import numpy as np
import matplotlib.pyplot as plt
#Yıllara göre gerçekleşen ölümlü ve yaralanmalı trafik kazaları
yil = np.arange(2010, 2021) #2021 dahil değil
yarali = [211496, 238074, 268079, 274829, 285059, 304421, 303812, 300383,
307071, 283234, 226266]
olumlu = [4045,3835,3750,3685,3524,7530,7300,7427,6675,5473, 4866]
#1.grafik
plt.subplot (2,1,1) #211 bitişik de yazılabilir: 2 satır ve 1 sütuna böl, 1.satıra şekli yerleştir
plt.plot(yil, yarali, 'b', label= 'yaralanmalı kazalar') #1. grafik:mavi
#2.grafik
plt.subplot (2,1,2) #212 bitişik de yazılabilir: 2 satır ve 1 sütuna böl, 2.satıra şekli yerleştir
plt.plot(yil, olumlu, 'r-.', label= 'ölümlü kazalar') #2. grafik:kırmızı
plt.legend() #etiketleri yerleştir
plt.suptitle("Trafik kazaları") #Ortak başlık
plt.tight_layout() #sıkışık grafikleri ayrıştır
plt.xlabel('Yıllar')
plt.show() #grafiği ekranda göster