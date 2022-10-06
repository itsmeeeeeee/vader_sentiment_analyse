import json
from lib2to3.pgen2 import token
import re
import emoji
import spacy
from pathlib import Path

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.tokenizer import Tokenizer



__file__="preprocessing.py"
DATA_DIR="../data/"

path_data=(Path(__file__)/f"{DATA_DIR}preprocessed_minimal.txt").resolve()

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
    #text = re.sub(r'#', '', text) #removes the '#' symbol
    text = re.sub(r'RT[\s]+', '', text) #removes etweets
    text = re.sub(r'https?:\/\/\S+', '', text) #removes hyperlink
    #text = re.sub(emoji.get_emoji_regexp(), r"", text) #removes emojisCor
    #text = text.encode("ascii", "ignore")
    #text= text.decode()
    text = re.sub(r'((www\.[^\s]+)|(https?://[^\s]+))', "", text) #Remove special html characters such as website link, http/https/www
    text = re.sub(r'["#&\()*+,-/:;@[\]^_`{|}~ξ]', "", text) #Remove Punctuations special characters such as % & ξ
    text = re.sub(r'()', "",text)

    return text
    
def cleanedTweets(data):

    # Read the tweets and clean it 
    
    with open(data,'r',encoding="UTF-8") as file:
        obj = json.load(file)
        lines=[]
        for tweets_obj in obj:
            listofwords=[]
            for string in tweets_obj['Tweet Text'].split():
                listofwords.append(string.lower())
            lines.append(clean_txt((" ".join(listofwords))))
        
        # removes duplicate blanks
        lines=[" ".join(line.split()) for line in lines]
       

        return lines
        
       
def preprocess_data(c_tweets):

    # save the preprocessed data in a text file
    
    with open(path_data, 'w',encoding="UTF-8") as f:
        for tweet in c_tweets:
            #remove_sw=remove_stw(tweet)
            #lemmatisierung=lemma_(remove_sw)
           
            f.write(tweet)
            f.write('\n')
            

        
#cleaned_tweets=cleanedTweets(path_to_clean_data)

#preprocess_data(cleaned_tweets)

t="$ETH There are too many tokens, not enough use cases and the economy is lacking. People en businesses don't have enough money and too much debt."

doc=nlp(clean_txt(t))
print("Tweet: ", clean_txt(t))
tokens=[token.text for token in doc]
print("Tokenisierung: ",tokens)
print("Stoppwörter Enfernen: ",remove_stw(" ".join(tokens)) )
print("Lemmatisierung: ",lemma_(remove_stw(" ".join(tokens))))
#remove_stw()



    


        
        




