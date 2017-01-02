import facebook
import requests

#可能有些沒有會出現錯誤，讓錯誤跳過，最後在50行設一個例外跳出迴圈
def some_action(post):
    
    try:
        print(post['created_time'])
    except KeyError:
        pass
    try:
        print(post['name'])
    except KeyError:
        pass
    try:    
        print(post['message'])
    except KeyError:
        pass   
    try:  
        print("likes_count "+str(post['reactions']['summary']['total_count']))
    except KeyError:
        print(None)
    print(r"---------------------")
    
 
    
   
            
    
    
    
    
    
    

access_token='fb權杖'

user='{use_id}/?fields=posts{message_tags,message,name,created_time,reactions.type(LIKE).summary(total_count)}'

graph=facebook.GraphAPI(access_token,version='2.7')
profile=graph.get_object(user)
posts=profile['posts']



while True:
    try:
        [some_action(post=post) for post in posts['data']]
        posts=requests.get(posts['paging']['next']).json()
    except :
        break       
        
        
        
        
