'''
Örnek 7.1:
Ana programda (main fonksiyonunda) girilen Fahrenayt sıcaklığını (F°) cevir
isimli fonksiyonla Dereceye (C°) çeviren ve çevrim sonucunu ana programda
gösteren programı yazınız. {Çevrim için C°= (F° - 32)/ 1.8 formülünü kullanınız}.
'''
#cevir fonksiyonu
def cevir(f):
    return ((f - 32) / 1.8)
#Ana program
f = float(input('Fahrenhayt değeri:'))
C = cevir(f)
print(C , " derecedir")