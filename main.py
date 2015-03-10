import praw
r = praw.Reddit('flairs all posts in a sub')

################# Keep everything between the single quotes: ###########################

username = 'your_username'		# Reddit Username, must have mod privs
password = 'your_password'		# Reddit Password, must have mod privs
sub = 'your_subreddit'			# Just need the text name of your sub, no 'r/.. etc
flair_text = 'your_flair_text'		# Text you want to be used in the flair
flair_css = 'css_for_flair'		# Name of CSS class used for flair decoration

########################################################################################

r.login(username,password)
subreddit = r.get_subreddit(sub)
already_done = set()
ignore_list = ['EVENT', 'NEWS', 'CLAIM', 'event', 'news', 'claim']

print '-->Scanning 1000 newest submissions (this might take a bit)...\n'
for link in subreddit.get_new(limit=None):
	if link.link_flair_text in ignore_list:
		continue
	link.set_flair(flair_text, flair_css)
	already_done.add(link.id)

print '-->Scanning top submissions from this month...\n'
for link in subreddit.get_top_from_month(limit=None):
	if link.id in already_done or link.link_flair_text in ignore_list:
		continue
	link.set_flair(flair_text, flair_css)
	already_done.add(link.id)

print '-->Scanning top submissions from this year...\n'
for link in subreddit.get_top_from_year(limit=None):
	if link.id in already_done or link.link_flair_text in ignore_list:
		continue
	link.set_flair(flair_text, flair_css)
	already_done.add(link.id)

print '-->Scanning top submissions from all time...\n'
for link in subreddit.get_top_from_all(limit=None):
	if link.id in already_done or link.link_flair_text in ignore_list:
		continue
	link.set_flair(flair_text, flair_css)
	already_done.add(link.id)

print 'All done!'
exit()
