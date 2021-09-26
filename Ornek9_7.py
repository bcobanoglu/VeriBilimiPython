'''
Örnek 9.7:
Parola (password) sorgulaması yapan bir programı kodlayalım
'''
sayac=0
while sayac<3:
    parola = input('Parola.:')
    if parola == 'alim':
        print('hoş geldiniz!')
        break #döngüden çık
    else:
        sayac += 1
        print('Hatalı')

if sayac>=3:
    print('üzgünüm, hakkınız kalmadı!')