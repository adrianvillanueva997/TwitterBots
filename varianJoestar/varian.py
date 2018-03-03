import markovify
import basc_py4chan
import re
import tweepy, time
from tweepy import OAuthHandler
import pymysql
from random import randint

hostname = ''
user = ''
password = ''
database = ''
port = 3306

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
tweetBot = tweepy.API(auth)

tweet = ''

boards = 'pol'


def getShit():
    try:
        board = basc_py4chan.Board(boards)
        threads = board.get_all_thread_ids()
        randomThread = randint(0, len(threads))
        thread = board.get_thread(threads[randomThread])
        topic = thread.topic
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', topic.comment)
        test = str(cleantext).replace('&gt;', '')
        cleanerText = str(test).replace('&#039;', '\'')
        cleanerText = str(cleanerText).replace('\'', '\'\'')
        cleanerText = str(cleanerText).replace('\"', '\"\"')
        insert4ChanShitPost(cleanerText)
    except Exception as exception:
        print(exception)


def insert4ChanShitPost(shit):
    try:
        db = pymysql.connect(host=hostname, user=user, password=password, port=port, database=database)
        cursor = db.cursor()

        query = 'INSERT into 4chanData (Text) VALUES ' + '(\'' + shit + '\')'
        cursor.execute(query)
        db.commit()
        db.close()
    except Exception as exception:
        print(exception)


def shitPost():
    try:
        con = pymysql.connect(host=hostname, user=user, password=password, port=port, database=database)
        cursor = con.cursor()
        cursor.execute('SELECT `Text` FROM TwitterBot.4chanData')
        rows = cursor.fetchall()
        shitPosting = []
        for row in rows:
            newRow = str(row).replace('(\'', '')
            updatedRow = str(newRow).replace('\',)', '')
            shitPosting.append(updatedRow)
        text_model = markovify.NewlineText(shitPosting)
        shitPostSupreme = text_model.make_short_sentence(280)
        newTweet = str(shitPostSupreme).replace('&#039;', '\'')
        newestTweet = str(newTweet).replace('&gt;', '')
        tweetBot.update_status(newestTweet)
        cursor = con.cursor()
        query = 'INSERT into VarianJoestar (Text) VALUES ' + '(\'' + shitPostSupreme + '\')'
        cursor.execute(query)
        con.commit()

        cursor.close()
        print(shitPostSupreme)
    except Exception as exception:
        print(exception)


def main():
    getShit()
    shitPost()


main()
