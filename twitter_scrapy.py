# By: Kenny_G_Loggins
# Created on: 8/2/20, 11:09 PM
# File: twitter_scrapy.py
# Project: pythonProject

import GetOldTweets3 as got
from pymongo import MongoClient
from config import mongserver, twitter_handles, twitter_words, count


# Setup connection to mongodb collection
server = MongoClient(mongserver)
db = server.twitter_db
posts = db.tweets

# Scrape the given twitter handles and stores the information in our mongodb
def twitter_scrape():
    # Go through each username set in twitter_handles from config.py
    # For each one grab their last 10 tweets
    for username in twitter_handles:
        tweetCriteria = got.manager.TweetCriteria().setUsername(username).setMaxTweets(count).setEmoji('unicode')
        tweets = got.manager.TweetManager.getTweets(tweetCriteria)
        # Grab specified fields for each tweet
        user_tweets = [[tweet.username, tweet.date, tweet.text, tweet.permalink] for tweet in tweets]
        # Run through each list that was created for each tweet and give them variables
        for tweet in user_tweets:
            handle = tweet[0]
            time = tweet[1]
            text = tweet[2]
            link = tweet[3]

            # Add tweet to our database if it isn't already there
            post = {"handle": handle, "time": time, "text": text, "link": link, "posted": False}
            if db.tweets.find_one({"link": post["link"]}):
                pass
            else:
                post_id = posts.insert_one(post).inserted_id

# Looks through our information stored in our mongodb and returns the links of the documents matching our criteria.
def twitter_filter():
    link_list = []
    # Iterate through our provided search terms in twitter_words
    for word in twitter_words:
        results = db.tweets.find({"text": {"$regex": word}})
        for result in results:
            # Check if we've posted before, if not append the link to our list and set the posted value to true in
            # the document.
            if result and not result["posted"]:
                link_list.append(result['link'])
                db.tweets.update_one({"_id": result["_id"]}, {"$set":{"posted": True}})
            else:
                pass
    return(link_list)
