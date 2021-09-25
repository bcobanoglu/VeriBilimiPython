'''
Örnek 6.10 (while True örneği):
Girilen sayı sıfırdan farklı olduğu sürece o sayının karesini alan programı ‘while
True:’ kodlayalım.
'''
print("Çıkmak için 0 giriniz!")
while True: #sonsuz döngü
    S = int(input('Gir bir sayı.:'))
    if S == 0:
        break
    print ("Karesi.: ", S*S)