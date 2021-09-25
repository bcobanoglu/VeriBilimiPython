'''
Proje 6.11 (while True örneği): Trafik Sinyalizasyon Sistemi
Trafik sinyalizasyon sistemimizde; yeşil ışıkta geçilecek, sarı ışıkta
yavaşlayacak ve kırmızı ışıkta durulacaktır. Programda “Kırmızı” - “Sarı” –
“Yeşil” renk düzeneği kullanılmıştır.
'''

# Trafik Sinyalizasyon Sistemi
while True:
    Sinyal = input('Trafik Lambası rengi.:')
    if (Sinyal =='Kırmızı'):
        print ("Dur")
    if (Sinyal =='Sarı'):
        print ("Yavaşla")
    if (Sinyal =='Yeşil'):
        print ("Geç")
        break #döngüden çık
#Döngü sonu