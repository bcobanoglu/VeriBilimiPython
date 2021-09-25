'''
Örnek 5.8: Bir web sitesine girişte karşılaşılabilecek HTTP istemci hata
kodlarını gösteren bir ‘http_error’ isimli fonksiyonu kodlayınız.
'''
def http_error(durum):
    match durum:
        case 400:
            return "Bad request"
        case 402:
            return "Payment Required"
        case 404:
            return "Not found"
#üç farklı durumda da aynı mesajı
#vermek için or(|) operatörü kullanılabilir
        case 422 | 423 | 424:
            return "Method failure"
#Hiçbir hata durumu ile eşleşmezse
        case _:
            return "Bilinmeyen Web hatası"

#ana program
print (http_error(404))