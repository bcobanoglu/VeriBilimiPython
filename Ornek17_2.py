'''
Örnek 17.2: Girilen bir ismi 5 kez “isim.txt” adlı bir dosyaya yazan programı
Python dilinde kodlayınız.
'''
adi = str(input("Bir isim giriniz"))
#w: Dosyayı yazma (write) amaçlı açıldı.
dosya = open('D:\\isim.txt', 'w')
for i in range(5):
    dosya.write(adi+"\n")
    #dosyaya girilen ad 10 kez yazıldı
dosya.close() #dosya kapatıldı