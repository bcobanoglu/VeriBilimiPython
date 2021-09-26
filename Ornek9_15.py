'''
Örnek 9.15:ROT13 Şifrelemesi
Konsoldan girilen her bir karakteri (sayı içermeyecek) alfabede kendisinden
sonra gelen 13. karakter ile değiştiren (gerektiğinde ‘Z’den ‘A’ya atlayacak
şekilde) basit bir şifreleme programını yazınız
'''
#ROT13 fonksiyonu
def rot13(s):
    tKar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    donus = tKar[13:]+tKar[:13]
    rotKar = lambda c: donus[tKar.find(c)] if tKar.find(c)>-1 else c
    return ''.join( rotKar(c) for c in s )
#Ana program
s=input("Metni giriniz.:")
print(rot13(s.upper()))