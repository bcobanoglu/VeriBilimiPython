'''
Örnek 15.6:
29 Ekim tarihi geldiğinde “Cumhuriyet Bayramınız Kutlu Olsun” kutlama
mesajını ekrana yazan programı kodlayınız
'''
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, '')
bugun = datetime.today().strftime('%d %B')
gun, ay = bugun.split(' ')
print ("Bugün.: ", gun, ay)
if gun=='29' and ay=='Ekim' :
    print ("""
    X X X X X X X X X X X X X X X X X
    X                               X
    X   Cumhuriyet Bayramımız       X
    X               Kutlu Olsun     X
    X                               X
    X X X X X X X X X X X X X X X X X
    """)