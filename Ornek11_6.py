'''
Örnek 11.6:
Önce bir ‘s’ sözlüğü tanımlayalım. Sonra bu sözlüğe eleman ekleme ve silme
işlemlerinin nasıl gerçekleştirilebileceğini basit bir uygulama ile gösterelim.
'''

#mevcut sözlük yapısı
s = {1:"a",2:"b",3:"c",4:"d",6:"f"}
#sözlükten eleman silelim
s.pop(1)    #anahtar değeri 1 olan elemanı sil
s.pop(3)    #anahtar değeri 3 olan elemanı sil
print (s)   # {2: 'b', 4: 'd', 5: 'e'}
#şimdi sözlüğe yeni eleman ekle
s[8] = "g"
print (s)   #{2: 'b', 4: 'd', 6: 'f', 8: 'g'}