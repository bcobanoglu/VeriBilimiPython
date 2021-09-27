'''
Örnek 19.2:
Yığına eleman ekleme ve çıkarma işlemlerini liste yapısı üzerinden
gerçekleştiriniz
'''
liste = [3,4,5,6]   #liste
liste.append(7)     #yığına 7 eklendi
liste.append(8)     #yığına 8 eklendi
print ("Mevcut liste..:", liste)
print ("Yığın görünümü:", list(reversed(liste)))
print ("Yığından çıkarılan.:", liste.pop())
print ("Yığından çıkarılan.:",liste.pop())
print ("Yığının şimdiki hali.:", list(reversed(liste)))
print ("En üstteki eleman:",liste[-1] )