'''
Örnek 21.12: İki matrisi (a, b) birleştirerek yeni matrisler (c, d) elde eden
programı kodlayınız
'''
import numpy as np
a = np.array([[1,2,3],
            [4,5,6]])
b = np.array([[7,8,9],
            [0,1,0]])
print ("Yatay eksende birleştirme:")
c = np.hstack((a,b))
print (c)
print ("Dikey eksende birleştirme:")
d = np.vstack((a,b))
print (d)