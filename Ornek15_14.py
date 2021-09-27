'''
Örnek 15.14: String veri tipinde tarih verilerinin tutulduğu bir listeyi tarih-zaman
tipinde farklı saat dilimlerine (“Tokyo”, “İstanbul” gibi) dönüştüren uygulamayı
kodlayınız
'''
import pendulum
tarihList = ["01.01.2020","01.02.2020", "01.03.2020","15.07.2021"]
#bölgesel tarih-saat formatında listele
b = []
t = []
for tarih in tarihList:
    x = pendulum.parse(tarih, tz= "Europe/Istanbul", strict=False)
    y = pendulum.parse(tarih, tz= "Asia/Tokyo",strict=False)
    b.append(x)
    t.append(y)

print ("Yıl-Ay-Gün T Saat Formatı")
for ist in b:
    print (ist) #Türkiye/istanbul saati

print ("----------------")

for tky in t:
    print (tky) #Asya/tokyo saati