'''
Örnek 17.6: Aşağıdaki gibi ‘rehber.csv’ isminde bir dosyamız olduğunu
varsayalım. Şimdi bu dosyadaki kayıtları okuyan bir program yazınız.
'''

#csv modülünü import et(çağır)
import csv
#f ile temsil edilen 'rehber.csv' dosyasını aç
with open('rehber.csv', 'r', newline='') as f:
    #dosyadaki ',' ile ayrılmış her bir veriyi okuDosya değişkeninde tut
    okuDosya = csv.reader(f, delimiter=',')
    #okuDosya'daki her bir veriyi ekrana yaz
    for satir in okuDosya:
        print(', '.join(satir))