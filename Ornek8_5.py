'''
Örnek 8.5 (Yazı-Tura Oyunu):
Yazı-tura atışı yapan programı kodlayalım.
'''
from random import *
print("Yazı mı? Tura mı?")
#random 0-1 arasında kesirli sayı üretir ve
#round ile de bu sayı yuvarlatılır.
yT = round(random())
if yT==0 :
    print ("Tura")
else:
    print ("Yazı")