'''
Örnek 3.7:
Bir e-posta adresindeki ‘@’ ve ‘.’ karakterlerini Unicode ve ASCII kod
karşılıklarını kullanarak kodlayalım.
'''
mail1="cobanoglubulent\u0040gmail\u002Ecom"
mail2="bulent"+chr(64)+"gmail"+chr(46)+"com"
print (mail1)
print (mail2)