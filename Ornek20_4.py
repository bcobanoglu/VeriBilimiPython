'''
Örnek 20.4. (Kovaryans ve Korelasyon Hesabı):
x = [1, 2, 3, 4, 5, 6, 7, 8, 9] ve y = [1, 2, 3, 1, 2, 3, 1, 2, 3]
İki veri kümesinin hem kovaryansını hem de korelasyon katsayısını hesaplayan
programları kodlayalım
'''
from statistics import *
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [1, 2, 3, 1, 2, 3, 1, 2, 3]
#Kovaryans hesabı
print ("Kovaryans:", covariance(x,y))
#Korelasyon Katsayısı hesabı
print ("Korelasyon Katsayısı:",
correlation(x,y))