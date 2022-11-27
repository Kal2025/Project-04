import praw
import random
import time

reddit = praw.Reddit('bot', user_agent='cs40')
count = 0

while True:
    for i in random.choices(list(reddit.subreddit("Liberal").hot(limit=1000))):
        a = (i.title)
        b = (i.url)
        c = (i.selftext)
        print("="*40)
        print (reddit.subreddit("Liberal").hot(limit=1000))
        print ('title=', a)
        print ('URL=', b)
        print ('text=', c)

        reddit.subreddit("cs40_2022fall").submit(a, selftext=c)

        count += 1
        print (count)

        time.sleep(25)
