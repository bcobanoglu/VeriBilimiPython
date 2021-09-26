'''
Örnek 11.1:
Haftanın günlerinin rakamsal karşılığını veren programı kodlayınız
'''
gun= ['Pazartesi', 'Salı', 'Çarşamba',
'Perşembe', 'Cuma', 'Cumartesi', 'Pazar']
# enumerate() ile indisini ve değerini aldık
for i, deger in enumerate(gun, start=1):
    print(str(i) + ".gün: " + deger)