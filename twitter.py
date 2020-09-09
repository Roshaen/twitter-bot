import tweepy 
import time

auth = tweepy.OAuthHandler('Juo5sWa0X8Q8Bt9JLWXkKDQ20','vo84tQ1YatsC6WQ7nS4ewLtOivqNKblpIFrnu4Jt8tWhRV8nLG')
auth.set_access_token('1252659653353320449-73o5u6o85ixkdlYspPm3kxt3ewic65','qBQE05rE7e9zlo1Zecw8vG7VE5kSAmL7nn2rSw29zXGuk')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify= True)
user = api.me()
print(user.name)
print(user.screen_name)

keyword = 'python'

for retwt in tweepy.Cursor(api.search, keyword).items(500):
    try:
        retwt.retweet()
        print("rewitted a tweet")
        time.sleep(10)
    except Exception as e:
        print(e)
        break


