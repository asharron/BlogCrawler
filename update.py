from app import db, models
import requests
from bs4 import BeautifulSoup

def updateDatabase():
    blogs = models.Blog.query.all()

    for blog in blogs:
        site = blog.url
        name = blog.student
        
        #Grab the page and turn it into an object
        response = requests.get(site)
        html = response.text
        page = BeautifulSoup(html,'html.parser')
        #Grab the entry titles for its text
        titles = page.find_all(blog.titletag,blog.titleclass)

        contents = page.find_all(blog.bodytag,blog.bodyclass)

        for title,content in zip(titles,contents):
            post = models.Post()
            post.title = title.get_text()
            post.body = content.get_text()
            post.author = name
            db.session.add(post)
            db.session.commit()
if __name__ == '__main__':
    updateDatabase()
