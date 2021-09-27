'''
Örnek 17.10. read_excel:‘ilPlaka.xls’ isimli aşağıdaki gibi bir Excel
dosyasındaki kayıtları veya çalışma sayfası isimlerini okuyan programı pandas
modülünü kullanarak gerçekleştiriniz.
'''
# -*- coding: UTF-8 -*-
import pandas
f = pandas.read_excel('ilPlaka.xls') #dosyadan oku
print(f)
#aktif excel dosyasındaki çalışma sayfaları
sayfa =pandas.ExcelFile('ilPlaka.xls')
print (sayfa.sheet_names)