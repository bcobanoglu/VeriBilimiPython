'''
Ornek 8.12: Yığmalı toplama ve çarpma işlemi
'''
from itertools import accumulate
import operator

liste = [1,2,3,4,5,6,7,8,9,10]
#alternatifi: liste=range(1,11)

toplama = accumulate(liste)
print (list(toplama))

#çarpma operatörü: operator.mul
carpma=accumulate(liste,operator.mul)
print (list(carpma))