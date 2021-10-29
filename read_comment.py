import praw
import time
import pickle
import os
from rickroll_list import links
from blacklist import blacklist

stats = [0, 0]

with open('stats.pk', 'rb') as fi:
    stats = pickle.load(fi)

r = praw.Reddit(
    client_id=os.environ['client_id'],
    client_secret=os.environ['client_secret'],
    password=os.environ['password'],
    username=os.environ['username'],
    user_agent=os.environ['user_agent']
)

subreddits = "all"
for s in blacklist:
    subreddits = subreddits + "-" + s

subreddit = r.subreddit(subreddits)

while True:
    try:
        for comment in subreddit.stream.comments(skip_existing=True):
            stats[0] += 1
            print(r.auth.limits)
            for l in links:
                if l in comment.body:
                    if comment.author == "RickRollRadar":
                        break
                    print("Detected Rickroll: ")
                    print(comment.body)
                    stats[1] += 1
                    comment.reply("Warning! The comment above has a **rickroll**! Click at your own risk! \n \n ^(I am a bot, warning the world of all rickrolls. Out of " + str(stats[0]) + " comments, I have detected " + str(stats[1]) + " rickrolls. You can find more information) [^(here)](https://www.youtube.com/watch?v=dQw4w9WgXcQ)^(.)")
                    print("Replied")
            with open('stats.pk', 'wb') as fi:
                pickle.dump(stats, fi)
    except Exception as e:
        print(str(e))
