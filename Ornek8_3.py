'''
Örnek 8.3 (Puanlı Sayı Tahmin Oyunu):
Bilgisayarın tuttuğu (0-100 arasındaki) sayıya göre kullanıcıyı “daha küçük veya
daha büyük sayı giriniz gibi” yönlendiren ve kaç tahminde sayıyı bulduğunu ve
puanını söyleyen bir sayı tahmin oyununu kodlayalım.
'''
from random import *
#0-100 arası rastgele bir sayı tut
sayi = randint(1,100)
s = 0 #sayaç değişkeni
puan = 100 #puan değişkeni
print("İlk Tahmininiz.:");
while True:
    tahmin =int(input()) #senin tahminin
    s = s + 1 #sayaçı artır
    if tahmin == sayi:
        print("Bravo!",s," tahminde bildin")
        break #döngüden çık
    elif tahmin < sayi: #tahminin küçükse
        print("Daha büyük bir sayı gir!")
    else: #tahminin büyükse
        print("Daha küçük bir sayı gir!")
        puan = puan - 10 #10 puan azalt

print("Toplam puan.:", puan)