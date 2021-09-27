'''
Örnek 17.16: name="bcobanoglu24" olan Twitter kullanıcısının (Bülent
Çobanoğlu) profil bilgilerini ekrana yazdıralım.
'''
from pytwitterscraper import TwitterScraper
tw = TwitterScraper()
pr = tw.get_profile(name="bcobanoglu24")
#Eşdeğeri: pr = tw.get_profile(id="961561334361059328")
print (pr.__dict__)