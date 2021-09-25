'''
Örnek 5.3:
Girilen kullanıcı adı (user) ve parola bilgilerine göre doğruysa “Sitemize Hoş
geldiniz!” değilse ‘Hatalı kullanıcı adı veya parola girişi’ mesajı veren
programı kodlayalım.
'''
user = input('Kullanıcı Adı.:')
parola = input('Parola.:')
if user != 'admin' or parola != 'admin':
    print ("Hatalı kullanıcı adı veya parola girişi")
else:
    print ("Sitemize Hoşgeldiniz")