from sshternal import SSHTunnelForwarder
import pymysql, os

HOST = os.getenv("DB_HOST")
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")

# server= SSHTunnelForwarder(

# db= pymysql.connect(host=HOST, user=USER, password=PASSWORD)
