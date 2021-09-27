'''
Örnek 21.11. (Boolean dilimleme):
Bir veri kümesindeki ‘3’ten büyük değerleri alan programı kodlayınız.
'''
import numpy as np
a = [[1,2,3],
    [4,5,6],
    [7,8,9]]
#array'e dönüştü
b = np.array(a)
#3'ten büyük sayıları al
print(b[np.where((b>3))])