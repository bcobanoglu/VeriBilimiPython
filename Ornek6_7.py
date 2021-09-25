'''
Örnek 6.7:
Kullanıcının girdiği birbirine tam bölünebilen iki pozitif tamsayının bölümünü
bölme operatörü kullanmadan hesaplayan programı, while döngüsü ile
gerçekleştirelim
'''
sayac = 0
print ("İlk sayıyı büyük giriniz!")
s1 = int (input ("1. sayı.: "))
s2 = int (input ("2. sayı.: "))
print (s1, "/", s2, end= " = ")
while(s1>=s2):
    s1 -=s2
    sayac+=1
#döngü sonu
print (sayac)