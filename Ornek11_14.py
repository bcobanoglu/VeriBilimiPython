'''
Örnek 11.14. (Sözlük yapısında min, max fonksiyonlarının kullanımı):
'''
sozluk = { 'a': 9, 'b': 2,'c': 6, 'd': 13 }
enk = min(sozluk, key=sozluk.__getitem__)
enb = max(sozluk, key=sozluk.__getitem__)
print ("en küçük eleman: ", enk)
print ("en büyük eleman: ", enb)
