from flask import render_template, flash, redirect, session, url_for, request, g
from app import app, db
import random
from .forms import *
from .models import *
from bs4 import BeautifulSoup
import requests

@app.route('/')
def home():
    posts = Post.query.all()
    """
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
    for title,content in zip(titles,contents):
        blog = (title.get_text(),content.get_text())
        if blog != None:
            students[name].append(blog)
    """
    return render_template('index.html',posts=posts)

@app.route('/login',methods=['GET','POST'])
def login():
    form = Admin()
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            session['username'] = user.username
            return redirect(url_for('home'))
        else:
            return render_template('login.html',form=form)
    else:
        return render_template('login.html',form=form)
@app.route('/admin',methods=['GET','POST'])
def admin():
    if session['username']:
        return render_template('admin.html')
    else:
        return redirect(url_for('login'))
