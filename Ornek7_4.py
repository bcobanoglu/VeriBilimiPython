'''
Örnek 7.4:
Her elemanı kendisinden önceki iki elemanın toplamı şeklinde ifade edilen
fibonacci serisinin n. eleman değerini özyinelemeli fonksiyon ile bulan programı
yazınız.
'''
# Özyinelemeli Fibonacci serisi
def fib(n):
    if n<=2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
#Ana program
n = int (input("Serinin kaçıncı elemanı.:"))
print (f"{n}.eleman:{fib(n)}")