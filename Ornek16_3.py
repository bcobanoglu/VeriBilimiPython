'''
Örnek 16.3: Girilen iki sayının toplamını yapan programda eğer kullanıcı sayı
haricinde bir karakter girer ise program, hata mesajı yerine 'sayı giriniz!'
uyarısı vermelidir.
'''
def topla(a,b):
    try:
        return(a + b)
    except: #bir hata olursa
        print ("sayı giriniz!")

#Ana program
print (topla(5, 3))
print (topla(5, 'a'))