'''
Örnek 4.5:
Girilen üç sayı içerisinden en büyük olanı ekranda gösteren programı
kodlayalım.
'''
a = int (input("1.sayı.:"))
b = int (input("2.sayı.:"))
c = int (input("3.sayı.:"))
enb = max (a, max(b,c))
print ("En büyüğü.:",enb)