'''
Örnek 17.3 (Metin dosyasına veri yazma ve okuma): 5 kişilik bir sınıftaki
öğrencilerin adını, soyadını ve notlarını ‘adres.txt’ isimli dosyaya yazan
(kaydeden) ve bu dosyadan okuyan (kayıtları listeleyen) programı kodlayalım
'''

notlar= ["Ömer Can :90",
        "Berat Can :95",
        "Levent Ak :69",
        "Bade Zehra :50",
        "Ekrem Can :68", ]
#dosyaya veri yazma
f1 = open('adres.txt', 'w')
for n in notlar:
    f1.write(n+"\n") #notlar alt alta yazıldı
f1.close() #1.dosya kapatıldı

#şimdi dosyayı açıp, okuyalım.
print ("Ad-Soyad - Notu")
print ("----------------")
#dosyadan verileri okumak için aç
f2 = open('adres.txt',"r")

while True:
    liste = f2.read() #okunanı liste'de tut.
    #eğer liste sonu ise döngüden çık
    if len(liste) == 0:
        break

    print (liste) #liste içeriğini ekrana yaz

f2.close() #2.dosya kapatıldı