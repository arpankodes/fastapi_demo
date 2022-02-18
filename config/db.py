from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:Favno.666@localhost:3306/fastapidemo")

#PyMySQL is a pure-Python MySQL client library
#ref: https://zetcode.com/python/pymysql/ 

conn = engine.connect()
meta = MetaData()