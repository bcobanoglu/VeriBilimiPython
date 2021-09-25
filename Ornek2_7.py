'''
Örnek 2.7:
Kullanıcı tarafından girilen yarıçap (r) değerine göre bir dairenin çevresini
hesaplayan programı kodlayalım.
'''
import math     #pi için gerekli
import easygui  #enterbox(), msgbox() için gerekli
r = easygui.enterbox("Dairenin yarıçapı.:")
r = float(r)    #girilen float tipine dönüştü.
Cevre = 2*math.pi*r
easygui.msgbox(msg=Cevre,title="Dairenin Çevresi")