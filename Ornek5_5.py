'''
Örnek 5.5:
100’lük sisteme göre girilen başarı notunu harfli sisteme dönüştüren programı
kodlayalım.
'''
Nt = int (input("0-100 arası not gir.:"))
if Nt>=90 and Nt<=100: #100<=Nt<90
    print("AA")
elif Nt>=80 and Nt<90:
    print("BA")
elif Nt>=70 and Nt<80:
    print("BB")
elif Nt>=60 and Nt<70:
    print("CB")
elif Nt>=50 and Nt<60:
    print("CC")
else:
    print("FF")