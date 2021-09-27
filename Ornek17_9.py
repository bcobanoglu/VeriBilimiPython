'''
Örnek 17.9. read_csv: Daha önce Örnek 17.5’te verilen ‘rehber.csv’
dosyasındaki kayıtları okuyan programı pandas modülünü kullanarak
gerçekleştiriniz.
'''
# -*- coding: UTF-8 -*-
import pandas
f = pandas.read_csv('rehber.csv') #dosyadan oku
print(f)