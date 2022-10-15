import json
import re
import emoji
import spacy
from pathlib import Path
from spacy.tokenizer import Tokenizer



__file__="preprocessing_maximal.py"
DATA_DIR="../data/"

path_data=(Path(__file__)/f"{DATA_DIR}preprocessed_maximal.txt").resolve()

path_to_clean_data=(Path(__file__)/f"{DATA_DIR}tweets_text_only.json").resolve()


#loading the english language small model of spacy
nlp = spacy.load("en_core_web_sm")


stopwords=nlp.Defaults.stop_words



def remove_stw(tweet):
    doc=nlp(tweet)
    filtered_sentences=[]
    
    # Tokenizing
    tokens=[token.text for token in doc]
    for word in tokens:
        if word not in stopwords:
            filtered_sentences.append(word)
    return " ".join(filtered_sentences)




def lemma_(tweet):
    
    #Lemmatizing
    
    doc = nlp(tweet)
    return " ".join([token.lemma_ for token in doc])




def clean_txt(text):

    # Clean the data
    
    text = re.sub(r'@[A-Za-z0-9]+', '', text) #removes @mentions
    text = re.sub(r'RT[\s]+', '', text) #removes etweets
    text = re.sub(r'https?:\/\/\S+', '', text) #removes hyperlink
    text = re.sub(emoji.get_emoji_regexp(), r"", text) #removes emojisCor
    text = text.encode("ascii", "ignore")
    text= text.decode()
    text = re.sub(r'((www\.[^\s]+)|(https?://[^\s]+))', "", text) #Remove special html characters such as website link, http/https/www
    text = re.sub(r'["?!$#&\()*+,-/:;@[\]^_`{|}~ξ]', "", text) #Remove Punctuations special characters such as % & ξ
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
    
def cleanedTweets(tweets):

    # clean tweets
    
    all_tweets=[]
    for tweet in tweets:
        listofwords=[]
        for token in tweet.split():
            listofwords.append(token.lower())
        all_tweets.append(clean_txt((" ".join(listofwords))))
        
        # removes duplicate blanks
    all_tweets=[" ".join(line.split()) for line in all_tweets]
       

    return all_tweets
        
       
def preprocess_data(c_tweets):

    # save the preprocessed data in a text file
    
    with open(path_data, 'w',encoding="UTF-8") as f:
        for tweet in c_tweets:
            remove_sw=remove_stw(tweet)
            lemmatisierung=lemma_(remove_sw)
           
            f.write(lemmatisierung)
            f.write('\n')
            

tweets=remove_double_tweets(path_to_clean_data)     
cleaned_tweets=cleanedTweets(tweets)
#print(cleaned_tweets)

preprocess_data(cleaned_tweets)