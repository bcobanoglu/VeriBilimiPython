'''
Örnek 16.4: Farklı try-except-else-finally kullanımlarında
farklı mesajlar gösteren bir programı kodlayalım.
'''
def Test1():
    try:
        1/0
    except TypeError:
        print('Veri tipi hatası')
    except ZeroDivisionError:
        print('Sıfıra bölme hatası')

def Test2():
    try:
        1/0
    except (TypeError, ZeroDivisionError):
        print('TypeError veya ZeroDivisionError hatası!')

def Test3():
    try:
        1/0
    except Exception as e:
        print(e)

#Ana program
Test1()
Test2()
Test3()