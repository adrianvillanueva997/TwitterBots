from sqlalchemy import create_engine

engine = create_engine("mysql+mysqldb://:" + '' + "@?charset=utf8mb4",
                           encoding='utf-8')
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''