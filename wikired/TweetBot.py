import markovify
import tweepy
from tweepy import OAuthHandler
from sqlalchemy import create_engine


def connectDatabase():
    engine = create_engine("mysql+mysqldb://USER:" + 'PASS' + "@YOURIPGOESHERE:PORT/DATABASE?charset=utf8mb4",
                           encoding='utf-8')
    connect = engine.connect()
    return connect


def getTweets(con):
    result = con.execute('SELECT Text FROM Wikired_Data')
    tweetList = []
    for tweet in result:
        tweetList.append(str(tweet['Text']))
    return tweetList


def generateTweet(tweetList):
    text_model = markovify.NewlineText(tweetList)
    tweet = text_model.make_short_sentence(280)
    return tweet


def publishTweet(tweet, con):
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_secret = ''

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    tweetBot = tweepy.API(auth)
    try:
        print(tweet)
        tweetBot.update_status(tweet)
        query = 'INSERT into WikiRed (Text) VALUES ' + '(\'' + tweet + '\')'
        con.execute(query)
    except Exception as e:
        print(e)


def main():
    con = connectDatabase()
    tweetList = getTweets(con)
    generateTweet(tweetList)
    tweet = generateTweet(tweetList)
    publishTweet(tweet, con)

    con.close()


if __name__ == '__main__':
    main()
