# By: Kenny_G_Loggins
# Created on: 8/2/20, 3:57 PM
# File: reddit_bot_tut.py
# Project: Reddit_bot

import praw
import sqlite3


# Uncomment first time running to create database
#c.execute('CREATE TABLE replied_to (submission text)')

# Grab bot info from praw.ini
reddit = praw.Reddit('bot1')
replied_to = sqlite3.connect('replied_to.db')
c = replied_to.cursor()

# Grab post from a subreddit and only return a url if it hasn't been returned before
def forumal_dank(sub, count):
    danger = reddit.subreddit(sub)
    new_title = []
    new_post = []
    for post in danger.hot(limit=10):
        if post.ups > count and not post.stickied:
            # Check in database to see if we've posted this submission before
            c.execute("SELECT * FROM replied_to WHERE submission=?", (post.id,))
            if c.fetchone():
                pass
            else:
                # Haven't posted before so store submission ID in database
                c.execute("INSERT INTO replied_to VALUES (:submission)", {'submission': str(post.id)})
                replied_to.commit()
                new_title.append(post.title)
                new_post.append(post.url)
    return new_post, new_title


#with concurrent.futures.ThreadPoolExecutor() as executor:
    #f1 = executor.submit(schedule.every(10).seconds.do(forumal_dank))
