'''
Örnek 2.6:
Kullanıcı tarafından diyalog penceresinden girilen yarıçap (r) değerine göre bir
dairenin alanını hesaplayan programı kodlayalım.
'''
import math #pi için gerekli
import turtle #numinput() için gerekli
import tkinter.messagebox as msj
#messagebox program içerisinde ‘msj’ ile temsil edilecek
r = turtle.numinput("Alan", "Yarıçapı.:")
Alan = math.pi*(r*r)
msj.showinfo(title="Daire Alanı:", message=Alan)