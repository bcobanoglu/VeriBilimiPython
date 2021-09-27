'''
Örnek 17.19: Bilgisayarınızdaki bir resim dosyası üzerinde ‘yeniden
boyutlandırma, gri tonlama, farklı formatta kaydetme, döndürme’ gibi işlemleri
gerçekleştiren bir program yazınız.
'''
from PIL import Image, ImageFilter  #pillow kütüphanesinin ilgili sınıflarını ekle
r1 = Image.open('bulent.jpg')       #resmi yükle
r1.show()                           #yüklenen resmi göster

r2 = r1.resize((200, 250))          #resmi yeniden boyutlandır
x=r2.rotate(90)                     #resim2'yi 90 derece döndür
r2=x.convert('L')                   #x'e greyscale-gri ton (L) moduna dönüştür.
r2.save('pngBulent.png')            #r2'i 'pngBulent.gif' olarak kaydet.
r2.show()                           #2.resmi ekranda göster

r3= r1.filter(ImageFilter.BLUR)     #1.resmi bulanıklaştır
r3.show()                           #ve göster

r4 = r2.transpose(method=Image.TRANSPOSE)   #2.resmin transpozesini al
r4.show()                                   #ve ekranda göster
print("resim-1 uzantısı:",r1.format)        #1. resmin dosya uzantısını,
print("resim1 modu:",r1.mode)               #pixel formatını,
print("resim1 boyutu:", r1.size)            #Resim boyutunu (genişlik, yükseklik) yaz
print("resim-1 adı:",r1.filename)           #1.resmin adını,
print("resim-2 uzantısı:",r2.format)        #2. resmin dosya uzantısını,
print("resim-3 boyutu:",r3.size)            #3.resmin boyutunu,
print("resim-4 modu:",r4.mode)              #4.resmin formatını yaz