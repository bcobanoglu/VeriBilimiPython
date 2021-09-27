'''
Örnek 17.17: ‘id’ numarası verilen Twitter kullanıcısının attığı son 3 tweeti
ekranda gösteren programı kodlayalım.
'''
from pytwitterscraper import TwitterScraper
tw = TwitterScraper()
tweet = tw.get_tweets(961561334361059328, count=3)
print(tweet.contents) #tweet içeriğini listele