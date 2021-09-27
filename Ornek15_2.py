'''
Örnek 15.2: Şu anki tarih ve saati veren uygulamayı iki farklı modülü kullanarak
gerçekleştiriniz.
'''
import time
suAn = time.asctime()
#alternatifi: suAn = time.ctime()
print (suAn)

from time import *
#GünAdı, Gün-Ay-Saat:Dakika:Saniye
suAn = strftime("%a, %d-%b-%Y-%H:%M:%S",
localtime())
print(suAn)

from datetime import datetime
suAn = datetime.now()
#Yıl-Ay-Gün-Saat:Dakika:Saniye
print(f'{suAn:%Y-%m-%d %H:%M:%S}')

from datetime import datetime
suAn = datetime.now()
#alternatifi: suAn = datetime.utcnow()
print (suAn)