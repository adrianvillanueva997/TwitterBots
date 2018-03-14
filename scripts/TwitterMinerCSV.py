import tweepy  # https://github.com/tweepy/tweepy
import csv
from tweepy import OAuthHandler

# Twitter API credentials
consumer_key = '5XDMHKiHvl10spl6DDd9dCwkI'
consumer_secret = 'vrM1UBlmQRKErvpRksGEp1EmbdhSBrnB6jKF2o8ueCmmtZ42Qu'
access_token = '4251643571-q7tKcUwyEqUDc5xm4xbYzR3MpdVmzhoY0E5QSLn'
access_secret = 'Wv3HUfSZGZKBAehdjDsdCd5l2YiKe1Ka2jFhjopCpWtzY'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

amountOfTweets = 200
accountName = '@KosmonavtRed'


def storeTweets(screen_name, numberOfTweets):
    api = tweepy.API(auth)  # Twitter only allows access to a users most recent 3240 tweets with this method
    alltweets = []  # initialize a list to hold all the tweepy Tweets
    new_tweets = api.user_timeline(screen_name=screen_name,
                                   count=numberOfTweets)  # make initial request for most recent tweets (200 is the maximum allowed count)
    alltweets.extend(new_tweets)  # save most recent tweets
    oldest = alltweets[-1].id - 1  # save the id of the oldest tweet less one

    while len(new_tweets) > 0:  # keep grabbing tweets until there are no tweets left to grab
        print("getting tweets ")
        new_tweets = api.user_timeline(screen_name=screen_name, count=numberOfTweets,
                                       max_id=oldest)  # all subsiquent requests use the max_id param to prevent duplicates
        alltweets.extend(new_tweets)  # save most recent tweets
        oldest = alltweets[-1].id - 1  # update the id of the oldest tweet less one
        print("...%s tweets downloaded" % (len(alltweets)))

    outtweets = [[tweet.id_str, tweet.created_at, tweet.text] for tweet in
                 alltweets]  # transform the tweepy tweets into an Array to populate the csv

    with open('%s_tweets.csv' % screen_name, mode='w', encoding='utf-8') as f:  # write the csv
        print("tweets.csv created")
        writer = csv.writer(f)
        writer.writerow(["id", "created_at", "text"])
        writer.writerows(outtweets)
        print("Done!")
    pass


def main():
    storeTweets(accountName, amountOfTweets)  # pass in the username of the account you want to download


main()
