'''
Örnek 21.7. (Matris toplamı ve çarpımı):
İki matrisin toplam ve çarpım sonucunu ekranda gösteren programı yazınız.
'''
import numpy as np
a = np.array ([[3,5,9], [4,6,1], [1,8,2]])
b = np.array ([[1,0,3], [4,5,7], [2,3,6]])
cC = np.matmul(a,b) #matris çarpımı
cT = np.add(a,b) #matrisi toplamı
print ("a*b =\n",cC)
print ("a+b =\n",cT)