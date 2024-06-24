from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

def connect_db(app):
    """Connect to database."""
    
    db.app = app
    db.init_app(app)
    



class User(db.Model):
    
    __tablename__ = 'users'
    
    username = db.Column(db.Text, primary_key=True, nullable=False, unique=True)
    
    password = db.Column(db.Text, nullable=False)
    
    email = db.Column(db.String(50), nullable=False)
    
    first_name= db.Column(db.String(30), nullable=False)
    
    last_name= db.Column(db.String(30), nullable=False)
    
    @classmethod
    def register(cls, username, pwd, email, first_name, last_name):
        """Register user with a hashed password"""
        
        hashed = bcrypt.generate_password_hash(pwd)
         # turn bytestring into unicode utf8 string
        hashed_utf8 = hashed.decode("utf8")
        
        #return user with username and hased password
        user = cls(username=username, password=hashed_utf8, email=email, first_name=first_name, last_name=last_name)
        
        db.session.add(user)
        return user
    
    @classmethod
    def authenticate(cls, username, pwd):
        """Authenticate user exists and the credentials are correct"""
        
        u= User.query.filter_by(username=username).first()
        
        if u and bcrypt.check_password_hash(u.password, pwd):
            #return the user
            return u
        else:
            return False
        


class Feedback(db.Model):
    """Feedback Database"""
    
    __tablename__ = "feedback"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title= db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    username = db.Column(db.String(20), db.ForeignKey('users.username'), nullable=False)