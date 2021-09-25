'''
Örnek 7.9 (Fizz Buzz Oyunu):
Klavyeden girilen sayıya kadarki sayıları ekrana yazan ve ekrana yazarken
3’e bölünen sayı yerine ‘Fizz’, 5’e bölünen sayı yerine ‘Buzz’, hem 3’e hem de
5’e aynı ayna bölünen sayı yerine ise ‘FizzBuzz’ yazan programı fonksiyonlar
şeklinde kodlayınız.
'''
#FizzBuzz Fonksiyonu
def FizzBuzz(limit):
    for i in range(1, limit+1):
        if i%3 ==0:
            print ('Fizz', end='')
        if i%5 ==0:
            print ('Buzz', end='')
        if i%3 and i%5:
            print (i)
#main fonksiyonu
def main():
    n = int(input("Oyun sınırı.:"))
    FizzBuzz(n)

#ana program olarak main fonk. çalıştır
if __name__ == "__main__":
    main()