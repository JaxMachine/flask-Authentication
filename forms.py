from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import InputRequired, Length


class LoginForm(FlaskForm):
    """Login Form"""
    
    username = StringField("Username", validators=[InputRequired(), Length(min=1, max=20)],)
    password = PasswordField("Password", validators=[InputRequired(),Length(min=6, max=55)],)

class RegisterForm(FlaskForm):
    """Registration Form"""
    
    username = StringField("Username", validators=[InputRequired(), Length(min=1, max=20)],)
    password = PasswordField("Password", validators=[InputRequired(),Length(min=6, max=55)],)
    email = EmailField("Email", validators=[InputRequired(), Length(max=50)],)
    first_name= StringField("First Name", validators=[InputRequired(), Length(max=30)],)
    last_name=StringField("Last Name", validators=[InputRequired(), Length(max=30)],)
    


class FeedbackForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired(), Length(max=100)],)
    content = StringField("Content", validators=[InputRequired()],)
    

class DeleteForm(FlaskForm):
    """Delete Form, left Blank"""