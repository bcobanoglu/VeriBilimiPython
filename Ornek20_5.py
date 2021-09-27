'''
Örnek 20.5. (Regresyon Analizi): Kodlab yayınevinden çıkan bir ‘Python’
kitabının yıllara göre satış rakamları aşağıdaki tabloda verilmiştir:
yil = [2001, 2002, 2003, 2004, 2005, 2006 ]
satis = [1, 2, 3, 4, 5, 6 ] #(*1000 adet)
Buna göre 2022 yılında bu ‘Python’ kitabının tahmini satış rakamı ?
'''
from statistics import *                #3.10 ve üzeri sürümler için
yil = [2001,2002,2003,2004,2005,2006]
satis = [1, 2, 3, 4, 5, 6]
b, a=linear_regression(yil,satis)
#2022 yılı tahmini satış rakamı:
y = round(a*2022+b)                      #y = a*x+b
print (y)