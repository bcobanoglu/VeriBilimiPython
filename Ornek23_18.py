'''
Örnek 23.18:
0 ile 50 arasında N adet rasgele sayı üretilip bir dizide saklanacaktır. Dizide yer
alan her bir sayının kaç kez tekrar ettiğini (sıklığını) histogram grafiği şeklinde
çizen programı yazınız.
'''
import matplotlib.pyplot as plt
import numpy as np
n=25
np.random.seed(0)
x=np.random.randint(0,10,n)
print(x)
plt.hist(x,bins=n)
plt.yticks(np.arange(1,10))
plt.xticks(x)
plt.ylabel("Sıklık")
plt.xlabel("Random Numbers")
plt.title("Histogram grafiği")
plt.show()