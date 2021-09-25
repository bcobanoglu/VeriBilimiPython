'''
Örnek 6.14 (Pascal üçgeni):
Pascal üçgenini verecek programı iç içe döngü kullanarak Python dilinde
kodlayalım.
'''
for satir in range (9):
    s = 1
    r = satir + 1
    #içteki döngü: sütun sayısı
    for sutun in range (satir+1):
        if (sutun > 0):
            s=int (s*(r-sutun) / sutun)
        print (s, end=" ")
    #sutun döngüsü sonu
    print () #Bir satır atla
#satir döngüsü sonu