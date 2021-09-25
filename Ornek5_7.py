'''
Örnek 5.7: Karar Ağacı:
“Telefon, Radyo, TV, Kamera, Saat” gibi bir elektronik eşyayı aklımızdan
tutalım. Bilgisayara bu elektronik nesneyi, aşağıdakine benzer bir karar ağacını
kodlayarak buldurmaya çalışalım.
'''
print ("Karar Ağacı Oyunu:\n Aklından elektronik bir eşya tut!")
cvp = input ("Elektronik mi? [E/H]")
if cvp =='E' or cvp == 'e':
    cvp1 = input ("Taşınabilir mi? [E/H]")
    if cvp1 =='E' or cvp1 == 'e':
        cvp2 = input ("Kola takılabilir mi? [E/H]")
        if cvp2 =='E' or cvp2 == 'e':
            print("Tamam, Saat!")
        else:
            cvp3 = input ("Konuşmak için kullanılır mı? [E/H]")
            if cvp3 =='E' or cvp3 == 'e':
                print("Tamam, Telefon!")
            else:
                cvp4 = input ("Bir uygulama çalıştırır mı? [E/H]")
                if cvp4 =='E' or cvp4 == 'e':
                    print("Tamam, Tablet!")
                else:
                    cvp5 = input ("Video çeker mi? [E/H]")
                    if cvp5 =='E' or cvp5 == 'e':
                        print("Tamam, Kamera!")
                    else:
                        cvp6 = input ("Fotoğraf çeker mi? [E/H]")
                        if cvp6 =='E' or cvp6 == 'e':
                            print("Tamam, Fotoğraf Makinesi!")
                        else:
                            cvp7 = input ("Müzik dinlenir mi? [E/H]")
                            if cvp7 =='E' or cvp7 == 'e':
                                print("Tamam, Radyo!")
                            else:
                                print("Bilemedim! Elektronik değil mi?")
     
    #taşınamaz ise
    else:
        cvp8 = input ("Film izlenir mi? [E/H]")
        if cvp8 =='E' or cvp8 == 'e':
            print("Tamam, Televizyon!")
        else:
            cvp9 = input ("Beyaz Eşya mı? [E/H]")
            if cvp9 =='E' or cvp9 == 'e':
                cvpX = input("Birşey yıkar mı[E/H]")
                if cvpX =='E' or cvpX == 'e':
                    cvpXX = input("Çamaşır yıkar mı[E/H]")
                    if cvpXX =='E' or cvpXX == 'e':
                        print("Tamam, Çamaşır Makinesi!")
                    else:
                        print("Tamam, Bulaşık Makinesi!")
                else:
                    print("Tamam, Buzdolabı!")
            else:
                print ("Üzgünüm! Tahmin edemedim.")
else:
    print("Elektronik eşya tut!")