'''
Örnek 23.19: İki adet zar, 1000 kez atıldığında gelen değerleri histogram grafiği
şeklinde çizdiren programı kodlayalım.
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#iki zarı 1000 defa attığımızda gelme durumları
zar_1 = np.random.randint(1, 7, 1000)
zar_2 = np.random.randint(1, 7, 1000)
df = pd.DataFrame({
    'zar_1': pd.Series(zar_1),
    'zar_2': pd.Series(zar_1) })
print (df) #değerleri ekrana yaz
ax = df.hist(bins=6) #histogram grafiği
plt.show() #grafiği göster