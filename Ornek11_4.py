'''
Örnek 11.4:
Dil = ('C', 'C++', 'C#', 'Java', 'Python', 'Swift')
şeklindeki demet veri yapısındaki 'Python' değerini 'Piton' olarak değiştiren
programı kodlayınız
'''
Dil=('C', 'C++', 'C#', 'Java', 'Python','Swift')
Dil = list(Dil)         #Listeye dönüştü
Dil.remove('Python')    #Python silindi
Dil.insert(4,'Piton')   #4. indisli eleman 'Piton' oldu
print(tuple(Dil))       #Tekrar demete dönüştürüldü