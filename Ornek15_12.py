'''
Örnek 15.12: Atatürk'ün doğum tarihi ile vefat tarihi arasındaki gün sayısını
hesaplayıp ‘’Atam 20993 gün yaşadı” şeklinde mesaj veren uygulamayı
pendulum paketini kullanarak kodlayınız.
'''
import pendulum
d = pendulum.datetime(1881, 5, 19)
v = pendulum.datetime(1938, 11, 10)
sure = v - d
print ("Atam", sure.in_days(), "gün yaşadı")