import praw 
import pandas as pd
import os

from dotenv import load_dotenv
load_dotenv()


reddit = praw.Reddit(client_id=os.getenv('client_id'),      # your client id
                     client_secret=os.getenv('client_secret'),  # your client secret
                     user_agent="my user agent", # user agent name
                     username = "SchakoK",     # your reddit username
                     password = os.getenv('reddit_password'))

sub = ['Alexa']

for s in sub:
    subreddit = reddit.subreddit(s)

    
    #keywords = ['Alexa', 'hacked', 'security', 'vulnerability']

    #query = ' '.join(keywords)

    #for item in keywords:
    post_dict = {
        "title" : [],
        "score" : [],
        "id" : [],
        "url" : [],
        "comms_num": [],
        "created" : [],
        "body" : []
    }
    comments_dict = {
        "comment_id" : [],
        "comment_parent_id" : [],
        "comment_body" : [],
        "comment_link_id" : []
    }

    for submission in subreddit.new(limit = None): #subreddit.search(query, sort = "top", limit = 500)
        post_dict["title"].append(submission.title)
        post_dict["score"].append(submission.score)
        post_dict["id"].append(submission.id)
        post_dict["url"].append(submission.url)
        post_dict["comms_num"].append(submission.num_comments)
        post_dict["created"].append(submission.created)
        post_dict["body"].append(submission.selftext)

        submission.comments.replace_more(limit = None)
        for comment in submission.comments.list():
            comments_dict["comment_id"].append(comment.id)
            comments_dict["comment_parent_id"].append(comment.parent_id)
            comments_dict["comment_body"].append(comment.body)
            comments_dict["comment_link_id"].append(comment.link_id)

    post_comments = pd.DataFrame(comments_dict)
    post_comments.to_csv(s + "_comments_subreddit.csv", index = False) #s+"_comments_"+ item +"subreddit.csv")
    post_data = pd.DataFrame(post_dict)
    post_data.to_csv(s + "_subreddit.csv", index=False) #s+"_"+ item +"subreddit.csv"