'''
Örnek 10.14:
Bir listedeki sayıların karesinden yeni bir liste oluşturan programı map()
fonksiyonu ile kodlayalım
'''
liste = [1, 2, 3, 4, 5]
kare = map(lambda x: x **2, liste)
print(list(kare))