from app import db, models

pairs = [('https://adamska426.wordpress.com/','Katelyn'),('https://computerscience183923392.wordpress.com','Jessie'),
        ('https://youngdublog.wordpress.com/','Dustin'),('https://waughblogs.wordpress.com','Chandler'),
        ('https://basantfoss.wordpress.com','Basanta'),('https://mysoftwarejourney.wordpress.com','Malachi'),
        ('https://gbondo.wordpress.com/','Moses'),('https://awyoonisj.wordpress.com/','Jamal'),
        ('https://opensourcewithdove.wordpress.com/','Dove'),('https://johnsone978745682.wordpress.com/','Evan'),
        ('https://halfeatenapple608323536.wordpress.com','Abi'),('https://csc426blog.wordpress.com/','Cameron')]

students = {'Katelyn':[],'Jessie':[],'Dustin':[],
            'Chandler':[],'Basanta':[],'Malachi':[],
            'Moses':[],'Jamal':[],'Dove':[],'Evan':[],
            'Abi':[],'Cameron':[]}    

for i in pairs:
    blog = models.Blog()
    blog.student = i[1]
    blog.url = i[0]
    if i[1] == 'Moses':
        blog.titletag = 'h2'
    else:
        blog.titletag = 'h1'
    blog.titleclass = 'entry-title'
    blog.bodytag = 'div'
    blog.bodyclass = 'entry-content'
    db.session.add(blog)
    db.session.commit()
