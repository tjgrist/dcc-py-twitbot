
import tweepy, time, sys, random
from random import randint
 
argfile = str("liners.txt")
 

 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY =  '25Nt1PmV9hzJYIJa1Qa3DgB1x'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'Eswziu1rAoPGYHEyehpP4eBtCYn9iG3EIhMKlsoRzgwS8BHyT7'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '717132551702315008-WP3X6WoL5Qg6sSDAu3s04ZpJ2drGNi5'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'NPnnt3tsY37L30fpJCyCR8jSJSHV2TUHzO01TltEb0OHm'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
filename=open(argfile,'r')
f=filename.readlines()
filename.close()
 
while True:
    for line in f:
        curtime= time.strftime("%H:%M:%S")
        curdate= time.strftime("%x")
        api.update_status("{0}---{1}, {2}".format(curdate,curtime,line)) 
        TimeToSleep = randint(780,1200)
        time.sleep(TimeToSleep)#Tweet every 15 minutes