'''
Örnek 15.13: İki farklı tarih arasındaki gün veya ay farkını veren bir uygulamayı
pendulum modulünü kullanarak kodlayınız
'''
import pendulum
basla = pendulum.datetime(2020, 1, 1)
dur = pendulum.datetime(2020, 2, 5)
peryot = dur- basla
#Gün farkı
for g in peryot.range('days'):
    print(g)

print("----------------------")
#Ay farkı
for m in peryot.range('months'):
    print(m)
