'''
Örnek 4.7:
Aşağıdaki ifadenin çıktısı ne olur? Açarak yeniden kodlayalım.
'''
i, j = 1, 2
i += 1
j *= i
print (j)

'''
Örnek 4.8:
Aşağıdaki program çalıştırıldıktan sonra d, e, f ve g değişkenlerinin son
değerleri ne olur?
'''
b = 1; c = 2
d = b & c
e = b | c
f = c >> 1
print(d,e,f)