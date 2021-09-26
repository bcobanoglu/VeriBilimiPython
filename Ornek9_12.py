'''
Örnek 9.12 Çarpım tablosu ezberletme oyunu:
Çarpım tablosunu ezberletmeyi amaçlayan eğitim amaçlı bir oyun kodlayınız
'''
import random
print ("*Çarpım oyunu*\nÇıkmak için harf giriniz!!!")
basarili = 0 #başarı durum sayacı
basarisiz = 0 #başarısız durum sayacı
while True:
    a = random.randint(1,10) #1-10 arası 1.sayı
    b = random.randint(1,10) #1-10 arası 2.sayı
    Soru = "{} * {} = ?".format(a,b)
    dCvp = a * b #doğru cevap
    cvp = input(Soru)
    #oyundan çıkma durumu:
    if cvp.isdigit()==False: #cevap sayı değilse
        break #programdan çık
    #cevaba göre verilen mesaj
    if int(cvp) == dCvp:
        basarili +=1
        print("Cevap doğru!")
    else:
        basarisiz +=1
        print("Cevap hatalı")

#Ana program:Test durumu
if basarisiz == 0:
    print ("Bravo, hepsini doğru bildiniz... ")
elif basarili>basarisiz:
    print ("Tebrikler, çarpman iyi ama biraz daha dikkat...")
else:
    print ("Üzgünüm, çarpım tablosunu tekrar ezberlemen gerek...")