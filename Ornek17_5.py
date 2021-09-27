'''
Örnek 17.5:
Daha önce Örnek 17.3’te verilen 5 kişilik bir sınıftaki öğrencilerin adını, soyadını
ve notlarını ‘notlar.bin’ isimli binary dosyaya yazan (kaydeden) ve bu dosyadan
okuyan (kayıtları listeleyen) programı kodlayınız.
'''
import pickle #pickle modülü çağrıldı
notlar= ["Ömer Can :90",
        "Berat Can :95",
        "Levent Çoban :99",
        "Bade Zehra :50",
        "Ekrem Can :68" ]
#ikili dosya yazma amaçlı açıldı ve notlar yazıldı
with open('notlar.bin', 'wb') as f:
    pickle.dump(notlar,f)
#şimdi dosyayı açıp, okuyalım.
with open('notlar.bin', 'rb') as f: 
    notList=pickle.load(f)
    print(notList )