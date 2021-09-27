'''
Örnek 22.3: Pandas serilerini (series), veri çerçevesine (dataframe)
dönüştürme işlemi ise aşağıdaki gibi gerçekleştirilebilir.
'''
import pandas as pd
#pandas serilerini dataframe dönüştürme
d = {
"bir": pd.Series([1, 2, 3], index=["a", "b", "c"]),
"iki": pd.Series([7, 8, 9, 10], index=["a", "b", "c", "d"]),
}
df = pd.DataFrame(d)
print (df)