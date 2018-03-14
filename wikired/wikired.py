import markovify
import tweepy
from tweepy import OAuthHandler
from wikired import config


def connectDatabase():
    engine = config.engine
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
    auth = OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_secret)
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



if __name__ == '__main__':
    main()
