import tweepy
import json
import io
from tweepy import OAuthHandler

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

amountOfTweets = 200
accountName = '@ACOUNTGOESHERE'

api = tweepy.API(auth)

def storeTweets(screen_name,numberOfTweets):
    alltweets = []

    new_tweets = api.user_timeline(screen_name=screen_name, count=numberOfTweets) # make initial request for most recent tweets (200 is the maximum allowed count)

    alltweets.extend(new_tweets) # save most recent tweets

    oldest = alltweets[-1].id - 1 # save the id of the oldest tweet less one

    while len(new_tweets) > 0: # keep grabbing tweets until there are no tweets left to grab

        new_tweets = api.user_timeline(screen_name=screen_name, count=numberOfTweets, max_id=oldest) # all subsiquent requests use the max_id param to prevent duplicates

        alltweets.extend(new_tweets) # save most recent tweets

        oldest = alltweets[-1].id - 1 # update the id of the oldest tweet less one
        print("...%s tweets downloaded so far" % (len(alltweets)))

    file = io.open('tweet.json', 'w',encoding='utf-8') # write tweet objects to JSON
    print("Writing tweets to JSON please wait...")
    for status in alltweets:
        file.write(status._json, file, sort_keys=True, indent=4)
        print("exporting tweets to json... ")
    print("Done!")


def main():
    storeTweets(accountName,amountOfTweets)

main()

