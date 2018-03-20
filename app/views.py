from flask import render_template, flash, redirect, session, url_for, request, g
from app import app, db
import random
from .forms import *
from .models import *
from bs4 import BeautifulSoup
from update import updateDatabase
import requests
import os, sys

#Default Route
@app.route('/')
def home():
    posts = Post.query.all() #Grab all posts in database
    return render_template('index.html',posts=posts)

#Route for loggin in the user
@app.route('/login',methods=['GET','POST'])
def login():
    form = Admin() #Grab the admin form for loggin in 
    if request.method == 'POST' and form.validate(): #If submitted form
        user = User.query.filter_by(username=form.username.data).first() #Try to find the user
        if user: #If user is in database
            session['username'] = user.username #Log user in and store their username
            return redirect(url_for('dash')) #This redirects to another route
        else:
            return render_template('login.html',form=form) #This returns the html jinja template
    else:
        return render_template('login.html',form=form)

#Route for adding a site to the blogs
@app.route('/addsite',methods=['GET','POST'])
def addSite():
    form = AddSite()
    if 'username' in session: #Make sure user is logged in
        if request.method == 'POST' and form.validate():
            newBlog = Blog() #Create a new Blog entry object for the database
            newBlog.student = form.name.data #Set all of the attributes of the blog
            newBlog.url = form.url.data
            newBlog.titletag = form.titletag.data
            newBlog.titleclass = form.titleclass.data
            newBlog.bodytag = form.bodytag.data
            newBlog.bodyclass = form.bodyclass.data
            db.session.add(newBlog) #Add and commit it to the database
            db.session.commit()
            updateDatabase() #Update the database by recrawling 
            
            
            print("Commited")
        return render_template('addSite.html', form=form)
    else:
        return redirect(url_for('login'))

@app.route('/admindash', methods=['GET','POST'])
def dash():
    if 'username' in session:
        return render_template('admindash.html')
    else:
        return redirect(url_for('login'))

@app.route('/removesite', methods=['GET','POST'])
def removeSite():
    if 'username' in session:
        form = DeleteSite()
        if request.method == 'POST' and form.validate():
           name = form.studentName.data 
           blog = Blog.query.filter_by(student=name).first()
           db.session.delete(blog)
           db.session.commit()
           posts = Post.query.filter_by(author=name)
           for post in posts:
               db.session.delete(post)
           db.session.commit()
           updateDatabase()

        blogs = Blog.query.all()
        return render_template('removeSite.html',form=form,blogs=blogs)
    else:
        return redirect(url_for('home'))
    

