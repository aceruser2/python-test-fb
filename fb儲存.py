
# coding: utf-8

# In[1]:

import facebook
import requests
import pymysql

conn=pymysql.connect(host='localhost', port=3306, user='', passwd='',db='資料庫',charset='UTF8')
cur=conn.cursor()
cur.execute("USE 資料庫")

def sort(posttime,title,content,postlike):
	＃這裡我先用phpmyadmin建立含id,posttime,title,content,postlike的utf8mb4_unicode_ci的資料表,因為資料有中文
    cur.execute("INSERT INTO text (posttime,title,content,postlike) VALUES(\"%s\",\"%s\",\"%s\",\"%s\")",(posttime,title,content,postlike))
    cur.connection.commit()


def some_action(post):
    posttime=''
    title=''
    content=''
    postlike=''
    try:
        posttime=post['created_time']
        
       
    except KeyError:
        pass
    try:
        title=post['name']
        
    except KeyError:
        pass
    try:    
        content=post['message']
    except KeyError:
        pass   
    try:  
        postlike=post['reactions']['summary']['total_count']
       
    except KeyError:
        postlike='none'
        print(None)
    sort(posttime,title,content,postlike)
    print('end')
   
    
    
    
    
    
    
    
    
   

            
    
    
    
    
    
    
    
    
    

access_token='權杖'

user='帳戶/?fields=posts{message_tags,message,name,created_time,reactions.type(LIKE).summary(total_count)}'

graph=facebook.GraphAPI(access_token,version='2.7')
profile=graph.get_object(user)
posts=profile['posts']



    
[some_action(post=post) for post in posts['data']]
       

while True:
    try:
        [some_action(post=post) for post in posts['data']]
        posts=requests.get(posts['paging']['next']).json()
    except :
        break       
        
        
        
        


