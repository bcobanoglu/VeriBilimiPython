'''
Örnek 23.17: Şimdi bir önceki örnekteki grafiği yan yana iki sütun şeklinde
gruplandırarak çizdirelim.
'''
import matplotlib.pyplot as plt
import pandas as pd
#alkol kullanım yüzdelerini gösteren veri setleri
veriSeti1 = [21, 31, 27, 26, 23, 11, 4]
veriSeti2 = [6, 10, 7, 5, 3, 1, 1]
yasGrubu = ['15-24', '25-34', '35-44', '45-54', '55-64', '65-74', '75+']
#veri çerçevesine dönüştürelim
df = pd.DataFrame({'Erkekler': veriSeti1, 'Kızlar': veriSeti2}, index=yasGrubu)
print(df)
ax= df.plot.bar(rot=0, color={"blue", "purple"})
#Eşdeğeri: ax= df.plot(kind="bar", color={"blue", "purple"})
ax.set(xlabel='Yaş', ylabel='Kullanım(%)', title='Alkol kullanım oranı')
plt.show()