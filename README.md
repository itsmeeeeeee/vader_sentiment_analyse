# vader_sentiment_analyse# 
Sentimentanalyse im Kontext von Tweets

Dieses Projekt wird uns durch den Prozess der Ausführung von Stimmungsanalysen für eine bestimmte Datenmenge führen. Die Daten bestehen aus einem Korpus (Sammlung) von Tweets, die Ethereum (Kryptowährung) betreffen. Der Korpus wird aufgebaut durch „scraping“ Tweets auf Twitter.

Sentiment-Analyse ist eine Technik, die die zugrunde liegende Stimmung in einem Textstück erkennt. Es ist der Prozess der Klassifizierung von Text als positiv, negativ oder neutral. Techniken des maschinellen Lernens werden verwendet, um ein Textstück zu bewerten und die Stimmung dahinter zu bestimmen.

Die folgenden Aufgaben werden in diesem Projekt ausgeführt:

* Twitter-Scraping anhand tweepy
* Verwendung von NLP, um Textdaten vorzubereiten und zu bereinigen (Spacy, NLTK)
* Stimmungsanalyse mit VADER
* Erstellung einer "WordCloud" anhand wordcloud, matplotlib und pandas


## Twitter-Scraping

Wir müssen auf die Twitter-API zugreifen, um die Daten zu sammeln, die wir von Twitter benötigen. Dazu müssen Sie Zugriff erhalten, und dies kann durch Erstellen einer App im Twitter-Entwicklerportal erfolgen.
Führen Sie dazu die folgenden Schritte aus:

* Besuchen Sie die Twitter-Website des Entwicklers und beantragen Sie ein Entwicklerkonto. Sie benötifen dafür einen Twitter-Account
* Nach der Genehmigung können Sie die App jetzt in der Entwicklungsumgebung erstellen. Weitere Informationen finden Sie unter diesem Link: [I'm an inline-style link](https://developer.twitter.com/en/docs/apps/overview)
* Um auf die API zugreifen zu können, benötigen Sie 4 verschiedene geheime Token-Schlüssel, die Sie auf der Registerkarte "Schlüssel und Token" im Abschnitt Projekte und Apps in Ihrer Entwicklerumgebung finden.

Die Module, die Sie hier benötigen, sind: tweepy and json
* pip install tweepy
* json ist ein eingebautes Modul in Python, Sie müssen es nicht mit pip installieren.

### Vorverarbeitung der Textdaten

Für die Vorverarbeitung der Daten wird Spacy und Regex eigesetzt. Die drei Vorverarbeitungsschritte sind: Tokenisierung, Stoppwörter Entfernung,Lemmatisierung.
Regex wird in dem Projekt angewendet, um die Tweets zu reinigen bzw. Sonderzeichen wie z.B. @mentions, hyperlinks, website link zu entfernen.
Um mit SpaCy und ReGex in Python arbeiten zu können, müssen wir zunächst einige Bibliotheken mit pip installieren.

How to install SpaCy:
* pip install -U pip setuptools wheel
* pip install -U spacy
* python -m spacy download en_core_web_sm

How to install ReGex:
* pip install regex



#### VADER (Valence Aware Dictionary and sEntiment Reasoner)

VADER ist ein lexikon- und regelbasiertes Sentiment-Analyse-Tool, das speziell auf Stimmungen abgestimmt ist, die in sozialen Medien ausgedrückt werden. Es wird für die Stimmungsanalyse von Text verwendet, der sowohl die Polaritäten (positiv / negativ) aufweist. VADER wird auch verwendet, um zu quantifizieren, wie viel positive oder negative Emotion der Text hat und auch die Intensität der Emotion. Es verwendet eine Liste von lexikalischen Merkmalen (z. B. Wort), die gemäß ihrer semantischen Ausrichtung als positiv oder negativ gekennzeichnet sind, um die Textstimmung zu berechnen.
Weitere Informationen finden Sie unter diesem Link: [I'm an inline-style link](https://pypi.org/project/vader-sentiment/)

How to install vaderSentiment:
* pip install vaderSentiment

Vorteile der Verwendung von VADER:
* Es funktioniert gut mit Text vom Typ Social Media, lässt sich aber leicht auf mehrere Domänen verallgemeinern
* Es werden keine Trainingsdaten benötigt. Es basiert auf einem von Menschen geschaffenen Stimmungslexikon
* Es leidet nicht stark unter einem Geschwindigkeits-Leistungs-Kompromiss.

##### WordCloud

Wordcloud ist eine Visualisierungstechnik, um die Häufigkeit von Wörtern in einem Text darzustellen, wobei die Größe des Wortes seine Häufigkeit darstellt.
Um mit Wordclouds in Python arbeiten zu können, müssen wir zunächst einige Bibliotheken mit pip installieren. Sie sind pandas (zur Verarbeitung und Analyse von Daten), Matplotlib (zum Generieren von Plots) und schließlich Wordcloud (zum Generieren von Wordclouds).

How to install WordCloud, pandas und matplotlib:
* pip install wordcloud
* pip install pandas
* pip install matplotlib
