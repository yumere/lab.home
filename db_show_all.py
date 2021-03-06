from app import db, models
from sqlalchemy import desc

# User
print('DB: User ----------------------------------------------')
users = models.User.query.all()
for user in users:
	print('ID:\t\t%d' % (user.id))
	print('Nickname:\t%s' % (user.nickname))
	print('Email:\t\t%s' % (user.email))


# Lab. Info.
print('DB: LabInfo -------------------------------------------')
info = models.LabInfo.query.all()
for item in info:
	print('ID:\t\t%d' % (item.id))
	print('Name:\t\t%s' % (item.name))
	print('Description:\t%s' % (item.description))
	print('Sub-description:%s' % (item.sub_description))
	print('BG path:\t%s' % (item.background_img_path))

# About
print('DB: About ---------------------------------------------')
info = models.About.query.all()
for item in info:
	print('ID:\t\t%d' % (item.id))
	print('Text:\t\t%s' % (item.text))
	print('Sub-text:\t%s' % (item.sub_text))


# News
print('DB: News ----------------------------------------------')
# info = models.News.query.order_by(desc(models.News.date)).all()
# page_num = 1
# count_per_page = 10
# news_all = models.News.query.order_by(desc(models.News.date)).all()
# news_count = len(news_all)

# start_idx = (count_per_page * (page_num-1)) + 1
# end_idx = (count_per_page * (page_num-1)) + count_per_page
# if news_count < end_idx:
# 	end_idx = news_count

# news_page = []
# idx = 1
# for item in news_all:
# 	if start_idx <= idx and idx <= end_idx:
# 		news_page.append(item)
# 	idx += 1
news_page = models.News.query.order_by(desc(models.News.date)).all()
for item in news_page:
	print('ID:\t\t%d' % (item.id))
	print('SN:\t\t%d' % (item.sn))
	print('Title:\t\t%s' % (item.title))
	print('Contents:\t%s' % (item.contents))
	print('Date:\t\t%s' % (item.date))

# People
print('DB: Member ---------------------------------------------')
info = models.Member.query.all()
for item in info:
	print('ID:\t\t%d' % (item.id))
	print('SN:\t\t%d' % (item.sn))
	print('name:\t\t%s' % (item.name))
	print('homepage:\t%s' % (item.link_homepage))
	

# Teaching
print('DB: Teaching ---------------------------------------------')
info = models.Teaching.query.all()
for item in info:
	print('ID:\t\t%d' % (item.id))
	print('SN:\t\t%d' % (item.sn))
	print('code:\t\t%s' % (item.code))
	print('name:\t\t%s' % (item.name))

# Publications
print('DB: Publications------------------------------------------')
info = models.Publications.query.all()
for item in info:
	print('ID:\t\t%d' % (item.id))
	print('SN:\t\t%d' % (item.sn))
	print('title:\t\t%s' % (item.title))
	print('pdf1:\t\t%s' % (item.link_pdf1))
	print('pdf2:\t\t%s' % (item.link_pdf2))
	print('video:\t\t%s' % (item.link_video))
	print('code:\t\t%s' % (item.link_source))
	print('url:\t\t%s' % (item.link_url))
	print('etc:\t\t%s' % (item.link_etc))
	print('image:\t\t%s' % (item.teaser_image_path))
	print('thumb:\t\t%s' % (item.thumbnail_image_path))

# Links
print('DB: Links ------------------------------------------------')
info = models.Links.query.all()
for item in info:
	print('ID:\t\t%d' % (item.id))
	print('SN:\t\t%d' % (item.sn))
	print('name:\t\t%s' % (item.name))
	print('url:\t\t%s' % (item.link_url))
