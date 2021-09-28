'''
Örnek 23.1: Bu temel çizim “çubuk (bar), pasta (pie), nokta (scatter) ve çizgi
(plot)” şekillerini basit bir uygulama üzerinden gösteren programı kodlayalım.
'''
import matplotlib.pyplot as plt
ad = ['A', 'B', 'C', 'D', 'E']
data = [10, 25, 50, 100, 60]
#Çizim(figure) çerçevesini boyutlandırır
plt.figure(figsize=(8, 2)) #Çizim alanını 4 (8/2) parçaya ayırır
#Çubuk grafik çizimi
plt.subplot(2,2,1) #x=2, y=2, sıra numarası=1
plt.bar(ad, data) #her bir çubuğa bir ad verildi
plt.xlabel("Çubuk") #grafik etiketi
#Nokta grafik çizimi
plt.subplot(2,2,2) #x=2, y=2, sıra numarası=2
plt.scatter(ad, data) #her bir noktaya bir ad verildi
plt.xlabel("Nokta") #grafik etiketi
#Şekiller arasında aralık bırakalım
plt.tight_layout()
#Pasta grafik çizimi
plt.subplot(2,2,3) #3. sıradaki grafik
plt.pie(data, labels=ad) #her bir dilime bir ad verildi
plt.xlabel("Pasta") #grafik etiketi
#Çizgi grafik çizimi
plt.subplot(2,2,4) #4. sıradaki grafik
plt.plot(ad, data) #her bir çizgiye bir ad verildi

plt.xlabel("Çizgi") #grafik etiketi
#Tüm çizimlerin ortak (üst) başlığı
plt.suptitle('Temel Çizim şekilleri')
plt.show() #tüm şekilleri/grafikleri göster