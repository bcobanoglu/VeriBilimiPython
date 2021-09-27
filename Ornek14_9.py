'''
Örnek 14.9: Bir metindeki sonu ‘ar’ ile biten kelimelerin başlangıç (start) ve bitiş
(end) pozisyonlarını (indis numaralarını) veren programı kodlayınız.
'''
import re
text = """
Sanma şâhım herkesi sen sâdıkâne yar olur
Herkesi sen dostmu sandın belki ol ağyar olur
Sâdıkâne belki ol bu âlemde dildar olur
Yar olur ağyar olur dildar olur serdar olur
Yavuz Sultan Selim"""
for m in re.finditer(r"\w+ar", text):
    print(m.start(),"-", m.end(), m.group(0))