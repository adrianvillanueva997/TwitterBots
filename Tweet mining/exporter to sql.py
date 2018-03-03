import re
import csv
import sqlite3


def readCSV():
    with open('@KosmonavtRed_tweets.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        tweets = []
        for row in reader:
            tweets.append(row['text'])
            # print(row['text'])
        return tweets


def regex(tweets):
    regex = r'(@[A-Za-z0-9_]+)'
    updatedList = []
    for tweet in tweets:
        newTweet = re.sub(regex, '', tweet)
        # print(re.sub(regex, '', tweet))
        newTweet = str(newTweet).replace('RT : ', '')
        newTweet = str(newTweet).replace('\"', '\"\"')
        newTweet = str(newTweet).replace('\'', '\'\'')
        updatedList.append(newTweet)
        print(newTweet)
    return updatedList


def tweetExporter(tweets):
    try:
        dataBase = 'TweetsDB.db'
        db = sqlite3.connect(dataBase)
        for tweet in tweets:
            query = 'INSERT into Wikired_Data (Text) VALUES ' + '(\'' + tweet + '\')'
            db.execute(query)
            db.commit()
            print('Insertado: ' + tweet)
        db.close()
    except Exception as e:
        print(e)


def main():
    try:
        tweets = readCSV()
        tweets = regex(tweets)
        tweetExporter(tweets)
    except Exception as e:
        print(e)


main()
