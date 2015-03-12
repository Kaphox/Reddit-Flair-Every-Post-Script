import praw
r = praw.Reddit('flairs all posts in a sub')

################# Keep everything between the single quotes: ###########################

username = 'Kaphoxbot'		        # Reddit Username, must have mod privs
password = 'nottheactualpassword'		# Reddit Password, must have mod privs
sub = 'worldpowers'			# Just need the text name of your sub, no 'r/.. etc
flair_text = 'OLD WP'		# Text you want to be used in the flair
flair_css = 'oldWP'		# Name of CSS class used for flair decoration

########################################################################################

r.login(username,password)
subreddit = r.get_subreddit(sub)
already_done = set()
flair_list = ['EVENT', 'NEWS', 'CLAIM', 'CONFLICT', 'EXPANSION', 'CRISIS'] # Flairs you want to change

for link in subreddit.get_new(limit=None):
	if link.link_flair_text not in flair_list:
		continue
	link.set_flair(flair_text, flair_css)
	already_done.add(link.id)

for link in subreddit.get_top_from_month(limit=None):
	if link.id in already_done or link.link_flair_text not in flair_list:
		continue
	link.set_flair(flair_text, flair_css)
	already_done.add(link.id)

for link in subreddit.get_top_from_year(limit=None):
	if link.id in already_done or link.link_flair_text not in flair_list:
		continue
	link.set_flair(flair_text, flair_css)
	already_done.add(link.id)

for link in subreddit.get_top_from_all(limit=None):
	if link.id in already_done or link.link_flair_text not in flair_list:
		continue
	link.set_flair(flair_text, flair_css)
	already_done.add(link.id)

exit()
