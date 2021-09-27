'''
Örnek 14.5: Bir metin içerisinde içinde ‘-yor’ içeren kelimelerden yeni bir liste
oluşturan (esasında fiilleri bulan) programı kodlayınız
'''
import re
siir= """Ben gidiyorum, O geliyor. 
        O gelince rüzgâr esiyor."""
sonOlur=re.findall("\w+yor",siir)
#‘yor’ olanları bul kelimeleri al
print(sonOlur)