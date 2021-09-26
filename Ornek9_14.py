'''
Örnek 9.14: Sezar Şifrelemesi
Konsoldan girilen bir kelimedeki her harfi, o harften sonra 3 harf atlayarak
(gerektiğinde ‘Z’ den ‘A’ ya atlayacak şekilde) şifreleyen ve şifrelenmiş kelimeyi
ekranda gösteren programı kodlayınız.
'''
#Sezar fonksiyonu
def sezar(s):
    tKar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    donus = tKar[3:]+tKar[:3]
    rotKar = lambda c: donus[tKar.find(c)] if tKar.find(c)>-1 else c
    return ''.join( rotKar(c) for c in s )
#Ana program
s=input("Metni giriniz.:")
print(sezar(s.upper()))