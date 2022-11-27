# Project-04
## Reddit Bot Project 

The name of my bot for this project: Senior_BOT_4883. Here is a link to the [subreddit](https://www.reddit.com/r/cs40_2022fall/). 
<br />
<br />
For this project, my bot spread information on the subreddit supporting the PM of India: Narendra Modi. In terms of the attached files above, the `bot.py` file is the main code of this project including the six different tasks. For my first choice of the optional tasks, I decided to choose the third option: having the bot reply to the most highly upvoted comment in a thread. Instead of having it's own file above, I included it in the `bot.py` file as I used the code from the start. It will have a comment above it stating that it is the 'upvote-bot'. My second choice from the optional tasks was posting at least 200 submissions to the reddit, this corresponds with the file named: `bot_submissions.py` (This was the first option). This file posts random submissions from the r/Liberals reddit to our r/cs40_2020fall reddit. The last optional task I choose was the forth option, this corresponds with the file called: `bot_vote.py`. This last file will upvote or downvote any mention of Biden or Trump, and, using 'TextBlob', it can also measure the sentiment of the comment or post, reacting to it by upvoting or downvoting in accordance.
<br />
<br />
My favorite thread was [this](https://www.reddit.com/r/cs40_2022fall/comments/z362if/comment/ixk5scy/?utm_source=share&utm_medium=web2x&context=3), I liked it because it was really random and made no sense. Here is the image of the thread:
<br />

![Goofy reddit thread](https://user-images.githubusercontent.com/112449375/204111601-d43a090a-c383-4ae7-a356-2976b8091e5e.png)
<br />
## Output of `bot_counter.py`
```
len(comments)= 1000
len(top_level_comments)= 443
len(replies)= 557
len(valid_top_level_comments)= 443
len(not_self_replies)= 543
len(valid_replies)= 465
========================================
valid_comments= 908
========================================
```

## Score
Estimated score: 31/30
### Completed: 
1. All tasks in the `bot.py` file (+12 points) 
2. The github repo (+3 points)
3. `valid_comments` range of 900-999 (+8 points)
4. Optional task one, posting at least 200 submissions (+2 points)
5. Optional task three, replying to the most highly upvoted comments in a thread. (+2 points)
6. Optional task four, use 'TextBlob' sentiment analysis to upvote/downvote comments and submissions in accordance (+4 points)
### Not Completed:
1. Having at least 1000 valid comments posted
2. Create an "army" of 5 bots that are all posting similar comments 
3. Using gpt-2-simple or Markovify to generate text for my comments
