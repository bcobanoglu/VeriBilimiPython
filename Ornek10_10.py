'''
Örnek 10.10 (Adam Asmaca Oyunu: Hangman):
Bilgisayarın hafızasında tuttuğu kelimeyi verilen hak süresi içerisinde bulmaya
çalışan ‘adam asmaca’ oyununu kodlayınız.
'''
import random
liste = ["python","basic", "swift", "php", "java", "javascript", "csharp", "ruby", "cobol", "pascal","assembly", "delphi"]
kelime = random.choice(liste)
hangman = ['''
  +--+
  o  |
 -|- |
 / \ |
   _===_
''','''
  +--+
  o  |
 -|- |
 /|
   _===_
''','''
  +--+
  o  |
 -|- |
     |
   _===_
''','''
  +--+
  o  |
 -|  |
     |
   _===_
''','''
  +--+
  o  |
  |  |
     |
   _===_
''','''
  +--+
  o  |
     |
     |
   _===_
''','''
  +--+
     |
     |
     |
   _===_
''' ]
dogruHarf = []
yanlisHarf = []
hak = len(hangman) #10
while hak>0:
    out=""
    for h in kelime:
        if h in dogruHarf:
            out = out + h #php
        else:
            out = out + "_" #p_p
    if out == kelime:
        break #döngüden çık

    print ("Kelime: ", out)
    print (hangman[hak-1])
    girHarf = input() #harf girilecek
    if girHarf in dogruHarf or girHarf in yanlisHarf:
        print ("zaten ", girHarf, "girilmişti!")
    elif girHarf in kelime:
        print ("Doğru")
        dogruHarf.append(girHarf )
    else:
        print ("Yanlış")
        hak -=1 #hak = hak - 1
        yanlisHarf.append(girHarf )

if hak:
    print ("Tebrikler, Evet:", kelime)
else:
    print ("Maalesef kelimemiz:", kelime)