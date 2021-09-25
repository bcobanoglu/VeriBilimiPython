'''
Örnek 7.3
Şimdi girilen bir sayının faktöriyelini alan programı her iki yapıda kodlayalım
'''
#Döngüsel faktöriyel fonksiyonu
def fakt1(n):
    f = 1
    for i in range (n, 0, -1):
        f = f*i
    return f


#Özyinelemeli faktöriyel fonksiyonu
def fakt2(n):
    if n <= 1:
        return 1
    else:
        return n *fakt2(n-1)
#return 1 if n <= 1 else n * fakt(n - 1)

#Ana program
n = int (input("Faktöriyeli alınacak sayı.:"))
print (fakt1(n))
print (fakt2(n))