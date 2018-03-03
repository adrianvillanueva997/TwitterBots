import praw
from tweepy import OAuthHandler

import config
import sqlite3
import tweepy
import requests
import sys

dataBase = "TweetsDB.db"
con = sqlite3.connect(dataBase)
cur = con.cursor()


def bot_login():
    print("Loggin in...")
    redditConnection = praw.Reddit(username=config.username,
                                   pasword=config.password,
                                   client_id=config.client_id,
                                   client_secret=config.client_secret,
                                   user_agent='thexiao77\'s and Alexiwto\'s bot')
    print("Logged in!")

    return redditConnection


def getData(redditConnection):
    subreddit = redditConnection.subreddit('ImGoingToHellForThis')
    contador = 0
    for submission in subreddit.stream.submissions():
        text = submission.title.lower()
        url = str(submission.url)
        estado = '0'
        insertSQL(text, str(submission), estado, url)
        contador += 1
        if contador == 100:
            selectGutPost()


def existingPost(post_id):
    try:
        query = 'SELECT Post_ID FROM MIERDA_UTIL WHERE Post_ID = ' + '(\'' + post_id + '\')'
        cur.execute(query)
        con.commit()
        result = cur.fetchall()
        a = str(result).replace('[(\'', '')
        b = str(a).replace('\',)]', '')
        if b == post_id:
            return True
        else:
            return False
    except Exception as e:
        print(e)


def insertSQL(text, post_id, estado, imagen):
    try:
        if (existingPost(post_id) == False):
            print(text, post_id, estado, imagen)
            correctText = str(text).replace('\'', '\'\'')
            query = 'INSERT into MIERDA_UTIL (Post_ID,Estado,Imagen,Titulo) VALUES ' + '(\'' + post_id + '\',' + '\'' + estado + '\',' + '\'' + imagen + '\',' + '\'' + correctText + '\')'
            cur.execute(query)
            con.commit()
            print('insertado: ' + text + ' ' + post_id)
    except Exception as e:
        print(e)


def selectGutPost():
    try:
        query = 'select Titulo,Imagen from MIERDA_UTIL where Estado =\'0\' ORDER BY ID asc limit 1'
        cur.execute(query)
        con.commit()
        result = cur.fetchall()
        publishTweet(str(result))
        updateStatus(0)
    except Exception as e:
        print(e)


def updateStatus(index):
    try:
        query = 'update MIERDA_UTIL set Estado = 1 where ID = (select ID from MIERDA_UTIL where Estado = 0 ORDER BY ID asc limit 1)'
        cur.execute(query)
		con.commit()
        if index == 0:
            sys.exit()
        elif index == 1:
            selectGutPost()
    except Exception as e:
        print(e)


def publishTweet(tweetList):
    try:
        data = [e.strip() for e in tweetList.split(',')]
        print(data[0])
        print(data[1])
        title = str(data[0]).replace('[(\"', '')
        title2 = title.replace('\"', '')
        title3 = title2.replace('[(\'', '')
        title4 = title3.replace('\'', '')

        image = str(data[1].replace('\'', ''))
        image2 = image.replace(')]', '')
        print(title2)
        print(image2)
        filename = 'image.jpg'
        request = requests.get(image2, stream=True)
        if request.status_code == 200:
            with open(filename, 'wb') as file:
                for chunk in request:
                    file.write(chunk)
        consumer_key = ''
        consumer_secret = ''
        access_token = ''
        access_secret = ''
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        tweetBot = tweepy.API(auth)
        tweetBot.update_with_media(filename, title4)
    except Exception as e:
        print(e)
           updateStatus(1)


if __name__ == '__main__':
    redditConnection = bot_login()
    getData(redditConnection)
