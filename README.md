# twitterBot

Small twitter bot that learns from other tweets and generates tweets acording to them.
* Spanish bot: [@wikiredmsr](https://twitter.com/wikiredmsr)
* English bot: [@varian_joestar](https://twitter.com/varian_joestar)
* Reddit bot (r/IamGoingToHellForThis) [@HellGoin](https://twitter.com/HellGoin) Special thanks to [Alexiwto](https://github.com/alexiwto)
* Another Spanish bot: [@eressGilipollas](https://twitter.com/eressGilipollas)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Make sure to have python 3 installed in your computer, if not you can download it from [here](https://www.python.org). Since pip comes by default in python 3 there is no need to install it.

If you are using any Linux distro with apt package management just type the following in the terminal.

```
sudo apt-get update
sudo apt-get install python3.6
sudo apt-get install python3-pip
```

To install the needed libraries use the following commands, they work for Windows and Linux. For windows users, you have to use the CMD terminal to install them.

```
pip3 install tweepy
pip3 install markovify
pip3 install pymysql
pip3 install basc-py4chan
pip 3 install praw
```

Once you have installed python3 and the libraries, you have to make a [twitter account](https://twitter.com), then go to the [twitter developers](https://dev.twitter.com), login with your account and grab the api keys (consumer and secret)

The regular expression that has been used to remove all the users from the tweet list
```
r"@([A-Za-z0-9_]+)"
```


## Built With

* [Python 3](https://www.python.org) 
* [MySQL](https://www.mysql.com) 


## Authors

* **Adrián Villanueva Martínez** -  [thexiao77](https://github.com/thexiao77)


## License

This project is licensed under GPL V3 - see the [LICENSE.md](https://github.com/thexiao77/twitterBot/blob/master/LICENSE) file for details

## Acknowledgments

* [RedMSR](https://github.com/msdlr) for providing me the idea and inspiration to make this awesome bot.
* [Alexiwto](https://github.com/alexiwto) for providing the idea of doing a reddit bot and developing it with me.

