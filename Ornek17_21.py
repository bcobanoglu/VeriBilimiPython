'''
Örnek 17.20: Klavyeden ‘r’ tuşuna bastıkça ekrandaki resmi saat yönünde 90
derece döndüren programı yazınız. {Programdan ‘esc’ tuşuna basıldığında
çıkılacaktır}
'''

import cv2 #opencv kütüphanesini ekle
r1 = cv2.imread('bulent.jpg') #resmi yükle
cv2.imshow("r_tusuna_bas", r1) #resmi göster
print ("Lütfen döndürmek için r tuşuna bas!")
while True: #sonsuz döngü
    key = cv2.waitKey(1) #klavyeden basılan tuşu al
    if key==ord('r'): #Eğer 'r' tuşuna basıldıysa
        dondur = cv2.rotate(r1, cv2.ROTATE_90_CLOCKWISE) #-> yönü
        cv2.imshow("r_tusuna_bas", dondur) #döndürülen resmi göster
        cv2.waitKey(0) #bekle
        dondur = cv2.rotate(dondur, cv2.ROTATE_90_CLOCKWISE) #tersi
        cv2.imshow("r_tusuna_bas", dondur) #döndürülen resmi göster
        cv2.waitKey(0) #bekle
        dondur = cv2.rotate(dondur, cv2.ROTATE_90_CLOCKWISE) #<- yönü
        cv2.imshow("r_tusuna_bas", dondur) #döndürülen resmi göster
        cv2.waitKey(0) #bekle
        dondur = cv2.rotate(dondur, cv2.ROTATE_90_CLOCKWISE) #normali
        cv2.imshow("r_tusuna_bas", dondur) #resmi göster
    elif key==27: #Esc tuşuna basıldıysa
        break #döngüden çık
cv2.destroyAllWindows() #tüm pencereleri kapat