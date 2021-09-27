'''
Örnek 21.8. (Transpoze):
Bir matrisin satırları ile sütunlarını yer değiştiren programı yazınız.
'''
import numpy as np
A=[[0, 2, 3, 4],
[5, 0, 6, 7],
[8, 9, 0, 1]]
#Önce liste diziye dönüştürülür
d = np.array(A)
#Sonra transpozesi alınır
print("Transpozesi:\n",d.T)