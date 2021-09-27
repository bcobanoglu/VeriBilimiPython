'''
Örnek 14.6: Bir metin içerisindeki kelimeleri başka bir kelime ile değiştiren
programı kodlayınız.
'''
import re
tekerleme= """kartal kalkar, dal sarkar,
dal sarkar, kartal kalkar."""
degistir=re.sub("sarkar","kalkar",tekerleme)
print(degistir)