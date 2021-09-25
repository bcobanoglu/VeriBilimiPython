'''
Örnek 4.3:
Bileşik faiz formülünde;
P = 1000 ₺ (Anapara/Sermaye), i = %5 (dönem faiz oranı), n = 1 (Dönem/Yıl
sayısı), FV = Sermayenin gelecekteki değeri, olmak üzere 1000 ₺ anapara,
yıllık % 5 faizle bileşik faize yatırılmış ise 1. sene sonundaki değeri ne olur?
'''
P = 1000
i = 0.05 # %5
n = 1
FV = P * ((1+i) ** n) #Bileşik faiz formülü
print (FV)