from config import config
import psycopg2
from psycopg2 import pool 

params = config()
con_pool = psycopg2.pool.SimpleConnectionPool(minconn = 1, maxconn=5, **params)

def init():
    connection = None
    try:
        connection = con_pool.getconn()
        cur = connection.cursor()
        query = """ CREATE TABLE IF blog_posts(
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            content TEXT, 
            category VARCHAR(255),
            tags TEXT[],
            createdAt TIMESTAMP,
            updatedAt TIMESTAMP     
        );"""
        
        cur.execute(query)
        connection.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Operation completed')
        
def add():
    try:
        # connection = None
        # params = config()
        # print('Connecting to the postgreSQL database..')
        connection= con_pool.getconn()
        
        cur = connection.cursor()
        print('PostgreSQL database version: ')
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('database connection terminated')

