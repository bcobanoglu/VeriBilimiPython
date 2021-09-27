'''
Örnek 15.7 (Takvim Uygulaması): Girilen bir yıla ait yerel takvimi (Türkçe)
listeleyen programı kodlayınız
'''
import calendar
import locale
locale.setlocale(locale.LC_ALL, '') #yerel tarih
yil = int(input("Takvim yılını giriniz:"))
calendar.prcal(yil)