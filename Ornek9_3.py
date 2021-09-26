'''
Örnek 9.3:
1’den 10’a kadarki sayıları ve karelerini sağa dayalı bir şekilde ekrana
yazdıralım.
'''
print ("Sayı\tKaresi")
print ("----\t----")
for x in range(1, 11):
    #sayı 2 karakter, karesini ise 3 karakter sağa dayalı yaz
    print(f'{x:02} \t {x*x:3} ')