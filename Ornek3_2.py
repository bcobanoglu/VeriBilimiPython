'''
Örnek 3.2: Kullanıcının girdiği sayının farklı sayı tabanlarındaki (8’li, 10’lu ve
16’lı) eşdeğerlerini ekranda gösteren programı kodlayalım.
'''
#1.yol
onlu = int(input("Sayı.:"))
print ("Desimal değeri.:", onlu)
print ("İkili eşdeğeri.:", bin(onlu))
print ("Sekizli eşdeğeri.:", oct(onlu))
print ("Onaltılı eşdeğeri.:", hex(onlu))

#2.yol
onlu = int(input("Sayı.:"))
print ("Desimal değeri.:", onlu)
print("İkili eşdeğeri:", format(onlu, '0b'))
print("Sekizli eşdeğeri.:", format(onlu, '0o'))
print("Onaltılı eşdeğeri.:", format(onlu, '0x'))

#3.yol kitabın 31. sayfasında :)