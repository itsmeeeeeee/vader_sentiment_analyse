import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from pathlib import Path



__file__="WordCloud.py"
DATA_DIR="../data/"

path_data_minimal_preprocess=(Path(__file__)/f"{DATA_DIR}preprocessed_minimal.txt").resolve()
path_data_maximal_preprocess=(Path(__file__)/f"{DATA_DIR}preprocessed_maximal.txt").resolve()
#print(path_data_minimal_preprocess)

# Read the csv file as a dataframe
df = pd.read_csv(path_data_maximal_preprocess, delimiter=" \t", engine='python') #filepath, delimiter (alias for sep):Tab-delimited, engine: Parser engine to use
df.columns = ['Tweets'] #label the coloumn of the actual tweets 'Tweets'
#print(df)

words = ''
stopwords = set(STOPWORDS)

for val in df['Tweets']:
    
    val = str(val)
    tokens = val.split()

    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()

    words += " ".join(tokens) + " "


wordcloud = WordCloud(width = 800, height = 800,
                background_color ='gray',
                stopwords = stopwords,
                min_font_size = 12).generate(words) #generate wordcloud from the words

plt.figure(figsize = (7, 7), facecolor = None) # Create a new figure, or activate an existing figure / figsize: Width, height in inches / facecolor: The background color.
plt.imshow(wordcloud) #Display data as an image, i.e., on a 2D regular raster.
plt.axis("off") #Turn off axis lines and labels
plt.tight_layout(pad = 0) # Adjust the padding between and around subplots / pad: This parameter is used for padding between the figure edge and the edges of subplots, as a fraction of the font size.
plt.show() #Display all open figures.