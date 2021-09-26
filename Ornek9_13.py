'''
Örnek 9.13 (Rastgele parola üreteci):
En az bir adet küçük karakter, bir adet büyük karakter ve bir adet ise rakam
içeren bir parola oluşturucu programı kodlayınız.
'''
import string
import random
s1 = string.ascii_lowercase #küçük harf
s2 = string.ascii_uppercase #büyük harf
s3 = string.digits #rakam
#özel karakter için string.punctuation eklenebilir
pUz = int(input("Password uzunluğu: "))
s = [] #boş liste tanımlandı
s.extend(list(s1)) #s1 i listeye dönüştür ve s listesine ekle
s.extend(list(s2)) #s listesini s2 ile genişlet
s.extend(list(s3)) #s listesini s3 ile genişlet
print("Üretilen password-1: ")
#pUz değeri kadar örnek al
print("".join(random.sample(s, pUz)))
#Tüm basılabilen karakterlerden oluştur:
print("Üretilen password-2: ")
s4 = string.printable
print("".join(random.sample(s4, pUz)))