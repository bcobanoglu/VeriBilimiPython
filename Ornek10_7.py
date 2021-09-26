'''
Örnek 10.7:
Bir tamsayı listesini ve hedef sayıyı girdi olarak alan ve bu listedeki iki sayının
toplamı hedef sayıya eşit ise bu iki sayının indisini liste hâlinde döndüren
programı kodlayınız. 
'''
def twoSum(liste, hedef):
    uz=len(liste) #liste uzunluğu
    for i in range (uz):
        for j in range (uz):
            if (liste[j] == hedef - liste[i]):
                return [i, j] #liste şeklindedöndür

#Ana program
L = [3, 1, 4, 9, 11]
hedef= 7
print (twoSum(L, hedef))