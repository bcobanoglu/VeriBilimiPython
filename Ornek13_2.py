'''
Örnek 13.2:
Bir önceki bölümdeki Araba örneğini @classmethod kullanarak yeniden
kodlayalım.
'''
class Araba():
    # Sınıf özellikleri
    def __init__(self, bilgi):
        self.ozellikler = bilgi
    def __repr__(self):
        return f'Araba({self.ozellikler})'

    # Sınıf metotları
    @classmethod
    def taksi(cls):
        return cls (['ABS', 'Otomatik Vites', 'Hız=240'])
    @classmethod
    def kamyon(cls):
        return cls(['ABS', 'Manuel Vites', 'Hız=180'])

#Ana program
#kamyon ve taksi nesnelerini türetilmeden özellikler değiştirildi
print("Taksi.: ", Araba.taksi())
print("---------------------")
print("Kamyon.: ", Araba.kamyon())