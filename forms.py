from flask_wtf import FlaskForm
#impotitn a flask form, We have write in HTMLS but the [y form atomaticlaly converted into the htlm one
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired, Length, Email,EqualTo,ValidationError
from flaskk.models import User

class RegistrationForm(FlaskForm):
    #ffirst ffield we do want is a username
    username=StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])
    email=StringField('Email' , validators=[DataRequired(),Email() ])
    password=PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit=SubmitField('Sign Up')

    def validate_user(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username has been taken by someone, please try different one')

    def validate_email(self,email):
        email=User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('This email is taken , please chose ddiffernt')


class LoginForm(FlaskForm):
    #ffirst ffield we do want is a username
    #username=StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])
    email=StringField('Email' , validators=[DataRequired(),Email() ])
    password=PasswordField('Password', validators=[DataRequired()])
    #password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    remember=BooleanField('remember me')
    submit=SubmitField('Login')

