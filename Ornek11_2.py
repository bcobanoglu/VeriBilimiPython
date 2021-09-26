'''
Örnek 11.2: Temel matematiksel küme işlemlerini (birleşim, kesişim, fark ve
simetrik fark) gerçekleştiren programı kodlayınız.
'''
# Küme elemanları
A = {0, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}
# Birleşim
print("A u B=", A | B)
# Kesişim
print("A ∩ B=", A & B)
#Fark
print("A \ B=", A - B)
# Simetrik fark
print("A ∆ B=", A ^ B)