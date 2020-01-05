# import os
# import sys
# sys.path.insert(0, os.path.realpath(os.path.dirname(__file__)))
# os.chdir(os.path.dirname(__file__))

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sqlite3
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from unidecode import unidecode
import time
from threading import Lock, Timer
import pandas as pd 
from config import stop_words
from config1 import ckey, csecret, atoken, asecret
import regex as re 
from collections import Counter
import string
import pickle
import itertools
from textblob import TextBlob 
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
# from googletrans import Translator

# translator = Translator()
analyzer = SentimentIntensityAnalyzer()

#consumer key, consumer secret, access token, access secret.
ckey=ckey
csecret=csecret
atoken=atoken
asecret=asecret

conn = sqlite3.connect('twitter3.db', isolation_level=None, check_same_thread=False)

c = conn.cursor()

def create_table():
    try:
        # http://www.sqlite.org/pragma.html#pragma_journal_mode
        # Allows concurrent write and reads
        c.execute("PRAGMA jouranl_mode=wal")
        # c.execute("PRAGMA wal_checkpoint=TRUNCATE")
        c.execute("PRAGMA journal_mode=PERSIST")


        c.execute("CREATE TABLE IF NOT EXISTS sentiment(id INTEGER PRIMARY KEY AUTOINCREMENT, unix INTERGER, tweet TEXT, sentiment REAL)")
        # Key-value table for random stuff
        c.execute("CREATE TABLE IF NOT EXISTS misc(key TEXT PRIMARY KEY, value TEXT)")
        # id on index, both as DESC
        c.execute("CREATE INDEX id_unix ON sentiment (id DESC, unix DESC)")
        # Full-text search table
        c.execute("CREATE VIRTUAL TABLE sentiment_fts USING fts5(tweet, content=sentiment, content_rowid=id, prefix=1, prefix=2, prefix=3)")
        # trigger will automatically update out table when row is inserted
        # requires additonal triggers on update and delete
        c.execute("""
            CREATE TRIGGER sentiment_insert AFTER INSERT ON sentiment BEGIN
                INSERT INTO sentiment_fts(rowid, tweet) VALUES (new.id, new.tweet);
                END
            """)
   
    except Exception as e:
        print(str(e))
create_table()

# create lock
lock = Lock()


# 'created_at': 'Sun Nov 03 22:06:03 +0000 2019', 
# 'id': 1191114339496779776, 
# 'id_str': '1191114339496779776', 
# 'text': '@AuthorCharish @JackHarbon Now I need to make a happy playlist!🎵🎶🎵', 
# 'display_text_range': [27, 66], 
# 'source': '<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>', 
# 'truncated': False, 
# 'in_reply_to_status_id': 1191035796893118469, 
# 'in_reply_to_status_id_str': '1191035796893118469', 
# 'in_reply_to_user_id': 457829199, 
# 'in_reply_to_user_id_str': '457829199', 
# 'in_reply_to_screen_name': 'AuthorCharish', 
# 'user': {'id': 43488965, 'id_str': '43488965', 'name': 'Patti L', 'screen_name': 'bkwmn1992', 'location': 'Tucson, AZ', 
#         'url': None, 'description': 'Reader, wife, librarian, coloring aficionado, both nerd & geek, friend, daughter, sister, aunt, feminist, transplanted Michigander.', 
#         'translator_type': 'none', 'protected': False, 'verified': False, 'followers_count': 1285, 'friends_count': 1731, 
#          'listed_count': 71, 'favourites_count': 105566, 'statuses_count': 20723, 'created_at': 'Sat May 30 05:45:03 +0000 2009', 
#          'utc_offset': None, 'time_zone': None, 'geo_enabled': True, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 
#         'profile_background_color': '000000', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme5/bg.gif', 
#          'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme5/bg.gif', 'profile_background_tile': False,
#          'profile_link_color': '4A913C', 'profile_sidebar_border_color': '000000', 'profile_sidebar_fill_color': '000000', 'profile_text_color': '000000', 'profile_use_background_image': False,
#          'profile_image_url': 'http://pbs.twimg.com/profile_images/1314997357/Photo_7_fr_Brad_normal.JPG', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1314997357/Photo_7_fr_Brad_normal.JPG',
#          'default_profile': False, 'default_profile_image': False, 'following': None, 'follow_request_sent': None, 'notifications': None}, 'geo': None, 'coordinates': None, 'place': None, 'contributors': None,
#          'is_quote_status': False, 'quote_count': 0, 'reply_count': 0, 'retweet_count': 0, 'favorite_count': 0, 'entities': {'hashtags': [], 'urls': [], 'user_mentions': [{'screen_name': 'AuthorCharish', 
#          'name': 'Charish Reid--Author', 'id': 457829199, 'id_str': '457829199', 'indices': [0, 14]}, {'screen_name': 'JackHarbon', 'name': 'jack harbon 🌸', 'id': 2878406147, 'id_str': '2878406147', 
#                                        

