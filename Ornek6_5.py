'''
Örnek 6.5:
Girilen iki pozitif tam sayının çarpımını çarpma operatörü kullanmadan
hesaplayan programı, for döngüsü ile gerçekleştirelim.
'''
carp = 0
s1 = int (input("1. sayı.:"))
s2 = int (input("2. sayı.:"))
for i in range (0, s1):
    carp = carp + s2
#döngü sonu
print (s1, "*", s2, "=", carp)