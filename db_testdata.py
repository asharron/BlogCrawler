from app import db, models
import random

states = open('./text/us_cities_states_counties.csv','r').readlines()
names = open('./text/first-names.txt','r').readlines()
emails = open('./text/email.txt','r').readlines()
interests = ['Buisness','Computer Science', 'Art', 'Biology', 'Chemistry']

for email in emails:
     fname = names[random.randint(0,2000)].strip('\n')
     lname = names[random.randint(0,2000)].strip('\n')
     stateint = random.randint(0,2000)
     state = states[stateint].split('|')[2]
     city = states[stateint].split('|')[0]
     interest = interests[random.randint(0,4)]
     user = models.Mentee(fname=fname,lname=lname,password="password",state=state,city=city,email=email,interest=interest)
     db.session.add(user)
     db.session.commit()