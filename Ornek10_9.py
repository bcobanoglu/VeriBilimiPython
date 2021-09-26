'''
Örnek 10.9:
Girilen para miktarını şu anda kullanılmakta olan kâğıt para kupürlerine ‘200 -
100 - 50 - 20 - 10 - 5’ göre en az sayıda kupür ile ödemek için bir veznedara
yardımcı olacak programı kodlayınız.
'''
kupur=[200,100,50,20,10,5]
para = int(input('Para miktarı.:'))
para2 = para
for i in range(len(kupur)):
    sayi = para//kupur[i]
    if sayi !=0:
        print(sayi,"adet",kupur[i])
        para=para-sayi*kupur[i]

print ("Ve", para2-(para2-para), "TL bozukluk vermelisiniz")