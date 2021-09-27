'''
Örnek 19.5:
Rastgele sayılardan oluşan basit bir min-heap ve max-heap veri yapısını
‘binarytree’ modülüne ait metotlar ile modelleyen programı kodlayınız.
'''
#binarytree ile heap oluşturma
import binarytree as bt
#rastgele 2 derinlikte min-heap yapısı
kok1 = bt.heap(height = 2, is_max = False, is_perfect = True)
print('min-heap yapısı.: \n', kok1)
#rastgele 2 derinlikte max-heap yapısı
kok2 = bt.heap(height = 2, is_max = True, is_perfect = True)
print('max-heap yapısı.: \n', kok2)