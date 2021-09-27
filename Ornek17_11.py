'''
Örnek 17.11. read_excel: https://biruni.tuik.gov.tr/medas/ adresinden
bilgisayara indirilen ‘95.xlsx’ isimli Excel dosyasındaki kayıtları okuyan programı
kodlayalım.
'''
import pandas as pd
adres = "C:\\Users\\bc\\Downloads\\95.xlsx"
f = pd.read_excel(adres) #dosyadan oku
print(pd.DataFrame(f)) #dataframe dönüştür
#Aktif excel dosyasındaki çalışma sayfalarını listele
sayfa =pd.ExcelFile(adres)
print ("Excel Çalışma Sayfaları:")
print (sayfa.sheet_names)
