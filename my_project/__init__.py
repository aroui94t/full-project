# __init__.py underneath my_project files

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
######################################
#### SET UP OUR SQLite DATABASE #####
####################################


app = Flask(__name__)


app.config['SECRET_KEY']  = 'mysecretkey'

# This grabs our directory
basedir = os.path.abspath(os.path.dirname(__file__))

# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)


from my_project.members.views import members_blueprints
from my_project.posts.views import posts_blueprints

app.register_blueprint(members_blueprints,url_prefix='/members')
app.register_blueprint(posts_blueprints,url_prefix='/posts')



