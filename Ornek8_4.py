'''
Örnek 8.4 (Zar Oyunu):
Kullanıcının girdiği sayı kadar (1 ile 6 arasında rastgele sayı üreten) zar atan
ve gelen zarların gelme sayısını (sıklığını) histogram grafiği şeklinde ekranda
gösteren programı kodlayalım
'''
from random import *
def zarAt(n):
    print ("Gelen Zarlar:")
    for _ in range(n): #n kez
        zar = randint(1,6) #zar at
        print (zar, "*" * zar)

#Ana program
n = int(input("Zar atış sayısı.:"))
zarAt(n)