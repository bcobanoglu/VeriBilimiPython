'''
Örnek 22.5: Bir web sayfasından (html formatındaki) verileri çekip sütun
adlarını değiştiren, ilk kaydı silen ve ilk 4 kaydı ekranda gösteren programı
kodlayalım
'''
import pandas as pd
#web sayfasından çekilecek veri
kaynak = "http://python-data.dr-chuck.net/comments_42.html"
data = pd.read_html(kaynak) #html formatındaki dosyayı oku
#Kayıtlar tek bir liste halinde tutulduğu için
#*’ öneki ile liste halinden çıkarıp, dataframe dönüştürüldü.
df = pd.DataFrame(*data)
print (df.head()) #ilk 5 kayıtı listele
df = df.drop([0], axis=0) #ilk kaydı sil
#sütun isimlerini değiştir
df.rename(columns = {list(df)[0]:'Ad', list(df)[1]:'Yorum'}, inplace=True)
print ("========================")
print (df.sort_values(by="Ad").tail()) #Ada göre son 5 kaydı listele