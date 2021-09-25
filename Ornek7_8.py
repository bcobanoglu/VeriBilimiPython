'''
Örnek 7.8:
‘if __name__ == '__main__':’ sorgusunun etkisini örnek bir program üzerinden
anlamaya çalışalım.
'''

import ab #ab dosyasını import edelim
def main():
    print('Ana fonksiyon')
def x():
    print ('X fonksiyonu')
if __name__ == "__main__":
    main()