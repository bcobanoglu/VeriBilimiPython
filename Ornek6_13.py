'''
Örnek 6.13: Çarpım tablosunu aşağıdaki desende ekrana basacak programı
Python dilinde kodlayalım:
'''

#Tablo deseninin ilk iki satırı
print("\t\t1\t2\t3\t4\t5\t6\t7\t8\t9\n")
print("\t\t---\t---\t---\t---\t---\t---\t---\t---\t---")
#Dıştaki i döngüsü
for i in range (1,10):
    print(i,"\t|", end=" ") #Tablo deseninin ilk sütunu
    #İçteki j döngüsü
    for j in range(1,10):
        #Diğer satır ve sütunlara çarpım sonucu yazdırılacak
        print("\t", i * j, end=" ")
    #içteki j döngüsünün sonu
    print("\n") #içteki döngünün her tamamlanmasından sonra bir alt satıra geç
#Dıştaki i döngüsünün sonu