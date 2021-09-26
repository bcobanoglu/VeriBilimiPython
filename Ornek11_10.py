'''
Örnek 11.10:
0’dan 10’a kadar ki çift sayıları ve karelerini sözlük yapısı şeklinde ekrana
yazan programı kodlayınız.
'''
#0-10 arası çift sayı üreteci: c
c = [x for x in range (0,12,2)]
#{çift sayı : karesi} sözlüğü: t
t = {x: x**2 for x in c}
print (t)