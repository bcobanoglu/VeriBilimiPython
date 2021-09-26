'''
Örnek 9.4:
Bir Stringin karakterlerini tek tek önce artırarak, sonra ise azaltarak ekrana
yazdıran programı kodlayalım.
'''
metin = "Atatürk"
#metni ileriye doğru artırarak yazdırma
for a in range(1,8):
    print (metin[:a])

#şimdi de geriye doğru azaltarak yazdıralım
for a in range(1,8):
    print(f'{metin[:-a]}')
