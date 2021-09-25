'''
Örnek 2.3:
Fiyatı ve ismi girilen bir ürünün KDV dâhil fiyatını hesaplayan programı
kodlayalım. KDV oranı %18 alınacaktır.
'''
Urun = input("Ürünün Adı.:")
Fiyat= float(input("Ürünün Fiyatı.:"))
kdvFyt = Fiyat*1.18
print ("Ürün adı.:",Urun)
print(f"KDV'li Fiyatı.: {kdvFyt} TL")
#Eşdeğeri:
#print("KDV'li Fiyatı.:",kdvFyt, "TL")