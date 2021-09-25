'''
Örnek 8.11 (Gregory – Leibniz serisi ile Pi Sayısı Hesabı):
'''
#Leibniz serisi
from math import *
n = 1000
Pi = 0
for k in range(0, n):
    Pi = Pi + 4*(pow(-1,k)/(2*k+1))
print ("Pi Sayısı:", Pi)