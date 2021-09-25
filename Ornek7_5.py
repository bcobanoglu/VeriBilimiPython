'''
Örnek 7.5:
Ackermann fonksiyonu: Matematikçi Gabriel Sudan ve Wilhelm Ackermann
tarafından geliştirilen bu fonksiyon özyinelemeli fonksiyonlara güzel bir örnektir.
Şimdi bu fonksiyonu kodlayalım:
'''
#Ackerman fonksiyonu
def ackerman(m, n):
    if (m == 0): #m=0 ise
        return n + 1
    elif (n == 0): #m>0 ve n=0 ise
        return ackerman(m-1, 1)
    else: #(m > 0) ve (n > 0) ise
        return ackerman(m-1, ackerman(m, n-1))
#Ana program
#Küçük değerler giriniz!
m = int (input("m ="))
n = int (input("n ="))
print ("A(", m, n, ") =", ackerman(m, n))