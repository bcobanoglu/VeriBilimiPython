'''
Örnek 7.2:
4 işlem yapan menülü basit bir hesap makinesi programını kodlayalım.
'''
#Menü fonksiyonu
def menu():
    print ("[+]-Toplama\n")
    print ("[-]-Çıkarma\n")
    print ("[*]-Çarpma\n")
    print ("[/]-Bölme\n")
#Hesapla fonksiyonu
def Hesapla (a, b, op):
    if (op == '+'): return a+b
    if (op == '-'): return a-b
    if (op == '*'): return a*b
    if (op == '/'): return a/b

#Ana program
while True:
    menu ()
    a = float (input ("1. sayı.:"))
    b = float (input ("2. sayı.:"))
    islec = input ("Menüden işlemi seç.:")
    sonuc = Hesapla (a, b, islec)
    print ("Sonuc= ", sonuc)
    cvp = input ("Devam mı[E/H].:")
    if cvp.lower()!='e':
        break #Eğer cvp ‘e’ değilse programdan çık