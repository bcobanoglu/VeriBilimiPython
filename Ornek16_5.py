'''
Örnek 16.5 (raise ile bilerek hata mesajı üreten bir uygulama örneği)
'''
kat = int(input("hangi kata çıkacaksınız: "))
if kat == 7:
    raise NameError("Bu kata çıkamazsınız!")

print("Asansör", kat, "a çıkıyor")