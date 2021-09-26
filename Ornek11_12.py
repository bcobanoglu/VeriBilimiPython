'''
Örnek 11.12. (Roma Rakamını Dönüştürme Programı):
Verilen sayıyı roma (romen) rakamına dönüştüren veya tersi işlemi
gerçekleştiren programı kodlayalım
'''
#sayıyı roma rakamına dönüştüren fonksiyon
def romaCevir(sayi):
    output = ""
    for key, value in romenRakam.items():
        while sayi >= key:
            output += value
            sayi -= key
    return output

#roma rakamını sayıya dönüştüren fonksiyon
def romadanCevir(roma):
    output = 0
    for key, value in romenRakam.items():
        while roma.startswith(value):
            output += key
            roma = roma[len(value):]
    return output

#Ana program
romenRakam = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C",
             90:"XC", 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV",1:"I" }
print (romaCevir(24))
print (romadanCevir("XXIV"))