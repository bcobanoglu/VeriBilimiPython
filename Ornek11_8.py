'''
Örnek 11.8 (Türkçe-İngilizce Sözlük Programı):
Girilen Türkçe günün İngilizce karşılığını veren Türkçe – İngilizce bir sözlük
programı kodlayalım.
'''
ara = input("Türkçe gün adı.:")
trEn = {"pazartesi": "monday", "salı": "tuesday","çarşamba": "wednesday", "perşembe": "thursday",
"cuma": "friday", "cumartesi": "saturday","pazar": "sunday"}
print("İngilizcesi.:", end=" ")
print(trEn.get(ara, "Bu kelime sözlükte yoktur!"))