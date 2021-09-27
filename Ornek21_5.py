'''
Örnek 21.5: A dizisinin elemanlarını, ters sırada B dizisine kopyalayan ve
ekranda gösteren programı yazınız
'''
import numpy as np
A = np.arange (7) #A dizisi (0-6)
print (A)
B = A [::-1] #B dizisi: A dizisinin tersi
print(B)