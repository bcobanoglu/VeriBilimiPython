'''
Örnek 17.8: JSON formatında veri oluşturup, bu veriden istenilen değerleri
alan programı kodlayalım
'''
import json
#json formatına dönüşebilecek veri
#sözlük yapısına benzer şekilde tasarlanır
veri = '''[
    {"plaka" : "01",
    "il" : "Adana"
    },
    {"plaka": "24",
    "il" : "Erzincan"
    }
    ]'''
#'.loads' metodu ile veri, JSON formatına dönüştürülür
veriJS = json.loads(veri)
#JSON formatındaki verinin kayıt sayısı
print ("kayıt sayısı.: ", len(veriJS))
#JSON formatındaki veriden belli değerler alınabilir
for i in veriJS:
    print ("il adı.: ", i['il'])
    print ("plakası.: ", i['plaka'])