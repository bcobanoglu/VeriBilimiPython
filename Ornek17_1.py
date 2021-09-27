'''
Örnek 17.1: Bir dosya hakkında bilgi veren uygulamayı gerçekleştiriniz.
'''
f = open("mevla.txt", "r")
print ("Dosya Adı: ", f.name)
print ("Kapalı mı Açık mı? : ", f.closed)
print ("Açılış amacı : ", f.mode)
f.close()
print ("Kapalı mı Açık mı? : ", f.closed)