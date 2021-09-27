'''
Örnek 19.1:
Kuyruğa eleman ekleme veya kuyruktan eleman çıkarma işlemlerini
gerçekleştiren basit bir uygulama gerçekleştiriniz.
'''
import collections as col
kyrk = col.deque(["Ömer", "Bade", "Berat"])
#Kuyruğa elemanlar ekleniyor
kyrk.append("Can")
kyrk.append("Zehra")
kyrk.append("İsmail")
print ("Kuyruktakiler.:\n", kyrk)
print ("Kuyruğun başı.:", kyrk[0])
#Kuyruktaki ilk eleman çıkarıldı
print ("Kuyruktan çıkarılan.:", kyrk.popleft())
kyrk.append("Levent") #yeni eleman eklendi
print ("Son hali.:", list(kyrk))