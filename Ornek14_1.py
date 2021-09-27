'''
Örnek 14.1: Bir String dizideki çift basamaklı sayıları listeleyen programı
kodlayınız
'''
import re
liste = ["1","3","04","5","6","7","8","09","10","12"]
regex = r"([0-9]{2})" #çift basamaklı sayıları grupla
for s in liste:
    if re.match(regex,s):
        print(s)