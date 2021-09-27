'''
Örnek 14.7: Girilen bir e-posta adresinin geçerli olup/olmadığını sorgulayan bir
programı kodlayınız.
'''
import re
email = input("e-posta adresini gir:")
regex = r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$" #email kontrol ifadesi
m = re.search(regex, email)
if m:
    print ("geçerli bir adres:", m.group())
else:
    print ("geçersiz bir adres, lütfen yeniden giriniz!!")