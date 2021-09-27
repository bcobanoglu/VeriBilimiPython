'''
Örnek 21.3. (Matrise (1D >> 2D ) Dönüştürme):
“d= [1,2,3,4,5,6,7,8,9,10,11,12]” şeklindeki tek boyutlu diziyi 4*3 lük bir matrise
dönüştüren programı yazınız.
'''
import numpy as np
#Tek boyutlu d dizisi (1-12)
d = np.arange (1, 13)
# d dizisi 4*3 lük matrise dönüştü.
A = d.reshape(4,3)
print (A)