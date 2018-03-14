from sqlalchemy import create_engine

con = engine = create_engine("mysql+mysqldb://:" + '' + "@/?charset=utf8mb4",
                             encoding='utf-8')