# class Tweet():
#     def __init__(self, unix, text, user, sentiment, description, location):
#         self.unix = unix
#         self.text = text
#         self.sentiment = sentiment
#         self.user = user
#         self.description = description
#         self.location = location


class listener(StreamListener):

    data = []
    lock =Lock()

    def __init__(self, lock):
        self.lock = lock
        self.save_in_database()

        super().__init__

    def save_in_database(self):

        Timer(1, self.save_in_database).start()

        with self.lock:
            if len(self.data):
                c.execute('BEGIN TRANSACTION')
                try:
                    c.executemany("INSERT INTO sentiment (unix, tweet, sentiment) VALUES (?, ?, ?)", self.data)
                except:
                    pass
                c.execute('COMMIT')

                self.data = []

    def on_data(self, data):
        try:
            data = json.loads(data)

            # print(data)
            if 'truncated' not in data:
                return True
                # print(data)
            if data['truncated']:
                tweet = unidecode(data['extended_tweet']['full_text'])
            else:
                tweet = unidecode(data['text'])

            # print(tweet)
            # if data.lang == 'en':
            #     return data

            # else:
            #     data = translatorl.translate(data['text'])
            
            
            time_ms = data['timestamp_ms']
            vs = analyzer.polarity_scores(tweet)
            sentiment = vs['compound']
            print(time_ms, tweet, sentiment)

            with self.lock:
                self.data.append((time_ms, tweet, sentiment))

        except KeyError as e:
            print(str(e))
        return True

    def on_error(self, status):
        print(status)


    
stop_words.append('')
blacklist_counter = Counter(dict(zip(stop_words, [1000000] * len(stop_words))))

punctuation =[str(i) for i in string.punctuation]
split_regex = re.compile("[ \n" + re.escape("".join(punctuation))+']')


def map_nouns(col):
        return [word[0] for word in TextBlob(col).tags if word[1] == u'NNP']


def generate_trending():
    try:
        df = pd.read_sql("SELECT * FROM sentiment ORDER BY id DESC, unix DESC LIMIT 10000", conn)
        df['nouns'] = list(map(map_nouns, df['tweet']))

        tokens = split_regex.split(' '.join(list(itertools.chain.from_iterable(df['nouns'].values.tolist()))).lower())

        trending = (Counter(tokens) - blacklist_counter).most_common(10)

        trending_with_sentiment = {}
        for term, count in trending:
            df = pd.read_sql("SELECT sentiment.* FROM sentiment_fts fts LEFT JOIN sentiment ON fts.rowid = sentiment.id WHERE fts.sentiment_fts MATCH ? ORDER BY fts.rowid DESC LIMIT 1000", conn, params=(term,))
            trending_with_sentiment[term] = [df['sentiment'].mean(), count]


        with lock:
            c.execute('BEGIN TRANSACTION')
            try:
                c.execute("REPLACE INTO misc (key, value) VALUES ('trending', ?)", (pickle.dumps(trending_with_sentiment),))
            except:
                pass
            c.execute('COMMIT')

    except Exception as e:
        with open('errors.txt', 'a') as f:
            f.write(str(e))
            f.write('\n')

    finally:
        Timer(5, generate_trending).start()

Timer(1, generate_trending).start()



while True:

    try:
        auth = OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret)
        twitterStream = Stream(auth, listener(lock))
        twitterStream.filter(languages=['en'], track=["a","e","i","o","u"])
    except Exception as e:
        print(str(e))
        time.sleep(5)