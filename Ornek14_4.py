'''
Örnek 14.4: Bir İngilizce metindeki zarfları bulan programı kodlayınız.
'''
import re
text = "He was carefully disguised but captured quickly by police."
regex = re.findall(r"\w+ly", text)
print (regex)