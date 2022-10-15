from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Create a variable to hold the VADER lexicon object 
analyzer = SentimentIntensityAnalyzer()

# Preview the lexicon contents
#print(analyzer.lexicon)


__file__="Vader_final.py"
DATA_DIR="../data/"

path_data_minimal_preprocess=(Path(__file__)/f"{DATA_DIR}preprocessed_minimal.txt").resolve()
path_data_maximal_preprocess=(Path(__file__)/f"{DATA_DIR}preprocessed_maximal.txt").resolve()

#Reading the txt file as a dataframe
#df = pd.read_csv('C:/Users/aldi_/OneDrive/Desktop/nlp projekt/src (1)/data/preprocessed_tweets.txt', delimiter=" \t", engine='python')
#Adding a column with the title "Tweets"
df=df = pd.read_csv(path_data_minimal_preprocess, delimiter=" \t", engine='python')
df.columns = ['Tweets']


senti_scores = []

for i in range(df['Tweets'].shape[0]):

# This method gives a sentiment dictionary: it takes in a string and returns a dictionary of scores in each of four categories: neg, neu, pos, comp.
# The Positive, Negative and Neutral scores represent the proportion of text that falls in these categories. Hence all these should add up to 1.
# The Compound score is a metric that calculates the sum of all the lexicon ratings which have been normalized between -1(most extreme negative) and +1 (most extreme positive).

    compound = analyzer.polarity_scores(df['Tweets'][i])["compound"]
    pos = analyzer.polarity_scores(df['Tweets'][i])["pos"]
    neu = analyzer.polarity_scores(df['Tweets'][i])["neu"]
    neg = analyzer.polarity_scores(df['Tweets'][i])["neg"]
    
    if compound >= 0.05:
            ov = "POSITIVE"
    elif compound <= -0.05:
            ov = "NEGATIVE"
    elif compound > -0.05 and compound < 0.05: # hier an else-statement will also do
            ov = "NEUTRAL"

    senti_scores.append({"Compound": compound,
                       "Positive": pos,
                       "Negative": neg,
                       "Neutral": neu,
                       "Overall": ov
                  })


sentiments_score = pd.DataFrame.from_dict(senti_scores)
df = df.join(sentiments_score)
print (df)

result_sentiments = df['Overall'].value_counts()
print(result_sentiments)

explode = (0.05, 0.05, 0.05)
x = result_sentiments.plot(kind='pie', autopct='%1.0f%%', title='The distribution of the overall sentiments about Ethereum', explode=explode)
x.plot()
plt.show()


