# Twitter Sentiment Analysis With Dash

## Objective

To build a interactive dashboard using tweets from twitter API that have been processed using nlp (natural language processing).  Once the tweets have been processed create a dashboard showing tweet sentiments, volume, sentiment totals, most recent tweets.  The dashboard can be created entirely in python using dash.

## Purpose/Goal

Twitter API provides a free account which allows users to gather 1% of tweets.  The project focused on showing tweet sentiments using [Vader Sentiment Analysis](https://github.com/cjhutto/vaderSentiment) by word search to gain intelligence of overall users of twitter associated with the word search.  Provide the intelligence in interactive dashboard using Dash https://plot.ly/dash/.

## Conclusion

Twitter tweets provide a great source of user information that can be mined and cleaned to gain insightful information.  There are many different data points that can be use to create many different type of scopes for the project.

## Technologies Used

- Python
- Sqlite3

## Modules Used

- Pandas
- Dash
- Tweepy
- Json
- Vader Sentiment 
- Unidecode
- Time
- Threading
- Regex
- Collections
- String
- Itertools
- TextBlob
- Nltk

## Screenshot for Dashboard

<img src="https://github.com/ktung1189/Sentiment_Analysis_With_Dash/blob/master/Images/tweet_graph.png" alt='Live_Twitter_Dashboard'>

<img src="https://github.com/ktung1189/Sentiment_Analysis_With_Dash/blob/master/Images/tweet_pie.png" alt='Live_Twitter_Dashboard'>

## To Run the Application

A Twitter API will be need which can  be download https://developer.twitter.com/en/docs/basics/getting-started and Dash will be required https://anaconda.org/conda-forge/dash.