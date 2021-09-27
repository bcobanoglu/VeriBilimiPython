'''
Örnek 21.10: Bir ‘a’ matrisinin 1. satırı ile son sütunu hariç kalan bölgesini
(dilimleyerek) almak için aşağıdaki kod yazılabilir:
'''
import numpy as np
a = [[1,2,3],
    [4,5,6],
    [7,8,9]]
b = np.array(a)
print(b[1:,:-1])