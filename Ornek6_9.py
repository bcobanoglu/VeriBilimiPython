'''
Örnek 6.9:
Altın oranla birlikte bir Fibonacci serisinin 100’den küçük değerlerini veren
programı kodlayalım.
'''
print ("Fibonacci Serisi.:")
n = 100
a, b = 0, 1
while a < n:
    print (a, end=' ')
    a, b = b, a+b
print ("\nAltın oran.:", b/a)