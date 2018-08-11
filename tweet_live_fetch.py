from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sentiment_mod as s
import json

import twitter_credentials

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)

        if "text" in all_data:

            tweet = ascii(all_data["text"])
            sentiment_value,confidence = s.sentiment(tweet)
            print(tweet, sentiment_value, confidence)

            if confidence>=0.5:
                output = open("twitter-out.txt","a")
                output.write(sentiment_value)
                output.write("\n")
                output.close()

            return True
        
        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Avengers"])
