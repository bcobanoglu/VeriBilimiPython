'''
Örnek 10.8:
0-100 arasındaki çift ve tek sayıları ayrı ayrı listeleyen programı kodlayalım.
'''
Cft = [i for i in range(54) if i % 2 == 0]
Tek = [i for i in range(54) if i % 2 != 0]
print (Cft)
print (Tek)
