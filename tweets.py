from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "1542794766-UmfF0uYkA9rZM4R09EjzKuApiOSwhi6PTCK0U1s"
access_token_secret = "tTbcHwtcTld8ICVp6vQs1lYLaMRbZwwCqjwqW72OdUKtT"
consumer_key = "OnqS86y9aHVwmAne3bmJQ9tLD"
consumer_secret = "rMFYdvjkrjvW59xFHFS2TAp4xxG7Cerpwv1J14uyQGtyVBQGNV"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['football', 'soccer', 'FIFA'])
