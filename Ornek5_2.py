'''
Örnek 5.2:
Kullanıcı tarafından girilen Not değerine göre öğrencinin o dersten geçip,
geçmediğini ekranda gösteren programı kodlayalım.
'''
N = int (input("Notu.: "))
if N >= 50:
    print ("Geçti")
else:
    print ("Kaldı")