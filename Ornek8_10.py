'''
Örnek 8.10:
e sayısı veya Euler sayısı aşağıdaki sonsuz toplama eşittir:
Buradaki n! ifadesi, n faktöriyeli temsil etmektedir: n! = 1 × 2 × 3 × ... × n. Bu
seriyi hesaplayan programı kodlayalım
'''
#Euler serisi
from math import *
def yaklasik_e(terim):
    return fsum(1 / factorial(n) for n in range(terim))
#Ana program
for i in range (6):
    print (i,"!=", yaklasik_e(i))