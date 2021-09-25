'''
Örnek 6.2:
A'dan Z'ye kadar İngilizce karakterleri ekranda gösteren programı for döngüsü
ile gerçekleştirelim.
'''
for S in range(ord('A'), ord('Z')+1):
    print (chr(S))

#...Alternatifi:
#for S in range(65, 91):
#    print (chr(S))
#...