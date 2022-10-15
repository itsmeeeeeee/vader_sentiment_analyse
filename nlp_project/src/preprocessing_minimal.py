import json
import re
import emoji
from pathlib import Path



__file__="preprocessing_minimal.py"
DATA_DIR="../data/"

path_data=(Path(__file__)/f"{DATA_DIR}preprocessed_minimal.txt").resolve()

path_to_clean_data=(Path(__file__)/f"{DATA_DIR}tweets_text_only.json").resolve()




def clean_txt(text):

    # Clean the data
    
    text = re.sub(r'@[A-Za-z0-9]+', '', text) #removes @mentions
    text = re.sub(r'#', '', text) #removes the '#' symbol
    text = re.sub(r'RT[\s]+', '', text) #removes etweets
    text = re.sub(r'https?:\/\/\S+', '', text) #removes hyperlink
    text = re.sub(r'((www\.[^\s]+)|(https?://[^\s]+))', "", text) #Remove special html characters such as website link, http/https/www
    text = re.sub(r'["#&\()*+,-/:;@[\]^_`{|}~ξ]', "", text) #Remove Punctuations special characters such as % & ξ
    text = re.sub(r'()', "",text)

    return text
    
def remove_double_tweets(data):

    # Read the tweets and remove double
    all_tweets=[]
    with open(data,'r',encoding="UTF-8") as file:
        #all_tweets=[]
        obj = json.load(file)
        
        for tweets_obj in obj:
            all_tweets.append(tweets_obj['Tweet Text'])
    return list(set(all_tweets))

def cleanedTweets(lists_of_tweets):
    all_tweets=[]
    for tweet in lists_of_tweets:
        
        all_tweets.append(clean_txt((tweet)))
        
    # removes duplicate blanks
    all_tweets=[" ".join(line.split()) for line in all_tweets]

    return all_tweets
        
       
def preprocess_data(c_tweets):

    # save the preprocessed data in a text file
    
    with open(path_data, 'w',encoding="UTF-8") as f:
        for tweet in c_tweets:
            f.write(tweet)
            f.write('\n')
            

        
#cleaned_tweets=cleanedTweets(path_to_clean_data)
list_of_tweets=remove_double_tweets(path_to_clean_data)
cleaned_tweets=cleanedTweets(list_of_tweets)
#print(len(cleaned_tweets))

preprocess_data(cleaned_tweets)





    


        
        




