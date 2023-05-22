import praw 
import pandas as pd
import os
import sys
import time
from dotenv import load_dotenv
load_dotenv()

def scrape_subreddit(subreddit_name):
    try:    
        reddit = praw.Reddit(client_id=os.getenv('client_id'),      
                            client_secret=os.getenv('client_secret'),  
                            user_agent="my user agent", 
                            username="SchakoK",     #reddit username
                            password=os.getenv('reddit_password'))

        subreddit = reddit.subreddit(subreddit_name)

        post_dict = {
            "title": [],
            "score": [],
            "id": [],
            "url": [],
            "comms_num": [],
            "created": [],
            "body": []
        }
        comments_dict = {
            "comment_id": [],
            "comment_parent_id": [],
            "comment_body": [],
            "comment_link_id": []
        }

        start_time = time.time()

        submissions = subreddit.new(limit=None)
        submissions = list(submissions) #new code 
        for submission in submissions:
            post_dict["title"].append(submission.title)
            post_dict["score"].append(submission.score)
            post_dict["id"].append(submission.id)
            post_dict["url"].append(submission.url)
            post_dict["comms_num"].append(submission.num_comments)
            post_dict["created"].append(submission.created)
            post_dict["body"].append(submission.selftext)

            submission.comments.replace_more(limit=None)
            for comment in submission.comments.list():
                comments_dict["comment_id"].append(comment.id)
                comments_dict["comment_parent_id"].append(comment.parent_id)
                comments_dict["comment_body"].append(comment.body)
                comments_dict["comment_link_id"].append(comment.link_id)

        #new code
        while True:
            last_post = submissions[-1].name

            submissions = subreddit.new(limit=None ,params={'after': last_post})
            submissions = list(submissions)

            if len(submissions) == 0:
                break

            for submission in submissions:
                post_dict["title"].append(submission.title)
                post_dict["score"].append(submission.score)
                post_dict["id"].append(submission.id)
                post_dict["url"].append(submission.url)
                post_dict["comms_num"].append(submission.num_comments)
                post_dict["created"].append(submission.created)
                post_dict["body"].append(submission.selftext)

                submission.comments.replace_more(limit=None)
                for comment in submission.comments.list():
                    comments_dict["comment_id"].append(comment.id)
                    comments_dict["comment_parent_id"].append(comment.parent_id)
                    comments_dict["comment_body"].append(comment.body)
                    comments_dict["comment_link_id"].append(comment.link_id)
        #end new code


        data_folder = "data"
        subreddit_folder = os.path.join(data_folder, subreddit_name)
        os.makedirs(subreddit_folder, exist_ok=True)

        post_comments = pd.DataFrame(comments_dict)
        post_comments.to_csv(os.path.join(subreddit_folder, subreddit_name + "_comments_subreddit.csv"), index=False)
        post_data = pd.DataFrame(post_dict)
        post_data.to_csv(os.path.join(subreddit_folder, subreddit_name + "_subreddit.csv"), index=False)

        end_time = time.time()
        run_time = end_time - start_time
        print(f"Scraping '{subreddit_name}' completed in {run_time:.2f} seconds.")

    except praw.exceptions.RedditAPIException:
        print(f"Subreddit '{subreddit_name}' does not exist.")    

if __name__ == "__main__":
    if len(sys.argv) > 1:
        subreddits = sys.argv[1:]
        for subreddit_name in subreddits:
            scrape_subreddit(subreddit_name)
    else:
        print("Please provide one subreddit name to scrape")

#optionally you can pass arguments into the functions like this
#scrape_subreddit("technology")
