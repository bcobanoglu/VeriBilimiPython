'''
Örnek 10.11:
3*3’lük bir A matrisini tek boyutlu diziye (iç içe iki listeyi tek listeye) dönüştüren
programı kodlayınız.
'''
A= [[1,2,3],
    [4,5,6],
    [7,8,9]]
B = [num for elem in A for num in elem]
print (B)