'''
Örnek 11.7: Sayıları harf karşılıkları ile eşleştiren bir sözlük yapısı oluşturalım.
Sonra da klavyeden girilen rakamın harf karşılığını ekrana yazdıran programı
kodlayalım
'''
rakam = int(input("1-9 arası bir sayı gir.:"))
Sozluk = {1:"Bir", 2:"İki", 3:"Üç", 4:"Dört", 5:"Beş", 6: "Altı", 7:"Yedi", 8:"Sekiz", 9:"Dokuz"}
#Rakam karşılığı sözlükte yoksa uyarı mesajı verelim
print(Sozluk.get(rakam, "Sözlükte yoktur!"))