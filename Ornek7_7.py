'''
Örnek 7.7:
Örnek 7.3’te verilen faktöriyel hesaplayan programı lambda ifadeleri ile
kodlayalım.
'''
fakt = lambda n: n * fakt(n-1) if n else 1
print (fakt(5))