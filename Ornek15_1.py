'''
Örnek 15.1: Kullandığınız bilgisayarın (daha doğrusu işletim sisteminin) hangi
tarihi zamanın başlangıcı ‘epoch’ olarak kabul ettiğini gösteren bir programı
kodlayınız
'''
import time #time modülünü çağır
#Tarihin sıfır/başlangıç(0) noktasını al
epok=time.gmtime(0)
#Tarihi gün / ay / yıl formatında yaz
print (epok.tm_mday,'/',epok.tm_mon,'/',epok.tm_year)