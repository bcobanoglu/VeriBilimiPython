'''
Örnek 18.4:
MongoDB veri tabanı ile bağlantı kurmak için gerekli programı yazınız
'''
from pymongo import MongoClient
""" MongoDB veritabanı ile bağlantı"""
try:
    c = MongoClient('mongodb://localhost:27017/')
    #Alternatifi: c = Connection(host="localhost", port=27017)
    print ("veri tabanına bağlanıldı")
except:
    print ("MongoDB bağlantısı başarısız ")