'''
Örnek 21.2. (3D >> 2D >> 1D dönüşüm):
Üç boyutlu bir dizi tanımlayıp bu diziyi sırası ile iki ve tek boyutlu diziye
dönüştüren programı yazınız.
'''
import numpy as np
#Üç boyutlu bir c3 dizisi tanımlandı
c3 = np.array([[[ 0, 1, 2],
[ 3, 4, 5],
[ 6, 7, 8]],
[[ 9, 10, 11],
[12, 13, 14],
[15, 16, 17]],
[[18, 19, 20],
[21, 22, 23],
[24, 25, 26]]])
print ("3*9 elemanlı iki boyutlu diziye dönüştü")
c2 = c3.reshape((3,9)) #c3 matrise dönüştü
print (c2)
print ("27 elemanlı tek boyutlu diziye dönüştü")
c1 = c2.ravel() #c2 vektöre dönüştü
print (c1)
print ("Dizi boyutları ve eleman sayıları")
print ("c3:", c3.shape) #(3, 3, 3)
print ("c2:", c2.shape) #(3, 9)
print ("c1:", c1.shape) #(27,)