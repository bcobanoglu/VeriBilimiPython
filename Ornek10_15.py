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

