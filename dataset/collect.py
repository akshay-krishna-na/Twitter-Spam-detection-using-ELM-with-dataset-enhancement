import os
import tweepy as tw
import csv
from datetime import date

consumer_key= 'kwKnXhRyrUCglyGs1XBdzl7nF' #api_key
consumer_secret= 'IZhS4F1xZRk4TiMDwVfxbWuBoOWa0txljpf0tmkU9OWxswXuBw' #api_secret_key
access_token= '835335689793220613-MmjXFl3Fbls48mJhZr6Mc4BrAaH001m'
access_token_secret= 'u4KHEBdTyzY7fKVoOevNJsNDTLXmuBFFeeSJ0yRJpy2vk'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

#api.update_status("hi")






#new_search = search_words + " -filter:retweets"

#tweets = tw.Cursor(api.home_timeline).items(1000)
query='is'
tweets = tw.Cursor(api.search,q=query,lang='en').items(1000)


count=0

with open('tweets.csv', 'w+', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name","Account Age","Tweet count","List count","Location","Followers","Following","Favorites","ID","Created at","Tweet","Retweet count","Likes/Favs","Hashtag count","URL count","Tweet length","Place of tweet","mention count","tweet source"])
    for tweet in tweets:
        count+=1
        if 'retweeted_status' in tweet._json:
            continue
            #users_locs = [tweet.user.screen_name ,tweet.text,tweet.user.location]
            #writer.writerow(users_locs)
        else:
            hashtagc=len(tweet.entities['hashtags'])
            urlc=len(tweet.entities['urls'])
            mentionc=len(tweet.entities['user_mentions'])
            tweet_place=''

            if(tweet.place):
                tweet_place=tweet.place.full_name

            today = date.today()
            age = today.year - tweet.user.created_at.year
            users_locs = [tweet.user.screen_name,age,tweet.user.statuses_count,tweet.user.listed_count,tweet.user.location,tweet.user.followers_count,tweet.user.friends_count,tweet.user.favourites_count,tweet.id,tweet.created_at,tweet.text,tweet.retweet_count,tweet.favorite_count,hashtagc,urlc,len(tweet.text),tweet_place,mentionc,tweet.source]
            writer.writerow(users_locs)
print("Total tweets pulled = "+str(count))
