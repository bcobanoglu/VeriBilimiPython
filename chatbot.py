"""
@author: Bulent Çobanoğlu
Chatbotlar, insanlarla doğal dilde etkileşim kurabilen yazılım programlarıdır.  
Bir chatbot, kullanıcının sorularını veya ifadelerini analiz eder, metin verilerini işler, anlam çıkarır ve buna uygun yanıtlar üretir. 
Chatbotlar kullanıcıların sorularını yanıtlamak, bilgi sağlamak, talimatlar vermek veya kullanıcıları yönlendirmek gibi 
işlevleri yerine getirirler.
Tabii ki basit bir chatbot programını hiç NLP kütüphanesi kullanmadan match-case yapısını kullanarak aşağıdaki gibi de kodlayabiliriz;
"""

while True:
   mesaj = input("Soru veya mesajınızı girin: ")
   match mesaj.lower():
       case "merhaba":
           cevap = f"Merhaba! Nasıl yardımcı olabilirim?"
       case "nasılsınız?":
           cevap = f"İyiyim, teşekkür ederim! Siz nasılsınız?"
       case "hava nasıl?":
           cevap = f"Hava güneşli ve sıcak!"
       case "teşekkür ederim":
           cevap = f"Rica ederim!"
       case "görüşürüz":
           cevap = f"Görüşmek üzere! İyi günler!"
       case "kapat":
           cevap = f"bye"
       case _:
           cevap = f"Üzgünüm, anlamadım. Tekrar eder misiniz?"
   if cevap=="bye":
       break
   print(cevap)
