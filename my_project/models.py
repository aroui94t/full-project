# Models.py 
# Set up db inside the __init__ .py under my_project project folder

from my_project import db


# ===================> define class Member <===================
class Member(db.Model):
    
    # Name the table in database
    __tablename__ = 'members'

    # Name of Column:
    id       = db.Column(db.Integer,primary_key = True)
    username =  db.Column(db.Text)
    email    = db.Column(db.Text)
    age      = db.Column(db.Integer)
    password = db.Column(db.Text)

    # This is a one-to-many relationship
    # A member can have many posts
    posts = db.relationship('Post',backref='Member',lazy='dynamic')

    
    def __init__(self,username,email,age,password):
        self.username = username
        self.email = email
        self.age = age
        self.password  = password




# ===================> define class Post <===================

class Post(db.Model):
    # Name the table in database
    __tablename__ = 'posts'
    
    # Name of Column:
    id      = db.Column(db.Integer,primary_key = True)
    title   = db.Column(db.Text)
    content = db.Column(db.Text)
    
    # Connect the post to the member that owns it.
    # We use members.id because __tablename__='members'
    member_id = db.Column(db.Integer,db.ForeignKey('members.id'))

    def __init__(self,title,content,member_id):
        self.title = title
        self.content = content 
        self.member_id = member_id





