'''
Örnek 11.3:
Aşağıdaki programda verilen küme işlemlerini ekran çıktısını dikkate alarak
anlamaya çalışınız.
'''
meyve = {'elma', 'muz', 'nar', 'erik', 'hurma'}
print ('armut' in meyve) # False
print ('nar' in meyve) #True
a = set('abracadabra')
b = set('abc')
c1 = {x for x in a if x not in b}
print (c1) #{'d', 'r'}
c2 = a.symmetric_difference(b) #c1'in eşdeğeri
print (c2)
print (a^b) #c1 ve c2 eşdeğeri
meyve.add('üzüm')
#küme eleman sayıları:
print (len(meyve), len(a))