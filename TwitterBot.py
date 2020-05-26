import tweepy
import time
consumer_key = '6PfI9DXszlbGOntnwzkkvQOPW'
consumer_secret = 'hX2rwzFBbpBIHLFQvostLevMCNIPoUr7TrBYGtVVHeFEgftvs9'
access_token = '1263865573231988736-Qw7DGIggx4d5znyxXp96P5Jii1i98X'
access_token_secret = 'I8aADEQgk8CGBoWP7hqSGeZDHLRXJfzkXOVMlYBdfQUru'
#auth = tweepy.OAuthHandler('6PfI9DXszlbGOntnwzkkvQOPW', 'hX2rwzFBbpBIHLFQvostLevMCNIPoUr7TrBYGtVVHeFEgftvs9')
#auth.set_access_token('1263865573231988736-Qw7DGIggx4d5znyxXp96P5Jii1i98X', 'I8aADEQgk8CGBoWP7hqSGeZDHLRXJfzkXOVMlYBdfQUru')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print (user.name) #prints your name.
print (user.screen_name) # print twitter handler
print (user.followers_count) # prit number of followers

search = "india"
numberOfTweets = 2

def limit_handle(cursor):
  while True:
    try:
      yield cursor.next()
    except tweepy.RateLimitError:
      time.sleep(1000)
'''
#Be nice to your followers. Follow everyone!
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
  if follower.name == 'Usernamehere':
    print(follower.name)
    follower.follow()
'''

# Like the tweet
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Liked the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break