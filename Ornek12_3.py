'''
Örnek 12.3:
Daha önce Örnek 12.2’de verilen Fibonacci serisini hesaplayan programı yield
komutu ile kodlayalım.
'''
def fib(max):
    a, b = 0, 1 #a=0; b=1 oldu
    while a < max:
        yield a #a değerini döndürür
        #a değerini test amaçlı yazdıralım
        print ("a:",a)
        # a = b; b = a + b yer değiştirme işlemini yapalım
        a, b = b, a + b

#Ana program
#1000'e kadar ki Fibonacci serisini yazdır
for n in fib(1000):
    print("n:", n, end=', ')