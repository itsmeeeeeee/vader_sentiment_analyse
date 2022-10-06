import tweepy 
import json

def scrape(words, numtweet, scraped_data):
    # Make an API call
    tweets = tweepy.Cursor(api.search_tweets, q=words, lang="en", tweet_mode='extended').items(numtweet)
    list_tweets = [tweet for tweet in tweets]

    i = 1

    for tweet in list_tweets:
        
        username = tweet.user.screen_name
        description = tweet.user.description
        location = tweet.user.location
        following = tweet.user.friends_count
        followers = tweet.user.followers_count
        totaltweets = tweet.user.statuses_count
        retweetcount = tweet.retweet_count
        hashtags = tweet.entities['hashtags']

        try:
            text = tweet.retweeted_status.full_text
        except AttributeError:
            text = tweet.full_text
        hashtext = list()
        for j in range(0, len(hashtags)):
            hashtext.append(hashtags[j]['text'])

        ith_tweet = [username, description, location, following, followers, totaltweets, retweetcount, text, hashtext]
        printtweetdata(i, ith_tweet, scraped_data)

        i = i+1


def printtweetdata(n, ith_tweet, scraped_data):

    d = {"Tweet Scraped" : n, "Username": ith_tweet[0], "Description" : ith_tweet[1], "Location" : ith_tweet[2], "Following Count" : ith_tweet[3], "Follower Count" : ith_tweet[4], 
         "Total Tweets" : ith_tweet[5], "Retweet Count" : ith_tweet[6], "Tweet Text" : ith_tweet[7], "Hashtags Used" : ith_tweet[8]}

    print(f"Tweet scrapped: {n}")
    print(f"Username: {ith_tweet[0]}")
    print(f"Description: {ith_tweet[1]}")
    print(f"Location: {ith_tweet[2]}")
    print(f"Following Count: {ith_tweet[3]}")
    print(f"Follower Count: {ith_tweet[4]}")
    print(f"Total Tweets: {ith_tweet[5]}")
    print(f"Retweet Count: {ith_tweet[6]}")
    print(f"Tweet Text: {ith_tweet[7]}")
    print(f"Hashtags Used: {ith_tweet[8]}")
    
    scraped_data.append(d)

    # storing tweets as a json-file
    with open(f'/Users/saberklai/Documents/Projekt_SentAn/tweets_try01.json', 'w') as outfile:
        json.dump(scraped_data, outfile, indent=4)
  

# Loading the file with the API keys
f = open('auth.json')
data = json.load(f)
# Getting API keys: we need to have a Twitter Developer Account and only with it, we can get keys to scrape tweets.
acces_token = data["access_token"]
access_token_secret = data["access_token_secret"]
# Import and prepare API object: pass api_key, secret, access_token, access_token_secret into the OAuthHandler.
api_key = data["api_key"]
api_key_secret = data["api_key_secret"]

auth = tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(acces_token, access_token_secret)
api = tweepy.API(auth)


print("Enter Twitter Hashtag to search for:")
words = input()

print("Enter Number of tweets to be scraped:")
numtweet = int(input())

scraped_data = []
print("Fetching tweets...")

scrape(words, numtweet, scraped_data)
print("Scraping has completed!")
