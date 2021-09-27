'''
Örnek 14.3: Verilen listeden sayı ile başlayan verileri çeken (alan) programı
kodlayınız.
'''
import re
liste = ["1","22","A1", "333", "A2A"]
regex = r"\d+"
for s in liste:
    if re.match(regex,s):
        print(s)