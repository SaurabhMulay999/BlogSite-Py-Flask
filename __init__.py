from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_bcrypt import Bcrypt
from flask_login import LoginManager
#conffig that below
#The urlfor is used too find the directory ot check the main description
#here i am config the secret key that can help us from random attacks
#cuurently i have declclare as a empty string here]

app=Flask(__name__) #here we have instantiated the flask application annd below we have created the routes\
app.config['SECRET_KEY']='acc0abfbd1cbcf3a457063549620b35b'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
#/// meqan that it is a relative path
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
#for @login required
login_manager.login_view='login'
login_manager.login_message_category='info'
#the info is a bootstrap class



#for password hashing Purpose

#we have a instance of this now
#this database in in form of classes like each class holds like a table
db=SQLAlchemy(app)

from flaskk import routes
