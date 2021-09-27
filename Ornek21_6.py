'''
Örnek 21.6:
Bir 4*4 birim matrisi oluşturup ekranda gösteren ve bu matrisin izini hesaplayan
programı yazınız.
'''
import numpy as np
d = np.eye(4, dtype=int)
print (d)
print ("Matrisin izi:")
print (np.trace(d))