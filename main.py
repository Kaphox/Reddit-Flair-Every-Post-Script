import praw
r = praw.Reddit('flairs all posts in a sub')

################# Keep everything between the single quotes: ###########################

username = 'your_username'
password = 'your_password'
sub = 'your_subreddit'			# Just need the text name of your sub, no 'r/.. etc
flair_text = 'your_flair_text'
flair_css = 'css_for_flair'

########################################################################################

r.login(username,password)
subreddit = r.get_subreddit(sub)
already_done = set()

for link in subreddit.get_new(limit=None):
	link.set_flair(flair_text, flair_css)
	already_done.add(link.id)

for link in subreddit.get_top_from_month(limit=None):
	if link.id in already_done:
		continue
	link.set_flair(flair_text, flair_css)
	already_done.add(link.id)

for link in subreddit.get_top_from_year(limit=None):
	if link.id in already_done:
		continue
	link.set_flair(flair_text, flair_css)
	already_done.add(link.id)

for link in subreddit.get_top_from_all(limit=None):
	if link.id in already_done:
		continue
	link.set_flair(flair_text, flair_css)
	already_done.add(link.id)

print '\nAll done!'
exit()
