'''
Affine Şifrelemesi
Örnek 9.16:
Konsoldan girilen mesaj içerisindeki her bir karakteri affine (doğrusal) şifreleme
algoritması kullanarak belirli bir indis değerine (anahtar değere) göre yeniden
düzenleyen / şifreleyen programı kodlayalım.
'''
#affine şifreleme algoritması
a=3
b=5
Krk = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
msj = "BADE"
for y in msj:
    x = Krk.index(y) #indis numarasını alır
    Ex=(a*x+b) % 26 #n=26
    print(''.join(Krk[Ex]), end="" )