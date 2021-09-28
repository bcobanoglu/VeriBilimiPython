'''
Örnek 24.2: Önceki bölümdeki örneklerde verilen 2012-2020 yılları arasındaki
aktif Facebook kullanıcı sayısını gösteren çizgi grafiğini relplot() ile çizdiriniz.
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
yil = np.arange(2012, 2021)
kSay = [1056, 1228, 1393, 1591, 1860, 2129, 2320, 2498, 2797]
df=pd.DataFrame({'Yıl':yil, 'Users':kSay }) #df tablosuna dönüştürüldü
ax= sns.lineplot(data=df, x="Yıl", y="Users")
#Eşdeğeri: ax= sns.relplot( data=df, x="Yıl", y="Users", kind="line")
ax.set(xlabel='Yıl', ylabel='Kullanıcı Sayısı(Milyon)',
title='Facebook Kullanıcıları')
plt.show()