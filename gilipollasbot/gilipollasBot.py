import tweepy
import tweepy, time
from tweepy import OAuthHandler
from random import randint

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
tweetBot = tweepy.API(auth)

gilipollas = ' gilipollas'
textoVacio = ''

listado = []


def devolverPalabra():
    with open('listado-general.txt', 'r', encoding='utf-8') as file:
        for word in file:
            listado.append(word)

        file.close()
        numeroRandom = randint(0, len(listado))
    return listado[numeroRandom]



def main():
    replaces = devolverPalabra().replace("\n", "")
    tweet = textoVacio.join([replaces,gilipollas])
    tweetBot.update_status(tweet)
main()
