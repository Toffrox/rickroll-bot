import praw
import time
from rickroll_list import links

comments_read = 0
rickrolls = 0

r = praw.Reddit('RickRollRadar by /r/Toffrox')

subreddit = r.subreddit("toffrox")
# TODO: Add subreddit blacklist, exception handling when crashing
for comment in subreddit.stream.comments(skip_existing=True):
    comments_read += 1
    print(r.auth.limits)
    for l in links:
        if l in comment.body:
            if comment.author == "RickRollRadar":
                break
            print("Detected Rickroll: ")
            print(comment.body)
            rickrolls += 1
            comment.reply("Warning! The comment above is a **rickroll**! Click at your own risk! \n \n ^(I am a bot, warning the world of all rickrolls. Out of " + str(comments_read) + " comments, I have detected " + str(rickrolls) + " rickrolls. You can find more information) [^(here)](https://www.youtube.com/watch?v=dQw4w9WgXcQ)^(.)")
            print("Replied")
