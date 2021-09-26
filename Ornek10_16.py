'''
Örnek 10.16 Bir matrisin satırları ile sütunlarını yer değiştiren programı kodlayalım
'''
A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12] ]
B = []
B = list(zip(*A))
print (B)