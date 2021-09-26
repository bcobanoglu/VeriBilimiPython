'''
Örnek 9.5:
Bir string metni içerisindeki ‘,’ virgül karakterlerinden ayrıştırarak listeye
dönüştüren programı kodlayalım.
'''
metin = "Bir ol. İri Ol. Diri Ol."
liste = metin.split(".")
for x in liste:
    print (x)