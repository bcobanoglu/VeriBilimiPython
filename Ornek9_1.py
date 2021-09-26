'''
Örnek 9.1:
Bir stringin içeriğini (belli bir karakterden sonrasını değiştiren) güncelleyen
programı kodlayalım.
'''
ad = 'Galata Saray'
yeniAd= ad[:7 ] + 'Bahçe'
#Alternatifi: 
#yeniAd= ad.replace( 'Galata Saray', 'Galata Bahçe')
print ("Adres Güncellendi: ", yeniAd)