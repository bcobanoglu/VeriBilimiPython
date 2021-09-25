'''
Örnek 2.5:
Kullanıcı tarafından diyalog penceresinden girilen yarıçap (r) değerine göre bir
dairenin alanını hesaplayan programı kodlayalım.
'''
import math
import turtle   #numinput() için gerekli kütüphane
r = turtle.numinput("Alan", "Yarıçapı.:")
Alan = math.pi*(r*r)
print (f"Dairenin Alanı.: {Alan:.3f}")