import tweepy 
from twitter_secrets import TwitterSecrets
import csv
ts=TwitterSecrets()

consumer_key = ts.CONSUMER_KEY
consumer_secret = ts.CONSUMER_SECRET
access_token = ts.ACCESS_TOKEN
access_secret = ts.ACCESS_SECRET


print(f'consumer_key: {consumer_key}')
print(f'consumer_secret: {consumer_secret}')
print(f'access_token: {access_token}')
print(f'access_secret: {access_token}')


auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api=tweepy.API(auth)

  
# Open file 
with open('data.csv') as file:
    file_data = csv.reader(file)
      
      
    for row in file_data:
        print(row[0])
        api.update_status(row[0])

# tweet='this is an automated testing tweet using #Python $BTC $ETHH'

# api.update_status(tweet)
print("Done, Check your feed..")