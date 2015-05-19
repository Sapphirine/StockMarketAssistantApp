from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

ckey = 'dNATh8K9vGwlOSR2phVzaB9fh'
csecret = 'LmBKfyfoZmK1uIu577yFR9jYkVDRC95CXcKZQBZ8jWx9qdS4Vt'
atoken = '2165798475-nuQBGrTDeCgXTOneasqSFZLd3SppqAJDmXNq09V'
asecret = 'FOVzgXM0NJO2lHFydFCiOXCZdkhHlYBkmPNsWbRhLk8xd'

class Listener(StreamListener):
    def on_data(self, data):
        try:
            #print data
            tweet = data.split(',"text":"')[1].split('","source')[0]
            #print tweet
            
            #saveThis = str(time.time())+'::'+tweet
            saveFile = open('twitterData.txt','a')
            saveFile.write(tweet)
            saveFile.write('\n')
            saveFile.close()

        except BaseException as e:
            print ('failed ondata'), str(e)
            time.sleep(5)
    
        
    def on_error(self, status):
        print (status)
    
#to authorize        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream= Stream(auth, Listener())
twitterStream.filter(track=['Apple'])

start_time = time.clock()
while True:
    if time.clock() - start_time > 5:
        break 
twitterStream.disconnect()

