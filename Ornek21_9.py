'''
Örnek 21.9. (Matris elemanlarını sıralama):
Bir matrisin elemanlarını küçükten büyüğe doğru yan yana ekrana yazan
programı kodlayınız
'''
import numpy as np
a = np.array ([[3,5,9],
[4,6,1],
[7,8,2]])
aS = np.sort(a, axis = None)
print ("Sıralı hali.:", aS)
print ("Ters sıra.:", list(reversed(aS)))