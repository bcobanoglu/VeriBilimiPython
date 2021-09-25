'''
Örnek 5.6:
Saat Aralığı (Saat) Ücret (TL)
0-2 saat arası 5
2-4 saat arası 10
4-6 saat arası 15
6-24 saat arası 20
Yanda verilen ücret tarifesine göre otoparkta kalan araçlardan alınacak park
ücretini hesaplayan programı Python dilinde kodlayalım.
'''
Saat = float(input('Kalma Süresi.: '))
if Saat <= 2:
    Ucret = 5
elif Saat <= 4:
    Ucret = 10
elif Saat <= 6:
    Ucret = 15
else:
    Ucret = 20
print ("Park Ücreti.:", Ucret, "TL")