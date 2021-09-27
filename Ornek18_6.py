'''
Örnek 18.6:
Daha önceki örnekte oluşturulan ‘backup’ veri tabanı üzerindeki veri koleksiyonu
oluşturduğumuz tablo üzerinde aşağıdaki sorgulamaları yapan programı
kodlayınız:
#Sorgu-1: Tüm kayıtları ters sırada listele;
#Sorgu-2: 'ad'= 'Ali' olan kaydın adresini 'Adana' olarak değiştir;
#Sorgu-3: ’Adresi 'A' ile başlayanlar kayıtları listele;
'''
from pymongo import MongoClient
""" MongoDB veri tabanına kayıt ekleme"""
try:
    c = MongoClient('mongodb://localhost:27017/')
    print ("veri tabanına bağlanıldı")
except:
    print ("MongoDB bağlantısı başarısız ")

vt = c["backup"] #veritabanı adı
tablo = vt['rehber'] #tablo adı

#Sorgu-1: Öncelikle varolan kayıtları ters sırada listele;
print ("---Sorgu-1---")
sorgu1 = tablo.find().sort("adres", -1)
for x in sorgu1:
    print(x)
#Sorgu-2: 'ad'= 'Ali' olan kaydın adresini 'Adana' olarak değiştir;
veri = {'ad': 'Ali', 'adres': 'Mersin'}
yeniAdres = { "$set": { 'adres': 'Adana' } }
tablo.update_one(veri, yeniAdres) #güncelle

#Sorgu-3: ’Adresi 'A' ile başlayanları listele;
print ("---Sorgu-3---")
sorgu3 = { "adres": { "$regex": '^A' } }
docs = tablo.find( sorgu3 , {'_id': False})
for x in docs:
    print(x)