'''
Örnek 14.8: Bir metinden telefon rehberi oluşturan programı kodlayınız
'''
import re
text = """Ali Koç: 545.345.12.54 Fenerbahçe
Adnan Polat: 532.345.34.28 Galatasaray
Süleyman Seba: 541.76.25.66 Beşiktaş
Ahmet Ağaoğlu: 544.326.45.84 Trabzon"""
liste = re.split("\n+", text)
for ad in liste:
    print (re.split(":? ", ad, 4))