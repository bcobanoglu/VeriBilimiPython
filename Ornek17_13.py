'''
Örnek 17.13. read_json(): Bir web sayfasından (JSON formatındaki) verileri
çeken programı kodlayınız.
'''
import pandas
import numpy
webSayfa= "http://python-data.dr-chuck.net/comments_42.json"
print (pandas.read_json(webSayfa))