'''
Örnek 5.4:
Girilen bir sayının sıfır mı, negatif mi, pozitif mi olduğunu ekranda gösteren
programı iç içe if else yapılarını kullanarak farklı şekillerde kodlayalım.
Çözüm:
'''
a = int (input("Bir sayı gir.:"))
if a > 0:
    print ("Pozitif")
elif a == 0:
    print ("Sıfır")
else:
    print ("Negatif")