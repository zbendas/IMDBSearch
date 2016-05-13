# This is all super broken. Don't really use it right now.

import praw

r = praw.Reddit('Testing PRAW API by /u/knytemere')
r.login('moviebuffbot','kezier1pegasus2')
subreddit = r.get_subreddit("askreddit")
comments = praw.helpers.comment_stream(r, 'all', limit=5)
# flat_comments = praw.helpers.flatten_tree(comments)
for comment in comments:
    print(comment)