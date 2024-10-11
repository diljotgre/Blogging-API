from config import config
import psycopg2
from psycopg2 import pool 
from models import Post
import json


params = config()
con_pool = psycopg2.pool.SimpleConnectionPool(minconn = 1, maxconn=5, **params)

def init():
    connection = None
    try:
        connection = con_pool.getconn()
        cur = connection.cursor()
        query = """ CREATE TABLE IF NOT EXISTS blog_posts(
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
            
def add(title, content, category, tags, createdAt, updatedAt):
    
    try:
        connection = con_pool.getconn()
        cur = connection.cursor()
        query = """INSERT INTO blog_posts(title, content, category, tags, createdAt, updatedAt)
                VALUES(%s, %s, %s, %s, %s, %s); """
        
        data=(title, content, category, tags, createdAt, updatedAt)       
        cur.execute(query, data)    
        connection.commit()
    except(Exception, psycopg2.Error)  as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print("Database connection terminated")                                                                                                                                 
        
def test():
    try:
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


def update(title, content, category, tags, updatedAt, id):
    try:
        connection= con_pool.getconn()
        cur = connection.cursor()
        query = """UPDATE blog_posts
                   SET title = %s, content = %s, category = %s, tags=%s, updatedAt = %s
                   WHERE id = %s"""
        data = (title, content, category, tags, updatedAt, id)
        cur.execute(query,data)
        connection.commit()
    except(Exception, psycopg2.DataError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('database connection terminated')

def delete(id):
    try:
        connection = con_pool.getconn()
        cur = connection.cursor()
        query = """ DELETE FROM blog_posts
                    WHERE id = %s"""
       
        
        cur.execute(query, (id,))
        connection.commit()
        
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('database connection terminated')


def get_all():
    try:
        print('hello')
        connection = con_pool.getconn()
        if connection is None:
            print('failed to get a connection from the pool')
        cur = connection.cursor()
        # query = """ SELECT * from blog_posts """


        cur.execute('SELECT * from blog_posts;')
       
        data = cur.fetchall()
        posts = []
        
        for post in data:
            print('loop')
            post = Post(post[1], post[2], post[3], post[4], post[5], post[6])
            post = json.dumps(post)
            posts.append(post)
        
        print(posts)
                
        

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('database connection terminated')

get_all()