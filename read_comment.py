import praw
import time
import pickle
import os
from rickroll_list import links
from blacklist import blacklist

stats = [3993228, 10]

r = praw.Reddit(
    client_id=os.environ['client_id'],
    client_secret=os.environ['client_secret'],
    password=os.environ['password'],
    username=os.environ['username'],
    user_agent=os.environ['user_agent']
)

subreddit = r.subreddit("all")

while True:
    try:
        for comment in subreddit.stream.comments(skip_existing=True):
            stats[0] += 1
            print("Remaining: " + str(r.auth.limits['remaining']) + " Comments reviewed: " + str(stats[0]) + " Rickrolls: " +  str(stats[1]))
            for l in links:
                if l in comment.body:
                    if comment.author == "RickRollRadar" or "bot" in str(comment.author).lower() or str(comment.subreddit).lower() in blacklist:
                        break
                    print("Detected Rickroll: ")
                    print(comment.body)
                    stats[1] += 1
                    comment.reply("Warning! The comment above has a **rickroll**! Click at your own risk! \n \n ^(I am a bot, warning the world of all rickrolls. Out of " + str(stats[0]) + " comments, I have detected " + str(stats[1]) + " rickrolls. You can find more information) [^(here)](https://www.youtube.com/watch?v=dQw4w9WgXcQ)^(.)")
                    print("Replied")
    except Exception as e:
        print(str(e))
