import tweepy
import time
import random, os



consumer_key = 'FVxmHgq4SpfM6A0kdN8JRr3Rd'
consumer_secret = 'yshimrDc4edmltLhvjOmsaMAv8cf7S5VxgOuY2i17omeccbsLb'

key = '1037431700081582085-qbhNIDPJo0eWxdqm70BoFKJ3DAkvcV'
secret = 'd1JKEMfLQcRiyEvf9s1IBCtjIqCbEa5j4TeoRcocesvIV'



# Authentication

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
print("\nTwitter authentication was successfull!")



file_name = 'last_seen.txt'

def Read_lastSeen(file_name):
    file_read = open(file_name,'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_lastSeen(file_name, last_seen_id ):
    file_write = open(file_name,'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return 


#cat class 

def cat_pic():
    path = r"/Users/videet/Desktop/Water Bot/cats"
    cat = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
    ])
    cat_path = "cats/" + cat
    return cat_path

# load image

#print(type(cat))


def reply():
    tweets = api.mentions_timeline(Read_lastSeen(file_name),tweet_mode='extended')
    for tweet in reversed(tweets):
        if '#pheribot' in tweet.full_text.lower():
            print(str(tweet.id) + ' -  ' + tweet.full_text)
            cat = cat_pic()
            #print(cat)
            api.update_with_media(cat,'@' + tweet.user.screen_name + ' Please Drink water uwu ', in_reply_to_status_id=tweet.id, auto_populate_reply_metadata=True)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_lastSeen(file_name, tweet.id)

while True:
    reply()
    time.sleep(15)

