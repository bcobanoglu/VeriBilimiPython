'''
Örnek 9.8:
Girilen bir metnin Palindrom olup olmadığını sorgulayan programı kodlayalım
'''
s=input("Bir metin gir.:")
if s == ''.join(reversed(s)): #s==s[::-1]:
    print(s, ":palindrom")
else:
    print(s, ":palindrom degil")