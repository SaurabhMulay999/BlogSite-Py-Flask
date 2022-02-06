import flask_bcrypt
from flask import Flask,render_template, url_for,flash,redirect,request
from flaskk.models import User,Post
from flaskk.forms import RegistrationForm, LoginForm
from flaskk import app, db,bcrypt
from flask_login import login_user, current_user,logout_user,login_required
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot

englishBot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(englishBot)
trainer.train("chatterbot.corpus.english") #train the chatter bot for english


posts =[{'author':'Saurabh Mulay',
         'title':'Blog Post 1',
         'content':'Kulkarni and His 4th Wife',
        'date_posted':'July-2021'},

{       'author':'Abhishesk Ghrotale',
         'title':'Blog Post 2',
         'content':'Vishnupuri and the fucking petrol',
        'date_posted':'June-2021'
        }]

@app.route("/") #this is the forward slash shows the route page of a website or oue website
def helloWorld():
    pageTitle = "homepage"
    return render_template('home.html', posts=posts)
    #return "<h1>HeloFucking world</h1>"

@app.route("/about")
def theworld():
    return  render_template('about.html', title='TheAboutBlog')
    #return "<h2>The sceriest fukology ever </h2>"

@app.route("/Register" , methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if current_user.is_authenticated:
        return redirect(url_for('helloWorld'))
    if form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'The account has been created and you can login now!!!', 'success')
        #flash(f'The account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
        #update the layout page to flash the data or alert msg like js
        #we have to use the with statement there like ... with messages=get_flashed_messages(with_categories=True) here the categories mean nothing but the Success given in flash method


    return render_template('register.html', title='register the user' ,form=form)

@app.route("/Login",  methods=['GET','POST'])
def login():
    form=LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('helloWorld'))
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user,remember=form.remember.data)
            next_page=request.args.get(url_for('helloWorld'))

            return  redirect(next_page) if  next_page else redirect(url_for('helloWorld'))
            #import userlogin function
        else:
            flash('Unsuccessful attempt, please check your login id and password','danger')


    return render_template('Login.html', title='Login here' ,form=form)


@app.route("/Logout")
def logout():
    logout_user()
    return redirect(url_for('helloWorld'))

@app.route("/Account")
@login_required
def Account():
    return render_template('Window.html', title='Account' )

@app.route("/Info")
def info():
    return render_template('Window.html', title='info')

@app.route("/mustguidance")
def guidance():
    return render_template('form.html', title='MustGuidance')

@app.route("/bot")
def get_bot_response():
    userText = request.args.get('msg')
    return str(englishBot.get_response(userText))