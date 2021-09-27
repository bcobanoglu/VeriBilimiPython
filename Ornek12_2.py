'''
Örnek 12.2:
Fibonacci serisini hesaplayan sınıf yapısını ‘init()’, ‘iter(), next()’ gibi özel
metotlarla kodlayınız.
'''
class Fib():
    '''Yapılandırıcı sınıf:Fib(max)'''
    def __init__(self, max):
        self.max = max
    def __iter__(self):
        self.a = 0
        self.b = 1
        return self
    def __next__(self):
        fib = self.a
        if fib > self.max:
            exit() #next() fonksiyonunu sonlandır
            #eşdeğeri: raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        # a = b; b = a + b yer değiştirme işlemi yapıldı
        return fib

#Ana program
'''1000'e kadar ki Fibonacci serisini yazdır'''
for n in Fib(1000):
    print(n, end=' ')