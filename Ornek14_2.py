'''
Örnek 14.2: Verilen bir listeden adı ‘a’ veya ‘b’ ile başlayan ve ‘e’ ile biten
isimleri gösteren programı kodlayınız.
'''
import re
liste=["ali","ayşe","bade","sare","can", "bere"]
#a veya b ile başlayan ve e ile biten isimleri göster
for isim in liste:
    if re.search ("^[ab].*e$",isim):
        print(isim)