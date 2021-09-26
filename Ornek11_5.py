'''
Örnek 11.5: Bir kümeye başka bir küme veya demet elemanı eklemeye
çalıştığınızda neler olabileceğini örnek bir uygulama üzerinden gösteriniz
'''
k = {'d', 'b', 'c'}     #k kümesi
d = {'a', 'i'}          #d kümesi
k.add(d)                #k’ya d kümesini eklenmez ama d = ('a', 'i') demeti eklenebilir
print (k)