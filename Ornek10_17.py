'''
Örnek 10.17 (map ve zip fonksiyonlarının birlikte kullanımı):
İki listenin elemanlarını toplayan programı map() ve zip() fonksiyonları ile
kodlayalım.
'''
t = list(map(sum, zip([1, 2, 3], [4, 5, 6])))
print (t)