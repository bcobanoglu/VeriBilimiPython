'''
Örnek 24.3:
Bir tavla zarının atılması ve üste gelen zarın gözlenmesi deneyinde her bir
zarın kaç kez tekrar ettiğini (sıklığını) histogram grafiği şeklinde çizen programı
displot() /distplot() ile kodlayınız
'''
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
n = 20                                  #zar atılma sayısı
zar = np.random.randint(1, 7, n)        #sıklık (Frekans)
np.random.seed(0)
print(zar)
#Eşdeğer çizimler
ax1= sns.distplot(zar, rug=True, hist=True, kde=True,
                bins=n, color="black")  #soldaki grafik
ax2 = sns.displot(zar, kind = "hist", kde=True, bins=n,
            fill=False, color ='gray')  #sağdaki grafik
ax1.set(xlabel="Zarlar", ylabel="Sıklık")
ax2.set(xlabel="Zarlar", ylabel="Frekans")
plt.show()