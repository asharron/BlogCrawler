# BlogCrawler
I have been working as a TA for Open Source Software Engineering and this class requires students to create and maintain blogs about what they learn in class. It is difficult for students to read other students blogs and it is also difficult to grade each blog individiaully since it requires one having access to all the links. This project is a blog aggregator that crawls each students blog and puts it in one place. This makes grading much easier and also allows each student to see each other's blog. 

# Who Is This For
This is for anyone who would like to be able to aggreagate blogs. For now, it is intended to be used by teachers and TAs so that they can view their student's blogs, though anyone may use it for their own purposes. 

# How It Works
Currently, each blog url is stored in an SQLite database and is then crawled by a python script. The crawler finds posts and stores it into the database.

# Condition
This is still being worked on and is quite buggy. As of this writting, I am currently working on making the crawler more sophisicated. Currently, the crawler works best with Wordpress blogs, but efforts are being made to make it work with a variety of web blogs. 
