from config import config
import psycopg2
from psycopg2 import pool 
from models import Post
import json
from pydantic import json


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
        if cur is not None:
            cur.close()
        if connection is not None:
            con_pool.putconn(connection)
            print('database connection terminated')
            
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
        if cur is not None:
            cur.close()
        if connection is not None:
            con_pool.putconn(connection)
            print('database connection terminated')                                                                                                                                 
        
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
        if cur is not None:
            cur.close()
        if connection is not None:
            con_pool.putconn(connection)
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
        if cur is not None:
            cur.close()
        if connection is not None:
            con_pool.putconn(connection)
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
        if cur is not None:
            cur.close()
        if connection is not None:
            con_pool.putconn(connection)
            print('database connection terminated')


def get_all():
    try:
        
        connection = con_pool.getconn()
        if connection is None:
            print('failed to get a connection from the pool')
        cur = connection.cursor()
        # query = """ SELECT * from blog_posts """


        cur.execute('SELECT * from blog_posts;')
       
        data = cur.fetchall()
        posts = []
        
        for post in data:
            
            post = Post(title = post[1], content  = post[2], category= post[3], tags =  post[4], createdAt= post[5],updatedAt=  post[6])
            posts.append(post.model_dump())
            # print(post.model_dump())
        
        return posts, 200
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if connection is not None:
            con_pool.putconn(connection)
            print('database connection terminated')

def get_specific(term):
    try:
        connection = con_pool.getconn()
        if connection is None:
            print('failed to get a connection from the pool')
        cur = connection.cursor()
        
        query = """ SELECT * from blog_posts
                        WHERE  title = %s
                            OR  content = %s
                            OR  category = %s
                            OR  tags @> ARRAY[%s]
                            OR  createdAt = %s
                            OR  updatedAt = %s ; 
                """
        data = (term, term, term, term, term, term)
        cur.execute(query, data)
        data = cur.fetchall()
        posts = []
        for post in data:
            post = Post(title = post[1], content = post[2], category = post[3], tags = post[4], createdAt = post[5], updatedAt = post[6])
            posts.append(post.model_dump())
            
        return posts, 200
        
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if connection is not None:
            con_pool.putconn(connection)
            print('database connection terminated')
    
    
    
    
    