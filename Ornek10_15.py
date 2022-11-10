'''
VERİ BİLİMİ İÇİN PYTHON
Örnek 10.15:
Bir string listesini karakter listesine iç içe liste şeklinde dönüştüren programı
map() fonksiyonu ile kodlayalım.
'''
stringListe = ['ali', 'bade', 'can', 'berat']
karakter = map(list, stringListe)
print(list(karakter))

"""
Soru: Peki tersi işlemi nasıl  gerçekleştirebiliriz?
Yani birden fazla karakter listesini tek bir string listesine nasıl dönüştürebiliriz?
"""
k0_list = ['a', 'l', 'i']
k1_list = ['b', 'a', 'd', 'e']
k2_list = ['c', 'a', 'n']
k3_list = ['b', 'e', 'r', 'a', 't']
str_list = map(ambda x,y,z,t: x+y+z+t, k0_list,k1_list,k2_list,k3_ilst)
print(list(str_list))
