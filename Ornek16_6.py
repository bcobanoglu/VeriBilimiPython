'''
Örnek 16.6: Verilen bir listenin her bir elemanının sayı olup olmadığını test
eden basit bir assert uygulamasını gerçekleştiriniz.
'''
def testSayi(liste):
    for i in liste:
        try:
        #i: bir sayı mı?
            assert str(i).isnumeric()
        #sayı değilse except bloğu çalışır
        except AssertionError:
            print("{} sayı değil.".format(i))

#Ana program
liste = [1, 2, 3, 'c', 4, 5, 'a', 6, 'd']
testSayi(liste)