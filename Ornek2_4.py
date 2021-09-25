'''
Örnek 2.4:
Kullanıcı tarafından girilen yarıçap (r) değerine göre bir dairenin alanını
hesaplayan programı kodlayalım.
'''
import math #pi sayısı için gerekli kütüphane
r = float(input("Yarıçapı.:"))
Alan = math.pi*(r*r)
print (f"Dairenin Alanı.:{Alan:.3f}")
#Eşdeğeri: print("Dairenin Alanı.: {0:.3f}".format(Alan))