'''
Örnek 6.6:
Girilen sayı sıfırdan farklı olduğu sürece o sayının karesini alan programı
kodlayalım.
'''
S = 1
print ("Çıkmak için 0 giriniz!")
while (S!=0):
    S = int (input("Sayı gir.:"))
    print ("Karesi.: ", S*S)