import praw
import random
import datetime
import time

# FIXME:
# copy your generate_comment function from the madlibs assignment here

madlibs = [
    "Narendra Modi is the [BEST] Prime Minister of India in a number of [FIELDS]. Such a prime minister is [MOST] wanted in India to handle the current circumstances and challenges that currently affect and have affected the Nation [BEFORE]. [AFTER] becoming Prime Minister, Modi changed the horizon of politics and standard of administration.",
    "Narendra Modi is one of the most poorly understood men in [INDIA]. He is an honest and [EXTREMELY] hard working [MAN]. He isn't here for [POWER], he wants to actually leave a legacy behind that will change the face of the nation for the [BETTER].",
    "Narendra Modi is the first Prime Minister of [INDIA] who has been working [CONTINUOUSLY] for more than 18 hours in a day without taking any leave. [MOREOVER], he is the most [ENERGETIC] prime minister of India by taking very fast decisions and insuring involvement and commitment of the bureaucracy at [HIGH] levels.",
    "India has been under foreign rule for more than 1000 years, [AS A RESULT OF THIS], the [MAIN] morals of the entire nation, [ESPECIALLY] the Hindu community, has been at the bottom, even after India got independence in 1947. Modi has [STARTED] reverse engineering to restore the [LOST] glory of Indian pride.",
    "Separating political lines, Narendra Modi has [SHOWN] exemplar talent and skill in climbing up to the highest position of [INDIA], [DESPITE] him coming from a humble background and not even having a personal life or a family of his own. This all requires a [TREMENDOUS] amount of resilience and [DETERMINATION].",
    "[SOCIETY] considers Narendra Modi as a [FIGHTER] who will not stop till the truth is known to [INDIA]. He fought a [LONG] battle with Congress on Godra riots for nearly ten long years to bring out the truth to the public. He has the ability to compete against forces that are [STRONGER] than him and prevail."
    ]

replacements = {
    'BEST' : ['best', 'greatest','finest'],
    'FIELDS': ['fields', 'departments','areas'],
    'BEFORE' : ['before','previously','beforehand'],
    'AFTER' : ['After', 'As a result of', 'Latter to'],
    'INDIA' : ['India', 'the world', 'society'],
    'EXTREMELY' : ['extremely', 'exceptionally','immensely'],
    'MAN' : ['man', 'person', 'indivual','human'],
    'POWER': ['power', 'fame', 'wealth'],
    'MOREOVER':['Moreover','Furthermore','In addition'],
    'CONTINUOUSLY': ['continuously','constantly','endlessly'],
    'BETTER': ['better', 'greater good', 'best'],
    'ENERGETIC':['energetic', 'charasmatic','affable'],
    'ESPECIALLY': ['especially', 'notably', 'specifically'],
    'STARTED' : ['started','begun','initialized'],
    'LOST' : ['lost', 'absent', 'disoriented'],
    'MAIN': ['main', 'overarching','central'],
    'SHOWN': ['shown','demonstrated', 'displayed'],
    'MOST' : ['most', 'highly','vastly'],
    'TREMENDOUS': ['tremendous','exceptional', 'marvelous'],
    'DETERMINATION': ['determination', 'dedication','valor'],
    'FIGHTER': ['fighter', 'warrior','champion'],
    'SOCIETY': ['Society', 'The world', 'Everyone'],
    'HIGH': ['high', 'top', 'extreme', 'soaring'], 
    'AS A RESULT OF THIS': ['because of this','as a result of this','by cause of this'],
    'LONG': ['long', 'continuous','lasting'],
    'STRONGER':['stronger', 'more powerful', 'more fierce'],
    'DESPITE' :['despite', 'regardless of', 'in spite of']

    }

def generate_comment():
    madlib = random.choice(madlibs)
    for replacement in replacements.keys():
        madlib = madlib.replace('['+replacement+']', random.choice(replacements[replacement]))
    return madlib

#EXTRA CREDIT UPVOTE:
def score_comment(comment):
    comment = random.choice(comments_without_replies)
    comment_score = comment.score
    return comment_score


# FIXME:
# connect to reddit 
reddit = praw.Reddit('bot', user_agent='cs40')

# FIXME:
# select a "home" submission in the /r/cs40_2022fall subreddit to post to,
# and put the url below
#
# HINT:
# The default submissions are going to fill up VERY quickly with comments from other students' bots.
# This can cause your code to slow down considerably.
# When you're first writing your code, it probably makes sense to make a submission
# that only you and 1-2 other students are working with.
# That way, you can more easily control the number of comments in the submission.
submission_url = 'https://www.reddit.com/r/cs40_2022fall/comments/z3tmug/wp_something_happy_please_include_cats_and_maybe/'
submission = reddit.submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
while True:

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions

    submission.comments.replace_more(limit=None)
    all_comments = []
    all_comments = submission.comments.list()
    



    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not\
    
    not_my_comments = []
    for comment in all_comments:
        #print('comment.author=', comment.author)
        #print('type(comment.author)=', type(comment.author))
        if str(comment.author) != 'Senior_BOT_4883':
            not_my_comments.append(comment)

    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)
    print('has_not_commented=', has_not_commented)

    if has_not_commented:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message
        text = generate_comment()
        submission.reply(text)

    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two    nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        comments_without_replies = []
        for comment in not_my_comments:
            did_reply = False
            for replies in comment.replies:
                if str(replies.author) == 'Senior_BOT_4883':
                    did_reply = True
            if did_reply == False:
                comments_without_replies.append(comment)

        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly;
        # many students struggle with getting a large number of "valid comments"
                #print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message
                comment = random.choice(comments_without_replies)
    try: 
        #EXTRA CREDIT UPVOTE:
            comment = sorted(comments_without_replies,key=score_comment, reverse=True)[0]
            print(comment)
            comment.reply(generate_comment())
    except praw.exceptions.APIException: 
            print('not replying to a comment that has been deleted')
    except IndexError:
            print('not replying to a post where I have already commented')

    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions
        
    submission = random.choice(list(reddit.subreddit("cs40_2022fall").hot(limit=5)))
    #print ('title=', submission.title)
    #print('link=', submission.permalink)
    print('submission=', submission)


    # We sleep just for 1 second at the end of the while loop.
    # This doesn't avoid rate limiting
    # (since we're not sleeping for a long period of time),
    # but it does make the program's output more readable.
    time.sleep(0)

