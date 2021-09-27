class Araba:
    def __init__(self):
        self.marka = 'BMW'
        self.moto = self.Motor()
    def yaz(self):
        print('Marka = ', self.marka)
    #iç sınıf
    class Motor:
        def __init__(self):
            self.ykt = "Dizel"
            self.vts = "Otomatik"
        def yaz(self):
            print('Motor = {}-{}'.format(self.ykt, self.vts))
#Ana program
# araba sınıfından nesne türetildi
taksi = Araba()
taksi.yaz()
# Motor iç sınıfından nesne türetildi
x = Araba.Motor() #ya da x = taksi.moto
x.yaz()


