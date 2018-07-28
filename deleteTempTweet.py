import tweepy
from datetime import datetime, timedelta

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

now = datetime.utcnow()

numOfMyStatuses = api.me().statuses_count

allMyTweets = api.user_timeline(count=numOfMyStatuses)
for myTweet in allMyTweets:
    myHashtags = myTweet.entities['hashtags']
    for hashtag in myHashtags:
        if hashtag['text'].find('temp_') == 0:
            try:
                tempDays = int(hashtag['text'].split("temp_", 2)[1])
            except ValueError:
                tempDays = 0
            tempDays = timedelta(days=tempDays)
            if tempDays.days > 0:
                tweetDays = now - myTweet.created_at
                if tweetDays >= tempDays:
                    print(myTweet.text)
                    api.destroy_status(myTweet.id)
                    break

