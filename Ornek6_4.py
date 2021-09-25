'''
Örnek 6.4:
0’dan 24’e kadar olan çift sayıların toplamını ekranda gösteren programı for
döngüsü ile kodlayalım.
'''
T = 0
for a in range(0,25,2):
    T = T + a
#döngü sonu
print("Toplam= ", T)