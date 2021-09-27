'''
Örnek 17.20: Önceki örnekteki bir resim dosyası üzerinde ‘yeniden
boyutlandırma, gri tonlama, farklı formatta kaydetme, döndürme’ gibi işlemleri
opencv kütüphanesini kullanarak gerçekleştiren bir program yazınız.
'''
import cv2                          #opencv kütüphanesi ekle
r1 = cv2.imread('bulent.jpg',1)     #resmi renkli formatta yükle
cv2.imshow("resim1", r1)            #yüklenen resmi göster
r2 = cv2.resize(r1,(90, 120))       #resmi yeniden boyutlandır
x= cv2.rotate(r2,cv2.ROTATE_90_CLOCKWISE) #resim2'yi saat yön. 90 derece döndür ve
cv2.imshow("resim2", x)             #gri tonlu göster
r2 = cv2.imread('bulent.jpg',0)     # ‘bulent.jpg’yi gri tonda oku
cv2.imwrite('Bulent2.jpg',r2)       #'Bulent2.jpg' olarak kaydet.
b = cv2.blur(r1, (10,10))           #1.resmi bulanıklaştır
cv2.imshow("resim3", b)             #ve resim3 olarak göster
r4 = cv2.transpose(r2)              #r2 nin(gri tonlu resmin) transpozesini al
cv2.imshow("resim4", r4)            #ve ekranda göster
cv2.waitKey(0)                      ##bir tuşa basılıncaya kadar bekle