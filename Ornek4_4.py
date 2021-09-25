'''
Örnek 4.4:
Dik kenar uzunlukları kullanıcı tarafından girilen bir dik üçgenin hipotenüsünü,
Pisagor teoremine göre hesaplayan programı kodlayalım.
'''
b = int (input("1.dik kenar.:"))
c = int (input("2.dik kenar.:"))
a = (b**2 + c**2)**0.5
print ("Hipotenüs.:", a)