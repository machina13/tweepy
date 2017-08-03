from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json

#consumer key, consumer secret, access token, access secret.
ckey="vzesZnrNCRkT638aJg8zA1iw7"
csecret="9u0UdGmKd7NjATMqqBjJxKDTZuxjlSB8tEkDM9YXZ4YY6onVOw"
atoken="3429693021-7btKN1A4TJpSX95FABMWnDH91qjjdbb5lc85fsZ"
asecret="vEBn0KQ9SlHOi3mdACFfqdHLLGYbUW45OkZ9CTm9cQLZq"

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data["text"]
        username = all_data["user"]["screen_name"]
        
        print((username,tweet))
        return True
    def on_error(self, status):
        print status
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["rt to win"])
