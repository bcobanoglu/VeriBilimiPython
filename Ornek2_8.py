'''
Örnek 2.8:
Kullanıcı tarafından girilen parolayı ‘*’ karakteri ile maskeleyen ve parolayı
ekranda gösteren programı kodlayalım.
'''
import math
import easygui as kutu
#easygui program içerisinde ‘kutu’ ile temsil edilecek
parola = kutu.passwordbox("Parola.:")
kutu.msgbox(parola) #print(parola)