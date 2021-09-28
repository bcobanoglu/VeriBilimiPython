'''
Örnek 23.16: Yaş gruplarına ve cinsiyete göre alkol tüketim oranlarını yığın
çubuk grafikleri ile birlikte gösteriniz.
'''
import matplotlib.pyplot as plt
#Alkol kullanım yüzdelerini gösteren veri setleri
veriSeti1 = [21, 31, 27, 26, 23, 11, 4]
veriSeti2 = [6, 10, 7, 5, 3, 1, 1]
yasGrubu = ['15-24', '25-34', '35-44', '45-54', '55-64', '65-74', '75+']
pos = list(range(7))
#veri aralığı
plt.bar(pos, veriSeti1, color='blue') #erkekler:mavi
plt.bar(pos, veriSeti2, color='purple') #kızlar:pembe
plt.xticks(ticks=pos, labels=yasGrubu)
plt.title('Alkol kullanma oranları (%)')
plt.xlabel('Yaş Grubu')
plt.ylabel('Frekans')
plt.legend(['Erkek', 'Kız'], loc='upper right')
plt.show()