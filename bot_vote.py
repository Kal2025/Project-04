import praw
import time
from praw.reddit import Subreddit
from textblob import TextBlob

reddit = praw.Reddit('bot', user_agent='cs40')
submission_url = 'https://www.reddit.com/r/cs40_2022fall/comments/z23ajv/noncredibledefense_1860s/'
submission = reddit.submission(url=submission_url)

while True:
    submission.comments.replace_more(limit=None)

    #This section upvotes and downvotes on submissions

    for submission in list(reddit.subreddit("cs40_2022fall").new(limit=500)):
        if 'trump' in submission.title.lower():
            submission.downvote()
            for submission in list(reddit.subreddit("cs40_2022fall").new(limit=500)):
                if 'biden' in submission.title.lower():
                    submission.upvote()
                    print('Upvoted')

        #This section upvotes and downvotes on comments using textblob
    
    for comment in submission.comments:
            commenttext = (TextBlob(comment.body).lower())
            if ("biden" in commenttext and commenttext.sentiment.polarity>0.5) or ("trump" in commenttext and commenttext.sentiment.polarity<-0.5):
                comment.upvote()
                print('Upvoted2')
                print('comment_body=',comment.body)
                print('link=',submission.permalink)

            elif ("biden" in commenttext and commenttext.sentiment.polarity<-0.5) or ("trump" in commenttext and commenttext.sentiment.polarity>0.5):
                comment.downvote()
                print('Downvoted2')
                print('link=',submission.permalink)

            else:
                pass
    print ('sleeping')
    time.sleep(25)