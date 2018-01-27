from bs4 import BeautifulSoup
import requests

#List of sites to crawl
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
for item in pairs:
    site = item[0]
    name = item[1]
    #Grab the page and turn it into an object
    response = requests.get(site)
    html = response.text
    page = BeautifulSoup(html,'html.parser')

    #Grab the entry titles for its text
    titles = page.find_all('h1','entry-title')
    if titles == []:
        titles = page.find_all('h2','entry-title')
    contents = page.find_all('div','entry-content')
    print(titles)
    print(contents)
    for title,content in zip(titles,contents):
        blog = (title.get_text(),content.get_text())
        if blog != None:
            students[name].append(blog)

print(students)
