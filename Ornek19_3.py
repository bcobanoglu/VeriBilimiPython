'''
Örnek 19.3:
Basit bir tek bağlı liste (linked list) oluşturup listeye eleman ekleme ve silme
işlemlerini gerçekleştiren programı kodlayınız.
'''
#Node(düğüm) sınıfı
class Node:
#Node nesnesinin başlangıç metot ve özellikleri
    def __init__(self, veri):
        self.veri = veri # veri(data) ata
        self.next = None # next başlangıç değeri:null

#Linked List sınıfı bir Node içerir
class LinkedList:
#head başlangıç değeri: null
    def __init__(self):
        self.head = None
    #Baştan itibaren sırası ile listeyi yaz
    def yazList(self):
        temp = self.head
        while (temp):
            print (temp.veri)
            temp = temp.next
    #aranan değere göre listeden sil
    def remove(self, ara):
        n = self.head
        temp = None
        while n and n.veri != ara:
            temp = n
            n = n.next
        #listeden bağını kopar (sil)
        if temp is None:
            self.head = n.next
        elif n:
            n.next = n.next
            n.next = None

#Ana program
#Bir Linked List nesnesi oluşturalım
llist = LinkedList()
#ve llist nesnesine düğümler/elemanlar ekleyelim
llist.head = Node(1) #ilk düğüm
ikinci = Node('a') #ikinci düğüm
ucuncu = Node(3) #üçüncü düğüm
dorduncu = Node('d') #dördüncü düğüm
#ilk düğüm ile ikinci düğüm arasındaki bağ
llist.head.next = ikinci
#ikinci düğüm ile üçüncü düğüm arasındaki bağ
ikinci.next = ucuncu
#üçüncü düğüm ile dördüncü düğüm arasındaki bağ
ucuncu.next = dorduncu
#düğüm yapısının mevcut halini göster
llist.yazList()
print ("================")
#Linked list yapısından bir eleman sil
llist.remove(3)
#ve düğüm yapısının son halini göster
llist.yazList()