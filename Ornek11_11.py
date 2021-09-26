'''
Örnek 11.11: Anahtarlarda (key) yapılan işlerin, değerlerde (value) ise işi yapan
kişilerin liste şeklinde tutulduğu bir sözlük yapısındaki anahtar ve değerleri ters
çeviren programı kodlayalım
'''
#mevcut sözlük
Sozluk = {  'boyama': 'mert', 
            'döşeme': 'can',
            'tesisat': 'mert', 
            'mobilya': 'veli'}
#yeni sözlük
yeniSzlk={}
for a, d in Sozluk.items():
    yeniSzlk.setdefault(d,[])
    yeniSzlk[d].append(a)
print (yeniSzlk)