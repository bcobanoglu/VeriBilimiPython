'''
Örnek 23.12:
Aynı pencere içerisine hem sinüs hemde kosinüs grafiklerini çizen programı
kodlayalım.
'''
# %%
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,10,100)
fig, ax = plt.subplots()
ax.plot(x,np.sin(x), '-b', label='Sinüs')
ax.plot(x,np.cos(x), '--r', label='Kosinüs')
ax.axis('equal')
ax.set_title('-Sinüs-Kosinüs Grafikleri')
ax.legend()
# %%
fig.show()