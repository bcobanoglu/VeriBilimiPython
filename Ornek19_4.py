'''
Örnek 19.4:
Basit bir ikili ağaç (binary tree) yapısını oluşturup ağaca eleman ekleme ve
silme işlemlerini gerçekleştiren programı kodlayınız.
'''
import binarytree as bt
agac = bt.Node(3) #ana düğüm
agac.left = bt.Node(6)
agac.right = bt.Node(8)
agac.left.left = bt.Node(4)
agac.left.right = bt.Node(5)
agac.right.left = bt.Node(9)
agac.right.right = bt.Node(11)
print('İkili ağaç yapısı:', agac)
print('Ağaç eleman sayısı:', agac.size)
#Ağaçtan dal silme
del agac[1] #ağacın sol dalını sil
print (agac)